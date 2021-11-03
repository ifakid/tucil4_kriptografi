from PyQt5 import QtWidgets, QtCore
from Algorithm import RSA
from Key import RSAKey
from Util import file


class RSA_UI(QtWidgets.QWidget):
    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)
        self.setObjectName("tab")
        self.rsa_opt = QtWidgets.QTabWidget(self)
        self.rsa_opt.setGeometry(QtCore.QRect(0, 0, 411, 591))
        self.rsa_opt.setObjectName("rsa_opt")

        self.tab_gen = RSA_Gen()
        self.rsa_opt.addTab(self.tab_gen, "")

        self.tab_enc = RSA_Enc()
        self.rsa_opt.addTab(self.tab_enc, "")

        self.tab_dec = RSA_Dec()
        self.rsa_opt.addTab(self.tab_dec, "")

        self.rsa_opt.setCurrentIndex(0)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate

        self.tab_gen.retranslateUi(Dialog)
        self.rsa_opt.setTabText(self.rsa_opt.indexOf(self.tab_gen), _translate("Dialog", "Generate"))

        self.tab_enc.retranslateUi(Dialog)
        self.rsa_opt.setTabText(self.rsa_opt.indexOf(self.tab_enc), _translate("Dialog", "Encrypt"))

        self.tab_dec.retranslateUi(Dialog)
        self.rsa_opt.setTabText(self.rsa_opt.indexOf(self.tab_dec), _translate("Dialog", "Decrypt"))


