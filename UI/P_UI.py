from PyQt5 import QtWidgets, QtCore
from Algorithm import Pailier
from Key import PaillierKey


class P_UI(QtWidgets.QWidget):
    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)
        self.setObjectName("tab_3")

        self.p_opt = QtWidgets.QTabWidget(self)
        self.p_opt.setGeometry(QtCore.QRect(0, 0, 411, 591))
        self.p_opt.setObjectName("p_opt")

        self.tab_gen = P_Gen()
        self.p_opt.addTab(self.tab_gen, "")

        self.tab_enc = P_Enc()
        self.p_opt.addTab(self.tab_enc, "")

        self.tab_dec = P_Dec()
        self.p_opt.addTab(self.tab_dec, "")

        self.p_opt.setCurrentIndex(0)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate

        self.tab_gen.retranslateUi(Dialog)
        self.p_opt.setTabText(self.p_opt.indexOf(self.tab_gen), _translate("Dialog", "Generate"))

        self.tab_enc.retranslateUi(Dialog)
        self.p_opt.setTabText(self.p_opt.indexOf(self.tab_enc), _translate("Dialog", "Encrypt"))

        self.tab_dec.retranslateUi(Dialog)
        self.p_opt.setTabText(self.p_opt.indexOf(self.tab_dec), _translate("Dialog", "Decrypt"))


class P_Gen(QtWidgets.QTabWidget):
    def __init__(self, *args):
        QtWidgets.QTabWidget.__init__(self, *args)
        self.setObjectName("tab_11")

        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.label_9.setObjectName("label_9")

        self.p_gen_len_text = QtWidgets.QLineEdit(self)
        self.p_gen_len_text.setGeometry(QtCore.QRect(110, 30, 261, 20))
        self.p_gen_len_text.setObjectName("p_gen_len_text")

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_3.setObjectName("label_3")

        self.p_gen_file_text = QtWidgets.QLineEdit(self)
        self.p_gen_file_text.setGeometry(QtCore.QRect(110, 60, 261, 20))
        self.p_gen_file_text.setObjectName("p_gen_file_text")

        self.p_gen_button = QtWidgets.QPushButton(self)
        self.p_gen_button.setGeometry(QtCore.QRect(170, 120, 75, 23))
        self.p_gen_button.setObjectName("p_gen_button")

        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(10, 60, 91, 16))
        self.label_10.setObjectName("label_10")

        self.p_gen_dir_button = QtWidgets.QPushButton(self)
        self.p_gen_dir_button.setGeometry(QtCore.QRect(10, 90, 121, 23))
        self.p_gen_dir_button.setObjectName("p_gen_dir_button")

        self.p_gen_dir_name = QtWidgets.QLabel(self)
        self.p_gen_dir_name.setGeometry(QtCore.QRect(140, 100, 251, 20))
        self.p_gen_dir_name.setObjectName("p_gen_dir_name")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.label_9.setText(_translate("Dialog", "Key length (bit):"))
        self.label_3.setText(_translate("Dialog", "Generate Keys"))
        self.p_gen_button.setText(_translate("Dialog", "Generate"))
        self.label_10.setText(_translate("Dialog", "File name:"))
        self.p_gen_dir_button.setText(_translate("Dialog", "Choose directory"))
        self.p_gen_dir_name.setText(_translate("Dialog", ""))


