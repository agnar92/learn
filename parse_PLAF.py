#!/app/vbuild/RHEL6-x86_64/python/3.5.1/bin/python3.5
import subprocess
import json
import argparse

pathMicroService = "/env/rbsg2/bin/microServiceIf.py"
pathPlaf = "com.ericsson.interface.zipper.plaf"

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--track', dest="track", required=True,
                    help="Name of relase track that will shearch in lists")
parser.add_argument('-p', '--project', dest="project", required=True, help="Project name for load correct white list")
parser.add_argument('--artefact_id', dest="artefact_id", required=True, help="Product numbert to check and add to PLAF")
parser.add_argument('--product_name', dest="product_name", help="Name of product that will be add to plaf")
parser.add_argument('--list', dest="list_PLAF", required=True, help="What list have to be get from PLAF databse")

args = parser.parse_args()


# Load json file.
def open_json(file):
    with open(file) as jsonData:
        return json.load(jsonData)


# Add product to PLAF
def plaf_add(track, product, project, name, list_plaf):
    post = {"track": track, "product_number": product, "project": project, "module_name": name, "list_type": list_plaf}
    json_post = json.dumps(post)
    subprocess.cell(['/env/rbsg2/bin/microServiceIf.py -s com.ericsson.interface.zipper.plaf -r POST -d ' +
                     str(json.loads(json_post)) + ' -u /products'], shell=True)


# Get json list from PLAF
def plaf_call(track, project, file, list_plaf):
    with open(file, "w+") as output:
        subprocess.call([pathMicroService + " -s " + pathPlaf + " -r GET -u /products/projects/" + project +
                         "/tracks/" + track + "/list_types/" + list_plaf + " -p -q"], stdout=output, shell=True)


# Check if exist in PLAF, if not add
def plaf_check_add(file, product, key, track, project, name, list_plaf):
    for product_number in open_json(file):
        if product_number[key] == product:
            print("Product exists, willn't be added to the whitelist")
            exit(1)
    print("Product dont exists, adding to white list: ")
    plaf_add(track, product, project, name, list_plaf)


# Execute
if __name__ == '__main__':
    plaf_call(args.track, args.project, "output.json", args.list_PLAF)
    plaf_check_add("output.json", args.artefact_id, "product_number", args.track, args.project,
                   args.product_name, args.list_PLAF)
