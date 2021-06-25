from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap
import ID_auth_ui as ui
import UUID_ui as UUID
import subprocess
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import threading
from loadFigure import FigureSet

class Main(QMainWindow, ui.Ui_MainWindow, UUID.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #圖集
        fig = FigureSet()
        icon = QPixmap()
        icon.loadFromData(fig.icon)

        self.setWindowIcon(QtGui.QIcon(icon))
        self.setWindowTitle('全站儀資料轉換系統註冊')
        self.ok_button.clicked.connect(self.getUUID)
        self.emailSetting = None
        self.key = '+d=d5u6ebp&_0%1lt%0$!-qmw%ceal-49ere*^yaat&_u3-$d!'
    def send_email(self):
        try:
            smtp = smtplib.SMTP(host="smtp.gmail.com", port="587")  # 設定SMTP伺服器
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("2835jifu.6@gmail.com", "usdqgwhhqijlxjfn")  # 登入寄件者gmail
            print("Complete!")
            self.emailSetting = smtp
        except Exception as e:
            print("Error message: ", e)  
    def getUUID(self):
        if self.company_edit.text() == '' or self.man_edit.text() == '' or self.contact_edit.text() == '':
            QMessageBox.warning(self, "提醒", "請填入完整資訊")
        else:
            #取得UUID
            cmd = 'wmic csproduct get UUID'
            uuid = str(subprocess.check_output(cmd))
            pos1 = uuid.find("\\n")+2
            uuid = uuid[pos1:-15]
            #取得使用者輸入資訊
            companyName = self.company_edit.text()
            manName = self.man_edit.text()
            contactName = self.contact_edit.text()
            emailContent = companyName +"\n"+ manName +"\n"+ contactName +"\n"+ uuid
            #開啟UUIDwindow
            self.window = QtWidgets.QMainWindow()
            self.ui = UUID.Ui_MainWindow()
            self.ui.setupUi(self.window, self.enctry(uuid,self.key))
            self.window.show()
            #email設定
            content = MIMEMultipart()
            content["subject"] = "全站儀轉換程式註冊"
            content["from"] = "2835jifu.6@gmail.com"
            content["to"] = "2835jifu.6@gmail.com"
            content.attach(MIMEText(emailContent))
            try:
                self.emailSetting.send_message(content)
            except Exception as e:
                print(e)
    #加密
    def enctry(self,s,k):
        encry_str = ""
        for i,j in zip(s,k):
            # i為字元，j為祕鑰字元
            temp = str(ord(i)+ord(j))+'.' # 加密字元 = 字元的Unicode碼 + 祕鑰的Unicode碼
            encry_str = encry_str + temp
        return encry_str
        


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show() 
    send_email_t = threading.Thread(target = window.send_email)
    send_email_t.start()
    sys.exit(app.exec_())