class P_Enc(QtWidgets.QTabWidget):
    def __init__(self, *args):
        QtWidgets.QTabWidget.__init__(self, *args)
        self.setObjectName("tab_12")

        self.label_50 = QtWidgets.QLabel(self)
        self.label_50.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_50.setObjectName("label_50")

        self.p_enc_g_text = QtWidgets.QTextEdit(self)
        self.p_enc_g_text.setGeometry(QtCore.QRect(80, 20, 301, 64))
        self.p_enc_g_text.setObjectName("p_enc_g_text")

        self.label_51 = QtWidgets.QLabel(self)
        self.label_51.setGeometry(QtCore.QRect(60, 170, 21, 16))
        self.label_51.setObjectName("label_51")

        self.p_enc_key_file_button = QtWidgets.QPushButton(self)
        self.p_enc_key_file_button.setGeometry(QtCore.QRect(80, 170, 81, 23))
        self.p_enc_key_file_button.setObjectName("p_enc_key_file_button")

        self.label_52 = QtWidgets.QLabel(self)
        self.label_52.setGeometry(QtCore.QRect(10, 90, 61, 16))
        self.label_52.setObjectName("label_52")

        self.p_enc_n_text = QtWidgets.QTextEdit(self)
        self.p_enc_n_text.setGeometry(QtCore.QRect(80, 90, 301, 64))
        self.p_enc_n_text.setObjectName("p_enc_n_text")

        self.label_53 = QtWidgets.QLabel(self)
        self.label_53.setGeometry(QtCore.QRect(10, 230, 61, 16))
        self.label_53.setObjectName("label_53")

        self.p_enc_m_text = QtWidgets.QTextEdit(self)
        self.p_enc_m_text.setGeometry(QtCore.QRect(80, 230, 301, 64))
        self.p_enc_m_text.setObjectName("p_enc_m_text")

        self.label_54 = QtWidgets.QLabel(self)
        self.label_54.setGeometry(QtCore.QRect(60, 300, 21, 16))
        self.label_54.setObjectName("label_54")

        self.p_enc_m_file_button = QtWidgets.QPushButton(self)
        self.p_enc_m_file_button.setGeometry(QtCore.QRect(80, 300, 81, 23))
        self.p_enc_m_file_button.setObjectName("p_enc_m_file_button")

        self.label_55 = QtWidgets.QLabel(self)
        self.label_55.setGeometry(QtCore.QRect(10, 0, 47, 14))
        self.label_55.setObjectName("label_55")

        self.label_56 = QtWidgets.QLabel(self)
        self.label_56.setGeometry(QtCore.QRect(10, 210, 47, 14))
        self.label_56.setObjectName("label_56")

        self.line_5 = QtWidgets.QFrame(self)
        self.line_5.setGeometry(QtCore.QRect(0, 200, 411, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        self.label_57 = QtWidgets.QLabel(self)
        self.label_57.setGeometry(QtCore.QRect(10, 330, 47, 14))
        self.label_57.setObjectName("label_57")

        self.p_enc_save_file_button = QtWidgets.QPushButton(self)
        self.p_enc_save_file_button.setGeometry(QtCore.QRect(80, 330, 81, 23))
        self.p_enc_save_file_button.setObjectName("p_enc_save_file_button")

        self.p_enc_button = QtWidgets.QPushButton(self)
        self.p_enc_button.setGeometry(QtCore.QRect(170, 360, 75, 23))
        self.p_enc_button.setObjectName("p_enc_button")

        self.p_enc_res_text = QtWidgets.QTextEdit(self)
        self.p_enc_res_text.setGeometry(QtCore.QRect(80, 390, 301, 64))
        self.p_enc_res_text.setObjectName("p_enc_res_text")

        self.label_58 = QtWidgets.QLabel(self)
        self.label_58.setGeometry(QtCore.QRect(10, 390, 61, 16))
        self.label_58.setObjectName("label_58")

        self.p_enc_key_file_name = QtWidgets.QLabel(self)
        self.p_enc_key_file_name.setGeometry(QtCore.QRect(170, 180, 211, 16))
        self.p_enc_key_file_name.setObjectName("p_enc_key_file_name")

        self.p_enc_m_file_name = QtWidgets.QLabel(self)
        self.p_enc_m_file_name.setGeometry(QtCore.QRect(170, 310, 211, 16))
        self.p_enc_m_file_name.setObjectName("p_enc_m_file_name")

        self.p_enc_save_file_name = QtWidgets.QLabel(self)
        self.p_enc_save_file_name.setGeometry(QtCore.QRect(170, 340, 211, 16))
        self.p_enc_save_file_name.setObjectName("p_enc_save_file_name")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.label_50.setText(_translate("Dialog", "g"))
        self.label_51.setText(_translate("Dialog", "or"))
        self.p_enc_key_file_button.setText(_translate("Dialog", "Choose file"))
        self.label_52.setText(_translate("Dialog", "n"))
        self.label_53.setText(_translate("Dialog", "Message"))
        self.label_54.setText(_translate("Dialog", "or"))
        self.p_enc_m_file_button.setText(_translate("Dialog", "Choose file"))
        self.label_55.setText(_translate("Dialog", "Key"))
        self.label_56.setText(_translate("Dialog", "Plaintext"))
        self.label_57.setText(_translate("Dialog", "Save"))
        self.p_enc_save_file_button.setText(_translate("Dialog", "Choose file"))
        self.p_enc_button.setText(_translate("Dialog", "Encrypt"))
        self.label_58.setText(_translate("Dialog", "Result"))
        self.p_enc_key_file_name.setText(_translate("Dialog", ""))
        self.p_enc_m_file_name.setText(_translate("Dialog", ""))
        self.p_enc_save_file_name.setText(_translate("Dialog", ""))


class P_Dec(QtWidgets.QTabWidget):
    def __init__(self, *args):
        QtWidgets.QTabWidget.__init__(self, *args)
        self.setObjectName("tab_13")

        self.label_59 = QtWidgets.QLabel(self)
        self.label_59.setGeometry(QtCore.QRect(10, 240, 61, 16))
        self.label_59.setObjectName("label_59")

        self.p_dec_m_text = QtWidgets.QTextEdit(self)
        self.p_dec_m_text.setGeometry(QtCore.QRect(80, 240, 301, 64))
        self.p_dec_m_text.setObjectName("p_dec_m_text")

        self.p_dec_m_file_button = QtWidgets.QPushButton(self)
        self.p_dec_m_file_button.setGeometry(QtCore.QRect(80, 310, 81, 23))
        self.p_dec_m_file_button.setObjectName("p_dec_m_file_button")

        self.p_dec_button = QtWidgets.QPushButton(self)
        self.p_dec_button.setGeometry(QtCore.QRect(170, 370, 75, 23))
        self.p_dec_button.setObjectName("p_dec_button")

        self.label_60 = QtWidgets.QLabel(self)
        self.label_60.setGeometry(QtCore.QRect(10, 10, 47, 14))
        self.label_60.setObjectName("label_60")

        self.label_61 = QtWidgets.QLabel(self)
        self.label_61.setGeometry(QtCore.QRect(60, 180, 21, 16))
        self.label_61.setObjectName("label_61")

        self.label_62 = QtWidgets.QLabel(self)
        self.label_62.setGeometry(QtCore.QRect(60, 310, 21, 16))
        self.label_62.setObjectName("label_62")

        self.label_63 = QtWidgets.QLabel(self)
        self.label_63.setGeometry(QtCore.QRect(10, 340, 47, 14))
        self.label_63.setObjectName("label_63")

        self.label_64 = QtWidgets.QLabel(self)
        self.label_64.setGeometry(QtCore.QRect(10, 100, 61, 21))
        self.label_64.setObjectName("label_64")

        self.p_dec_save_file_button = QtWidgets.QPushButton(self)
        self.p_dec_save_file_button.setGeometry(QtCore.QRect(80, 340, 81, 23))
        self.p_dec_save_file_button.setObjectName("p_dec_save_file_button")

        self.p_dec_key_file_button = QtWidgets.QPushButton(self)
        self.p_dec_key_file_button.setGeometry(QtCore.QRect(80, 180, 81, 23))
        self.p_dec_key_file_button.setObjectName("p_dec_key_file_button")

        self.p_dec_mu_text = QtWidgets.QTextEdit(self)
        self.p_dec_mu_text.setGeometry(QtCore.QRect(80, 100, 301, 64))
        self.p_dec_mu_text.setObjectName("p_dec_mu_text")

        self.label_65 = QtWidgets.QLabel(self)
        self.label_65.setGeometry(QtCore.QRect(10, 30, 61, 16))
        self.label_65.setObjectName("label_65")

        self.p_dec_lam_text = QtWidgets.QTextEdit(self)
        self.p_dec_lam_text.setGeometry(QtCore.QRect(80, 30, 301, 64))
        self.p_dec_lam_text.setObjectName("p_dec_lam_text")

        self.label_66 = QtWidgets.QLabel(self)
        self.label_66.setGeometry(QtCore.QRect(10, 220, 61, 16))
        self.label_66.setObjectName("label_66")

        self.line_6 = QtWidgets.QFrame(self)
        self.line_6.setGeometry(QtCore.QRect(0, 210, 411, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        self.p_dec_res_text = QtWidgets.QTextEdit(self)
        self.p_dec_res_text.setGeometry(QtCore.QRect(80, 400, 301, 64))
        self.p_dec_res_text.setObjectName("p_dec_res_text")

        self.label_67 = QtWidgets.QLabel(self)
        self.label_67.setGeometry(QtCore.QRect(10, 400, 61, 16))
        self.label_67.setObjectName("label_67")

        self.p_dec_key_file_name = QtWidgets.QLabel(self)
        self.p_dec_key_file_name.setGeometry(QtCore.QRect(170, 190, 211, 16))
        self.p_dec_key_file_name.setObjectName("p_dec_key_file_name")

        self.p_dec_save_file_name = QtWidgets.QLabel(self)
        self.p_dec_save_file_name.setGeometry(QtCore.QRect(170, 350, 211, 16))
        self.p_dec_save_file_name.setObjectName("p_dec_save_file_name")

        self.p_dec_m_file_name = QtWidgets.QLabel(self)
        self.p_dec_m_file_name.setGeometry(QtCore.QRect(170, 320, 211, 16))
        self.p_dec_m_file_name.setObjectName("p_dec_m_file_name")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.label_59.setText(_translate("Dialog", "Message"))
        self.p_dec_m_file_button.setText(_translate("Dialog", "Choose file"))
        self.p_dec_button.setText(_translate("Dialog", "Decrypt"))
        self.label_60.setText(_translate("Dialog", "Key"))
        self.label_61.setText(_translate("Dialog", "or"))
        self.label_62.setText(_translate("Dialog", "or"))
        self.label_63.setText(_translate("Dialog", "Save"))
        self.label_64.setText(_translate("Dialog", "mu"))
        self.p_dec_save_file_button.setText(_translate("Dialog", "Choose file"))
        self.p_dec_key_file_button.setText(_translate("Dialog", "Choose file"))
        self.label_65.setText(_translate("Dialog", "lambda"))
        self.label_66.setText(_translate("Dialog", "Ciphertext"))
        self.label_67.setText(_translate("Dialog", "Result"))
        self.p_dec_key_file_name.setText(_translate("Dialog", ""))
        self.p_dec_save_file_name.setText(_translate("Dialog", ""))
        self.p_dec_m_file_name.setText(_translate("Dialog", ""))