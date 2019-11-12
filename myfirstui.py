from PyQt5 import QtCore, QtGui, QtWidgets
import chatbot_test

Main_string = ""
check_entering_cust_id = False
class Ui_Dialog(object):
    def add_status(self,childbot_index):
        global Main_string
        if(childbot_index == 1):
            name_of_bot = "Jason..."
        if(childbot_index == 2):
            name_of_bot = "Smith..."
        Main_string = Main_string + "Please wait.. Contacting "+ name_of_bot+"\n"
        self.textBrowser.setText(Main_string)
        
    def enter_text(self):
        global Main_string
        global check_entering_cust_id
        temp_text_string = self.lineEdit.text()
        Main_string = Main_string +temp_text_string+"\n"
        self.textBrowser.setText(Main_string)
        self.lineEdit.setText("")
        if(check_entering_cust_id == False):
            chatbot_test.get_cust_id(temp_text_string)
            check_entering_cust_id = True
            Main_string+="Please enter your query \n"
            self.textBrowser.setText(Main_string)
        else:
            response = chatbot_test.get_reply(temp_text_string)
            response_string = response[0] + "\n"
            self.add_status(response[1])
            Main_string+=response_string
            Main_string+="Please enter any more queries \n"
            self.textBrowser.setText(Main_string)


    def reset_text(self):
        self.textBrowser.setText("")
        self.lineEdit.setText("")
    
    def get_faq_ui(self):
        self.textBrowser.setText(chatbot_test.get_faq())

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(300, 250, 51, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.enter_text)

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 250, 51, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.reset_text)

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 270, 51, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_3.clicked.connect(self.get_faq_ui)


        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 250, 221, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Enter your message here")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(70, 10, 321, 231))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        global Main_string
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dell customer service"))
        self.pushButton.setText(_translate("Dialog", "Enter"))
        self.pushButton_2.setText(_translate("Dialog", "Reset"))
        self.pushButton_3.setText(_translate("Dialog","FAQ"))
        temp_greetings = chatbot_test.get_greetings() + "\n"
        Main_string+= temp_greetings
        self.textBrowser.setText(temp_greetings)

        
def init_ui():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    init_ui()
