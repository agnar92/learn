from __future__ import unicode_literals
from ksztalt import Ksztalty, Ksztalt
from PyQt5.QtWidgets import QHBoxLayout

class Ui_Widget(object):

    def setupUi(self, Widgety):

        self.ksztalt = Ksztalt(self, Ksztalty.Polygon)

        ukladH1 = QHBoxLayout()
        ukladH1.addWidget(self.ksztalt)

        self.setLayout(ukladH1)
        self.setWindowTitle('widzety')