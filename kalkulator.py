from PyQt5.QtWidgets import QApplication, QWidget # podsawowe klasy interfejsu graficznego
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt

class Kalkulatro(QWidget): #dziedziczenie z klasy QWidget
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()


    def interfejs(self):

        self.resize(300, 100) # szerokosc okna
        self.setWindowTitle("Prosty Kalkulator")
        self.show() # wyswietla okno na ekranie

        # etykiety
        etykieta1 = QLabel("Liczba 1: ", self)
        etykieta2 = QLabel("Liczba 2: ", self)
        etykieta3 = QLabel("Wynik: ", self)

        # przypisanie widgetow do ukladu tabelarycznego
        ukladT = QGridLayout()
        ukladT.addWidget(etykieta1, 0, 0)
        ukladT.addWidget(etykieta2, 0, 1)
        ukladT.addWidget(etykieta3, 0, 3)

        #pisanie do okna
        self.setLayout(ukladT)

        self.setGeometry(20, 20, 300, 100) #polozenie okna na ekranie i rozmiar
        self.setWindowIcon(QIcon('kalkulator.png')) # ikona do pasku tytulowego lub miniaturze
        self.setWindowTitle("Prosty Kalkulator")
        self.show()

        # pole edycji
        self.liczba1Edt = QLineEdit()
        self.liczba2Edt = QLineEdit()
        self.wynikEdt = QLineEdit()

        self.wynikEdt.readonly = True # wylko odczyt pola

        ukladT.addWidget(self.liczba1Edt, 1, 0)
        ukladT.addWidget(self.liczba2Edt, 1, 1)
        ukladT.addWidget(self.wynikEdt, 1, 2)

        #przyciski
        dodajBtn = QPushButton("&Dodaj", self)
        odejmijBtn = QPushButton("&Odejmij", self)
        dzielBtn = QPushButton("&Dziel", self)
        mnozBtn = QPushButton("&Mnoz", self)
        koniecBtn = QPushButton("&Koniec", self)
        koniecBtn.resize(koniecBtn.sizeHint())
        koniecBtn.clicked.connect(self.koniec)

        ukladH = QHBoxLayout()
        ukladH.addWidget(dodajBtn)
        ukladH.addWidget(odejmijBtn)
        ukladH.addWidget(dzielBtn)
        ukladH.addWidget(mnozBtn)

        ukladT.addLayout(ukladH, 2, 0, 1, 3)
        ukladT.addWidget(koniecBtn, 3, 0, 1, 3)

        dodajBtn.clicked.connect(self.dzialanie)
        odejmijBtn.clicked.connect(self.dzialanie)
        dzielBtn.clicked.connect(self.dzialanie)
        mnozBtn.clicked.connect(self.dzialanie)

    def koniec(self):
        self.close()

    def closeEvent(self, QCloseEvent):
        odp = QMessageBox.question(self, 'Komunikat', "Czy napewno koniec?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No )

        if odp == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
            self.close()

    def dzialanie(self):
        nadawca = self.sender()

        try:
            liczba1 = float(self.liczba1Edt.text())
            liczba2 = float(self.liczba2Edt.text())
            wynik = ""

            if nadawca.text() == "&Dodaj":
                wynik = liczba1 + liczba2
            elif nadawca.text() == "&Odejmij":
                wynik = liczba1 - liczba2
            elif nadawca.text() == "&Mnoz":
                wynik = liczba1 * liczba2
            else:
                try:
                    wynik = round(liczba1 / liczba2, 9)
                except ZeroDivisionError:
                    QMessageBox.critical(self, "Blad", "Nie mozna dzielic przez zero!")
                    return

            self.wynikEdt.setText(str(wynik))
        except ValueError:
            QMessageBox.warning(self, "Blad", "Bledne Dane", QMessageBox.Ok)




if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv) # obiekt reprezentujacy aplikacjie, otrzymywanie paramtery z linie polecen dzieki sys.argv
    okno = Kalkulatro()
    sys.exit(app.exec_())

