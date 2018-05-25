from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtCore import QPoint, QRect, QSize

class Ksztalty:
    Rect, Ellipse, Polygon, Line = range(4)

class Ksztalt(QWidget):

    prost = QRect(1, 1, 101, 101)
    punkty = QPolygon([
        QPoint(1, 101),
        QPoint(51, 1),
        QPoint(101, 101)
    ])

    def __init__(self, parent, ksztalt=Ksztalty.Rect):
        super(Ksztalt, self).__init__(parent)

        self.ksztalt = ksztalt
        self.kolorO = QColor(0, 0, 0)
        self.kolorW = QColor(255, 255, 255)

    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        self.rysujFigure(QPaintEvent, qp)
        qp.end()

    def rysujFigury(self, QpaintEvent, qp):
        qp.setPen(self.kolorO)
        qp.setBruch(self.kolorW)
        qp.setRenderHint(QPainter.Antialiasing)

        if self.ksztalt == Ksztalty.Rect:
            qp.drawRect(self.prost)
        elif self.ksztalt == Ksztalty.Ellipse:
            qp.drawEllipse(self.prost)
        elif self.ksztalt == Ksztalty.Polygon:
            qp.drawPolygon(self.punkty)
        elif self.ksztalt == Ksztalty.Line:
            qp.drawLine(self.prost.topLeft(), self.prost.bottomRight())
        else:
            qp.drawRect(self.prost)

    def sizeHint(self):
        return QSize(102, 102)

    def minimumSizeHint(self):
        return QSize(102, 102)

    def ustawKsztalt(self, ksztalt):
        self.ksztalt = ksztalt
        self.update()

    def ustawKolorW(self, r=0, g=0, b=0):
        self.kolorW = QColor(r, g, b)
        self.update()