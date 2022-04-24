import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from mainwindow import main_ui
from login import login_ui


class my_loginui(QMainWindow, login_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login.clicked.connect(self.check_login)

    def check_login(self):
        username = self.username.text()
        password = self.password.text()
        if len(username) >= 2 and len(password) >= 6:
            main.show()
            self.hide()
        else:
            QMessageBox.warning(self, '登陆失败', '用户名长度必须大于等于2，密码长度必须大于等于6！')


class my_mainui(QMainWindow, main_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = my_loginui()
    main = my_mainui()
    login.show()
    sys.exit(app.exec_())
