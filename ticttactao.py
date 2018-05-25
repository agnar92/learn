import sys
class TickTak(object):

    def __init__(self):
        self.board = [['']*12 for i in range(12)]
        self.count = 0


    def _print_board(self):
        for i in range(11):
            print(''.join(self.board[i]))

    def display_board(self):
        for i in range(12):
            if i is 3 or i is 7:
                self.board[i] = ["-"]*11
            else:
                self.board[i] = ([" "]*3+['|'])*2+[" "]*3
        self._print_board()

    def refrash(self, row=0, kol=0, str=""):
        while self.board[row][kol] == 'X' or self.board[row][kol] == 'O':
            num = input('This field is already pick. Chose another section 1-9: ')
            print(str)
            row, kol = self.switch(int(num), str, True)

        print("\n" * 20)
        self.board[row][kol] = str
        self._print_board()

    def switch(self, num, str, re=False):
        switch = {
            1: [1, 1],
            2: [1, 5],
            3: [1, 9],
            4: [5, 1],
            5: [5, 5],
            6: [5, 9],
            7: [9, 1],
            8: [9, 5],
            9: [9, 9],
        }[num]
        return (self.refrash(switch[0], switch[1], str) if re is False else switch)

    def player_input(self, player=None):
        print("%s" % player)
        self.count += 1
        return input('Chose section 1-9: '), self.count

    def check_logic(self):
        result = False
        vertical_mach = [1,5,9]
        # horizontal search
        for i in range(12):
            mach_x_h = []
            mach_o_h = []
            # horizonatal
            mach_x_h += [x for x in self.board[i] if x == 'X']
            mach_o_h += [x for x in self.board[i] if x == 'O']
            if len(mach_x_h) is 3 or len(mach_o_h) is 3:
                print("Win H")
                sys.exit(0)
        # vertical
        for i in vertical_mach:
            mach_x_v = []
            mach_o_v = []
            mach_x_v += [x for x in range(12) if self.board[x][i] == 'X']
            mach_o_v += [x for x in range(12) if self.board[x][i] == 'O']
            if len(mach_x_v) is 3 or len(mach_o_v) is 3:
                print('Win V')
                sys.exit(0)
    def replay(self):
        main()

def main():
    t = TickTak()
    t.display_board()
    play = input('If you want to play write Yes or No \n')
    player_1 = input("Player one chose X or O \n")
    if player_1.lower() == "x":
        player_2 = "O"
    else:
        player_2 = "X"
    while play.lower() == "yes":
        num_1, count = t.player_input("Player_1")
        if num_1.lower() == "exit":
            sys.exit(0)
        t.switch(int(num_1), player_1.upper())
        t.check_logic()
        if count is 9: break
        num_2, count = t.player_input("Player_2")
        if num_2.lower() == "exit":
            sys.exit(0)
        t.switch(int(num_2), player_2.upper())
        t.check_logic()
        if count is 9: break

    replay = input('do you want replay? Yes or No \n')
    if replay.lower() == "yes":
        t.replay()
    else:
        print('Finish game!')
        sys.exit(0)

if __name__ == '__main__':
    main()
