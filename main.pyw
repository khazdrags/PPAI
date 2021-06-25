import gestor_reserva_visita as gestor
import sys
from PyQt5 import QtCore, QtWidgets, QtCore
from PyQt5.QtWidgets import (QLabel, QRadioButton, QPushButton, QVBoxLayout, QApplication, QWidget)
# Import the page designed by Qt designer
from interfaz.untitled import Ui_Dialog as screen1
from interfaz.interfaz import Ui_Registrarreserva as screen2

gestorReservaVisita1=gestor.Gestor_reserva_visita()

class HelloWindow(QtWidgets.QMainWindow, screen1):
    switch_window1 = QtCore.pyqtSignal() # Jump signal
    def __init__(self):
        super(HelloWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.goscreen2)
    def goscreen2(self):
        self.switch_window1.emit()



class LoginWindow(QtWidgets.QMainWindow, screen2):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        
    
class Controller:
    def __init__(self):
        pass
    # Jump to the hello window
    def show_hello(self):
        self.hello = HelloWindow()
        self.hello.switch_window1.connect(self.show_login)
        self.hello.show()
    # Jump to the login window, pay attention to close the original page
    def show_login(self):
        self.login = LoginWindow()
        self.hello.close()
        self.login.show()



app = QtWidgets.QApplication(sys.argv)
controller = Controller() # Controller instance
controller.show_hello() # The default display is the hello page

sys.exit(app.exec_())








print('-------------------------------------------------------------------------------------------------------------------------------------------')
print('-------------------------------------------------------------------------------------------------------------------------------------------')
print('-------------------------------------------------------------------------------------------------------------------------------------------')