class RSA_Gen(QtWidgets.QTabWidget):
    def __init__(self, *args):
        self.rsa = None

        QtWidgets.QTabWidget.__init__(self, *args)
        self.setObjectName("tab_5")

        self.rsa_gen_len_lbl = QtWidgets.QLabel(self)
        self.rsa_gen_len_lbl.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.rsa_gen_len_lbl.setObjectName("rsa_gen_len_lbl")

        self.rsa_gen_len_text = QtWidgets.QLineEdit(self)
        self.rsa_gen_len_text.setGeometry(QtCore.QRect(110, 30, 261, 20))
        self.rsa_gen_len_text.setObjectName("rsa_gen_len_text")

        self.rsa_gen_lbl = QtWidgets.QLabel(self)
        self.rsa_gen_lbl.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.rsa_gen_lbl.setObjectName("rsa_gen_lbl")

        self.rsa_gen_file_text = QtWidgets.QLineEdit(self)
        self.rsa_gen_file_text.setGeometry(QtCore.QRect(110, 60, 261, 20))
        self.rsa_gen_file_text.setObjectName("rsa_gen_file_text")

        self.rsa_gen_button = QtWidgets.QPushButton(self)
        self.rsa_gen_button.setGeometry(QtCore.QRect(170, 120, 75, 23))
        self.rsa_gen_button.setObjectName("rsa_gen_button")
        self.rsa_gen_button.clicked.connect(self.generate)

        self.rsa_gen_file_lbl = QtWidgets.QLabel(self)
        self.rsa_gen_file_lbl.setGeometry(QtCore.QRect(10, 60, 91, 16))
        self.rsa_gen_file_lbl.setObjectName("rsa_gen_file_lbl")

        self.rsa_gen_dir_button = QtWidgets.QPushButton(self)
        self.rsa_gen_dir_button.setGeometry(QtCore.QRect(10, 90, 111, 23))
        self.rsa_gen_dir_button.setObjectName("rsa_gen_dir_button")
        self.rsa_gen_dir_button.clicked.connect(self.get_dir)

        self.rsa_gen_dir_name = QtWidgets.QLabel(self)
        self.rsa_gen_dir_name.setGeometry(QtCore.QRect(130, 100, 261, 16))
        self.rsa_gen_dir_name.setObjectName("rsa_gen_dir_name")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate

        self.rsa_gen_len_lbl.setText(_translate("Dialog", "Key length (bit):"))
        self.rsa_gen_lbl.setText(_translate("Dialog", "Generate Keys"))
        self.rsa_gen_button.setText(_translate("Dialog", "Generate"))
        self.rsa_gen_file_lbl.setText(_translate("Dialog", "File name:"))
        self.rsa_gen_dir_button.setText(_translate("Dialog", "Choose directory"))
        self.rsa_gen_dir_name.setText(_translate("Dialog", ""))

    def generate(self):
        m = QtWidgets.QMessageBox()
        if not self.rsa_gen_len_text.text():
            m.setWindowTitle("Error")
            m.setText("Please enter key length")
            m.exec()
        elif not self.rsa_gen_file_text.text():
            m.setWindowTitle("Error")
            m.setText("Please enter file name")
            m.exec()
        elif not self.rsa_gen_dir_name.text():
            m.setWindowTitle("Error")
            m.setText("Please choose directory")
            m.exec()
        else:
            key = RSAKey.RSAKey()
            try:
                key_len = int(self.rsa_gen_len_text.text())
                if key_len % 8:
                    raise ValueError()
                key.generate_key(key_len)
                path = self.rsa_gen_dir_name.text() + '/' + self.rsa_gen_file_text.text()
                key.export_public_key(path)
                key.export_private_key(path)

                m.setWindowTitle("Success")
                m.setText("Key has been successfully generated")
                m.exec()
            except:
                m.setWindowTitle("Error")
                m.setText("Please check the parameters")
                m.exec()

    def get_dir(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select a directory")
        print(path)
        self.rsa_gen_dir_name.setText(path)


class RSA_Enc(QtWidgets.QTabWidget):
    def __init__(self, *args):
        self.key = None
        self.mb = QtWidgets.QMessageBox()

        QtWidgets.QTabWidget.__init__(self, *args)
        self.setObjectName("tab_6")

        self.rsa_enc_n_lbl = QtWidgets.QLabel(self)
        self.rsa_enc_n_lbl.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.rsa_enc_n_lbl.setObjectName("rsa_enc_n_lbl")

        self.rsa_enc_n_text = QtWidgets.QTextEdit(self)
        self.rsa_enc_n_text.setGeometry(QtCore.QRect(80, 20, 301, 64))
        self.rsa_enc_n_text.setObjectName("rsa_enc_n_text")

        self.rsa_enc_key_file_lbl = QtWidgets.QLabel(self)
        self.rsa_enc_key_file_lbl.setGeometry(QtCore.QRect(60, 170, 21, 16))
        self.rsa_enc_key_file_lbl.setObjectName("rsa_enc_key_file_lbl")

        self.rsa_enc_key_file_button = QtWidgets.QPushButton(self)
        self.rsa_enc_key_file_button.setGeometry(QtCore.QRect(80, 170, 81, 23))
        self.rsa_enc_key_file_button.setObjectName("rsa_enc_key_file_button")
        self.rsa_enc_key_file_button.clicked.connect(self.import_key)

        self.rsa_enc_e_lbl = QtWidgets.QLabel(self)
        self.rsa_enc_e_lbl.setGeometry(QtCore.QRect(10, 90, 61, 16))
        self.rsa_enc_e_lbl.setObjectName("rsa_enc_e_lbl")

        self.rsa_enc_e_text = QtWidgets.QTextEdit(self)
        self.rsa_enc_e_text.setGeometry(QtCore.QRect(80, 90, 301, 64))
        self.rsa_enc_e_text.setObjectName("rsa_enc_e_text")

        self.label_16 = QtWidgets.QLabel(self)
        self.label_16.setGeometry(QtCore.QRect(10, 230, 61, 16))
        self.label_16.setObjectName("label_16")

        self.rsa_enc_m_text = QtWidgets.QTextEdit(self)
        self.rsa_enc_m_text.setGeometry(QtCore.QRect(80, 230, 301, 64))
        self.rsa_enc_m_text.setObjectName("rsa_enc_m_text")

        self.label_17 = QtWidgets.QLabel(self)
        self.label_17.setGeometry(QtCore.QRect(60, 300, 21, 16))
        self.label_17.setObjectName("label_17")

        self.rsa_enc_m_file_button = QtWidgets.QPushButton(self)
        self.rsa_enc_m_file_button.setGeometry(QtCore.QRect(80, 300, 81, 23))
        self.rsa_enc_m_file_button.setObjectName("rsa_enc_m_file_button")
        self.rsa_enc_m_file_button.clicked.connect(self.message_file)

        self.rsa_enc_key_lbl = QtWidgets.QLabel(self)
        self.rsa_enc_key_lbl.setGeometry(QtCore.QRect(10, 0, 47, 14))
        self.rsa_enc_key_lbl.setObjectName("rsa_enc_key_lbl")

        self.label_19 = QtWidgets.QLabel(self)
        self.label_19.setGeometry(QtCore.QRect(10, 210, 47, 14))
        self.label_19.setObjectName("label_19")

        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(0, 200, 411, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.label_20 = QtWidgets.QLabel(self)
        self.label_20.setGeometry(QtCore.QRect(10, 330, 47, 14))
        self.label_20.setObjectName("label_20")

        self.rsa_enc_save_file_button = QtWidgets.QPushButton(self)
        self.rsa_enc_save_file_button.setGeometry(QtCore.QRect(80, 330, 81, 23))
        self.rsa_enc_save_file_button.setObjectName("rsa_enc_save_file_button")
        self.rsa_enc_save_file_button.clicked.connect(self.save_file)

        self.rsa_enc_button = QtWidgets.QPushButton(self)
        self.rsa_enc_button.setGeometry(QtCore.QRect(170, 360, 75, 23))
        self.rsa_enc_button.setObjectName("rsa_enc_button")
        self.rsa_enc_button.clicked.connect(self.encrypt)

        self.rsa_enc_res_button = QtWidgets.QTextEdit(self)
        self.rsa_enc_res_button.setGeometry(QtCore.QRect(80, 390, 301, 64))
        self.rsa_enc_res_button.setObjectName("rsa_enc_res_button")

        self.label_30 = QtWidgets.QLabel(self)
        self.label_30.setGeometry(QtCore.QRect(10, 390, 61, 16))
        self.label_30.setObjectName("label_30")

        self.rsa_enc_key_file_name = QtWidgets.QLabel(self)
        self.rsa_enc_key_file_name.setGeometry(QtCore.QRect(170, 180, 211, 16))
        self.rsa_enc_key_file_name.setObjectName("rsa_enc_key_file_name")

        self.rsa_enc_m_file_name = QtWidgets.QLabel(self)
        self.rsa_enc_m_file_name.setGeometry(QtCore.QRect(170, 310, 211, 16))
        self.rsa_enc_m_file_name.setObjectName("rsa_enc_m_file_name")

        self.rsa_enc_save_file_name = QtWidgets.QLabel(self)
        self.rsa_enc_save_file_name.setGeometry(QtCore.QRect(170, 340, 211, 16))
        self.rsa_enc_save_file_name.setObjectName("rsa_enc_save_file_name")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate

        self.rsa_enc_n_lbl.setText(_translate("Dialog", "n"))
        self.rsa_enc_key_file_lbl.setText(_translate("Dialog", "or"))
        self.rsa_enc_key_file_button.setText(_translate("Dialog", "Choose file"))
        self.rsa_enc_e_lbl.setText(_translate("Dialog", "e"))
        self.label_16.setText(_translate("Dialog", "Message"))
        self.label_17.setText(_translate("Dialog", "or"))
        self.rsa_enc_m_file_button.setText(_translate("Dialog", "Choose file"))
        self.rsa_enc_key_lbl.setText(_translate("Dialog", "Key"))
        self.label_19.setText(_translate("Dialog", "Plaintext"))
        self.label_20.setText(_translate("Dialog", "Save"))
        self.rsa_enc_save_file_button.setText(_translate("Dialog", "Choose file"))
        self.rsa_enc_button.setText(_translate("Dialog", "Encrypt"))
        self.label_30.setText(_translate("Dialog", "Result"))
        self.rsa_enc_key_file_name.setText(_translate("Dialog", ""))
        self.rsa_enc_m_file_name.setText(_translate("Dialog", ""))
        self.rsa_enc_save_file_name.setText(_translate("Dialog", ""))

    def import_key(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, "Select public key")[0]
        if path:
            self.key = RSAKey.RSAKey()
            try:
                self.key.import_public_key(path)
                self.rsa_enc_key_file_name.setText(path)
                self.rsa_enc_e_text.setText(str(self.key.e))
                self.rsa_enc_n_text.setText(str(self.key.n))
                print("Key imported")
            except ValueError:
                self.key = None
                self.mb.setWindowTitle("Error")
                self.mb.setText("Invalid file")
                self.mb.exec()

    def message_file(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file')
        self.rsa_enc_m_file_name.setText(path[0])

    def save_file(self):
        path = QtWidgets.QFileDialog.getSaveFileName(self, 'Select file')
        self.rsa_enc_save_file_name.setText(path[0])

    def encrypt(self):
        mb = QtWidgets.QMessageBox()
        if not self.key and not(self.rsa_enc_e_text.toPlainText() and self.rsa_enc_n_text.toPlainText()):
            mb.setWindowTitle("Error")
            mb.setText("Please enter key or load a .pub file")
            mb.exec()
        elif not(self.rsa_enc_m_text.toPlainText() or self.rsa_enc_m_file_name.text()):
            mb.setWindowTitle("Error")
            mb.setText("Please enter a message or load a file to encrypt")
            mb.exec()
        else:
            try:
                if not self.key:
                    e = int(self.rsa_enc_e_text.toPlainText())
                    n = int(self.rsa_enc_n_text.toPlainText())
                    self.key = RSAKey.RSAKey()
                    self.key.e = e
                    self.key.n = n
                if self.rsa_enc_m_text.toPlainText():
                    message = self.rsa_enc_m_text.toPlainText().encode()
                else:
                    m_path = self.rsa_enc_m_file_name.text()
                    message = file.load_file(m_path)
                rsa = RSA.RSA(self.key)
                encrypted = rsa.encrypt(message)
                if self.rsa_enc_save_file_name.text():
                    file.write_file(self.rsa_enc_save_file_name.text(), encrypted)
                self.rsa_enc_res_button.setPlainText(encrypted.decode(encoding='latin-1'))
                mb.setWindowTitle("Success")
                mb.setText("File successfully encrypted")
                mb.exec()
            except:
                mb.setWindowTitle("Error")
                mb.setText("Please check the parameters")
                mb.exec()


class RSA_Dec(QtWidgets.QTabWidget):
    def __init__(self, *args):
        self.key = None

        QtWidgets.QTabWidget.__init__(self, *args)
        self.setObjectName("tab_7")

        self.label_21 = QtWidgets.QLabel(self)
        self.label_21.setGeometry(QtCore.QRect(10, 240, 61, 16))
        self.label_21.setObjectName("label_21")

        self.rsa_dec_m_text = QtWidgets.QTextEdit(self)
        self.rsa_dec_m_text.setGeometry(QtCore.QRect(80, 240, 301, 64))
        self.rsa_dec_m_text.setObjectName("rsa_dec_m_text")

        self.rsa_dec_m_file_button = QtWidgets.QPushButton(self)
        self.rsa_dec_m_file_button.setGeometry(QtCore.QRect(80, 310, 81, 23))
        self.rsa_dec_m_file_button.setObjectName("rsa_dec_m_file_button")
        self.rsa_dec_m_file_button.clicked.connect(self.message_file)

        self.rsa_dec_button = QtWidgets.QPushButton(self)
        self.rsa_dec_button.setGeometry(QtCore.QRect(170, 370, 75, 23))
        self.rsa_dec_button.setObjectName("rsa_dec_button")
        self.rsa_dec_button.clicked.connect(self.decrypt)

        self.label_22 = QtWidgets.QLabel(self)
        self.label_22.setGeometry(QtCore.QRect(10, 10, 47, 14))
        self.label_22.setObjectName("label_22")

        self.label_23 = QtWidgets.QLabel(self)
        self.label_23.setGeometry(QtCore.QRect(60, 180, 21, 16))
        self.label_23.setObjectName("label_23")

        self.label_24 = QtWidgets.QLabel(self)
        self.label_24.setGeometry(QtCore.QRect(60, 310, 21, 16))
        self.label_24.setObjectName("label_24")

        self.label_25 = QtWidgets.QLabel(self)
        self.label_25.setGeometry(QtCore.QRect(10, 340, 47, 14))
        self.label_25.setObjectName("label_25")

        self.label_26 = QtWidgets.QLabel(self)
        self.label_26.setGeometry(QtCore.QRect(10, 100, 61, 21))
        self.label_26.setObjectName("label_26")

        self.rsa_dec_save_file_button = QtWidgets.QPushButton(self)
        self.rsa_dec_save_file_button.setGeometry(QtCore.QRect(80, 340, 81, 23))
        self.rsa_dec_save_file_button.setObjectName("rsa_dec_save_file_button")
        self.rsa_dec_save_file_button.clicked.connect(self.save_file)

        self.rsa_dec_key_file_button = QtWidgets.QPushButton(self)
        self.rsa_dec_key_file_button.setGeometry(QtCore.QRect(80, 180, 81, 23))
        self.rsa_dec_key_file_button.setObjectName("rsa_dec_key_file_button")
        self.rsa_dec_key_file_button.clicked.connect(self.import_key)

        self.rsa_dec_d_text = QtWidgets.QTextEdit(self)
        self.rsa_dec_d_text.setGeometry(QtCore.QRect(80, 100, 301, 64))
        self.rsa_dec_d_text.setObjectName("rsa_dec_d_text")

        self.label_27 = QtWidgets.QLabel(self)
        self.label_27.setGeometry(QtCore.QRect(10, 30, 61, 16))
        self.label_27.setObjectName("label_27")

        self.rsa_dec_n_text = QtWidgets.QTextEdit(self)
        self.rsa_dec_n_text.setGeometry(QtCore.QRect(80, 30, 301, 64))
        self.rsa_dec_n_text.setObjectName("rsa_dec_n_text")

        self.label_28 = QtWidgets.QLabel(self)
        self.label_28.setGeometry(QtCore.QRect(10, 220, 61, 16))
        self.label_28.setObjectName("label_28")

        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(0, 210, 411, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.rsa_dec_res_button = QtWidgets.QTextEdit(self)
        self.rsa_dec_res_button.setGeometry(QtCore.QRect(80, 400, 301, 64))
        self.rsa_dec_res_button.setObjectName("rsa_dec_res_button")

        self.label_29 = QtWidgets.QLabel(self)
        self.label_29.setGeometry(QtCore.QRect(10, 400, 61, 16))
        self.label_29.setObjectName("label_29")

        self.rsa_dec_m_file_name = QtWidgets.QLabel(self)
        self.rsa_dec_m_file_name.setGeometry(QtCore.QRect(170, 320, 211, 16))
        self.rsa_dec_m_file_name.setObjectName("rsa_dec_m_file_name")

        self.rsa_dec_save_file_name = QtWidgets.QLabel(self)
        self.rsa_dec_save_file_name.setGeometry(QtCore.QRect(170, 350, 211, 16))
        self.rsa_dec_save_file_name.setObjectName("rsa_dec_save_file_name")

        self.rsa_dec_key_file_name = QtWidgets.QLabel(self)
        self.rsa_dec_key_file_name.setGeometry(QtCore.QRect(170, 190, 211, 16))
        self.rsa_dec_key_file_name.setObjectName("rsa_dec_key_file_name")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate

        self.label_21.setText(_translate("Dialog", "Message"))
        self.rsa_dec_m_file_button.setText(_translate("Dialog", "Choose file"))
        self.rsa_dec_button.setText(_translate("Dialog", "Decrypt"))
        self.label_22.setText(_translate("Dialog", "Key"))
        self.label_23.setText(_translate("Dialog", "or"))
        self.label_24.setText(_translate("Dialog", "or"))
        self.label_25.setText(_translate("Dialog", "Save"))
        self.label_26.setText(_translate("Dialog", "d"))
        self.rsa_dec_save_file_button.setText(_translate("Dialog", "Choose file"))
        self.rsa_dec_key_file_button.setText(_translate("Dialog", "Choose file"))
        self.label_27.setText(_translate("Dialog", "n"))
        self.label_28.setText(_translate("Dialog", "Ciphertext"))
        self.label_29.setText(_translate("Dialog", "Result"))
        self.rsa_dec_m_file_name.setText(_translate("Dialog", ""))
        self.rsa_dec_save_file_name.setText(_translate("Dialog", ""))
        self.rsa_dec_key_file_name.setText(_translate("Dialog", ""))

    def import_key(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, "Select private key")[0]
        if path:
            self.key = RSAKey.RSAKey()
            try:
                self.key.import_private_key(path)
                self.rsa_dec_key_file_name.setText(path)
                self.rsa_dec_d_text.setText(str(self.key.d))
                self.rsa_dec_n_text.setText(str(self.key.n))
            except ValueError:
                self.key = None
                self.mb.setWindowTitle("Error")
                self.mb.setText("Invalid file")
                self.mb.exec()

    def message_file(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file')
        self.rsa_dec_m_file_name.setText(path[0])

    def save_file(self):
        path = QtWidgets.QFileDialog.getSaveFileName(self, 'Select file')
        self.rsa_dec_save_file_name.setText(path[0])

    def decrypt(self):
        mb = QtWidgets.QMessageBox()
        if not self.key and not(self.rsa_dec_e_text.toPlainText() and self.rsa_dec_n_text.toPlainText()):
            mb.setWindowTitle("Error")
            mb.setText("Please enter key or load a .pub file")
            mb.exec()
        elif not(self.rsa_dec_m_text.toPlainText() or self.rsa_dec_m_file_name.text()):
            mb.setWindowTitle("Error")
            mb.setText("Please enter a message or load a file to decrypt")
            mb.exec()
        else:
            try:
                if not self.key:
                    d = int(self.rsa_dec_d_text.text())
                    n = int(self.rsa_dec_n_text.text())
                    self.key = RSAKey.RSAKey()
                    self.key.d = d
                    self.key.n = n
                if self.rsa_dec_m_text.toPlainText():
                    message = self.rsa_dec_m_text.toPlainText().encode()
                else:
                    m_path = self.rsa_dec_m_file_name.text()
                    message = file.load_file(m_path)
                rsa = RSA.RSA(self.key)
                decrypted = rsa.decrypt(message)
                if self.rsa_dec_save_file_name.text():
                    file.write_file(self.rsa_dec_save_file_name.text(), decrypted)
                self.rsa_dec_res_button.setPlainText(decrypted.decode(encoding='latin-1'))
                mb.setWindowTitle("Success")
                mb.setText("File successfully decrypted")
                mb.exec()
            except:
                mb.setWindowTitle("Error")
                mb.setText("Please check the parameters")
                mb.exec()