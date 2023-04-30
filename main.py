from PyQt5 import QtWidgets, uic

class MiVentana(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui_files/diseñochvre.ui', self)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MiVentana()
    window.show()
    app.exec_()

print("Hola a todos")

print("Mi novia es daniela")