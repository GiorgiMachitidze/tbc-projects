'''
კოდში ვქმნით ფანჯარას, რომელსაც ვარქმევთ Login Formს, ვუწერთ ზომებს, ამ ფანჯარაზე გვაქვს
შექმნილი ორი label, ერთი პაროლისთვის, რომელსაც ფლეისჰოლდერტექსტის საშუალებით ვაწერთ
password, ხოლო მეორე label არის იუზერნეიმისთვის და იგივეს ვაკეთებთ მისთვისაც. ასევე გვაქვს Sign in
pushbutton. წინასწარ გვაქვს ჩაჰარდკოდებული პაროლი და იუზერნეიმი. თუ მომხმარებლის მიერ
შეყვანილი პაროლი და იუზერნეიმი სწორია pushbuton-ზე დაჭერის შემდეგ ჩნდება ახალი ფეიჯი,
რომელიც გვეუბნება "Authorization successful!", ეს ხდება stackwidget-ის საშუალებით. თუ მომხმარებლის
მიერ შეყვანილი მონაცემები არასწორია ვასუფთვებთ ველებს, გამოგვაქვს შეტყობინება: "Please try again!"
და ვრჩებით იგივე ფეიჯზე. ასევე გვაქვს show password ჩექბოქსი, რომლის მონიშვნის შემდეგ პაროლი
გამოჩნდება თუ არ მოვნიშნავთ ამ შემთხვევაში უხილავი იქნება, რასაც setEchoMode უზრუნველყოფს. პაროლის გამოჩენა
დაჰაიდებას კი უზრუნველყოფს ფუნქცია password_visibility. კოდში ასევე გაწერილია პაროლის დავიწყებისა და აქაუნთის
შექმნის ლეიბლები და მათი სიესესი.
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel


class SuccessfulSignInWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout(self)
        self.message_label = QtWidgets.QLabel("Authorization successful!", self)
        self.message_label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.message_label.setFont(font)
        layout.addWidget(self.message_label)

class Ui_MainWindow(object):
    def sign_in(self):
        if self.lineEdit.text() == self.user and self.lineEdit_2.text() == self.pas:
            self.stacked_widget.setCurrentIndex(1)
        else:
            self.label.setText("Please try again!")
            self.lineEdit.clear()
            self.lineEdit_2.clear()

    def setupUi(self, MainWindow):
        self.pas = "password"
        self.user = "username"

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 200)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.stacked_widget = QtWidgets.QStackedWidget(self.centralwidget)
        self.login_widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(self.login_widget)

        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setPlaceholderText("Username")
        self.lineEdit.setStyleSheet("padding: 10px; border: 2px solid #ccc; border-radius: 5px;")
        layout.addWidget(self.lineEdit)

        self.lineEdit_2 = QtWidgets.QLineEdit()
        self.lineEdit_2.setPlaceholderText("Password")
        self.lineEdit_2.setStyleSheet("padding: 10px; border: 2px solid #ccc; border-radius: 5px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        layout.addWidget(self.lineEdit_2)

        self.show_password_checkbox = QtWidgets.QCheckBox("Show Password")
        layout.addWidget(self.show_password_checkbox)

        self.label = QtWidgets.QLabel()
        layout.addWidget(self.label)

        self.pushButton = QtWidgets.QPushButton("Sign In")
        layout.addWidget(self.pushButton)
        self.pushButton.setStyleSheet("background-color: #4267B2; color: white; padding: 10px; border: none; border-radius: 5px;")
        layout.addStretch()

        self.stacked_widget.addWidget(self.login_widget)

        self.forgot_password_label = QLabel("<a href='#'>Forgot Password?</a>")
        self.forgot_password_label.setStyleSheet("color: #4267B2;")
        self.forgot_password_label.setOpenExternalLinks(True)
        layout.addWidget(self.forgot_password_label, alignment=Qt.AlignmentFlag.AlignRight)

        self.create_account_label = QLabel("Don't have an account? <a href='#'>Sign Up</a>")
        self.create_account_label.setStyleSheet("color: #4267B2;")
        self.create_account_label.setOpenExternalLinks(True)
        layout.addWidget(self.create_account_label, alignment=Qt.AlignmentFlag.AlignRight)

        self.successful_widget = SuccessfulSignInWindow()
        self.stacked_widget.addWidget(self.successful_widget)

        self.pushButton.clicked.connect(self.sign_in)
        self.show_password_checkbox.stateChanged.connect(self.password_visibility)

        MainWindow.setCentralWidget(self.stacked_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login Form"))
        self.pushButton.setText(_translate("MainWindow", "Sign In"))

    def password_visibility(self, state):
        if state == QtCore.Qt.Checked:
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
