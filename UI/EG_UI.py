from PyQt5 import QtWidgets, QtCore
from Algorithm import ElGamal
from Key import ElGamalKey


class EG_UI(QtWidgets.QWidget):
    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)
        self.setObjectName("tab_2")

        self.eg_opt = QtWidgets.QTabWidget(self)
        self.eg_opt.setGeometry(QtCore.QRect(0, 0, 411, 591))
        self.eg_opt.setObjectName("eg_opt")

        self.tab_gen = EG_Gen()
        self.eg_opt.addTab(self.tab_gen, "")

        self.tab_enc = EG_Enc()
        self.eg_opt.addTab(self.tab_enc, "")

        self.tab_dec = EG_Dec()
        self.eg_opt.addTab(self.tab_dec, "")

        self.eg_opt.setCurrentIndex(0)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate

        self.tab_gen.retranslateUi(Dialog)
        self.eg_opt.setTabText(self.eg_opt.indexOf(self.tab_gen), _translate("Dialog", "Generate"))

        self.tab_enc.retranslateUi(Dialog)
        self.eg_opt.setTabText(self.eg_opt.indexOf(self.tab_enc), _translate("Dialog", "Encrypt"))

        self.tab_dec.retranslateUi(Dialog)
        self.eg_opt.setTabText(self.eg_opt.indexOf(self.tab_dec), _translate("Dialog", "Decrypt"))


class EG_Gen(QtWidgets.QTabWidget):
    def __init__(self, *args):
        QtWidgets.QTabWidget.__init__(self, *args)
        self.setObjectName("tab_8")

        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.label_7.setObjectName("label_7")

        self.eg_gen_len_text = QtWidgets.QLineEdit(self)
        self.eg_gen_len_text.setGeometry(QtCore.QRect(112, 30, 261, 20))
        self.eg_gen_len_text.setObjectName("eg_gen_len_text")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_2.setObjectName("label_2")

        self.eg_gen_file_text = QtWidgets.QLineEdit(self)
        self.eg_gen_file_text.setGeometry(QtCore.QRect(112, 60, 261, 20))
        self.eg_gen_file_text.setObjectName("eg_gen_file_text")

        self.eg_gen_button = QtWidgets.QPushButton(self)
        self.eg_gen_button.setGeometry(QtCore.QRect(170, 120, 75, 23))
        self.eg_gen_button.setObjectName("eg_gen_button")

        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(10, 60, 91, 16))
        self.label_8.setObjectName("label_8")

        self.eg_gen_dir_button = QtWidgets.QPushButton(self)
        self.eg_gen_dir_button.setGeometry(QtCore.QRect(10, 90, 111, 23))
        self.eg_gen_dir_button.setObjectName("eg_gen_dir_button")

        self.eg_gen_dir_name = QtWidgets.QLabel(self)
        self.eg_gen_dir_name.setGeometry(QtCore.QRect(130, 100, 261, 16))
        self.eg_gen_dir_name.setObjectName("eg_gen_dir_name")
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate

        self.label_7.setText(_translate("Dialog", "Key length (bit):"))
        self.label_2.setText(_translate("Dialog", "Generate Keys"))
        self.eg_gen_button.setText(_translate("Dialog", "Generate"))
        self.label_8.setText(_translate("Dialog", "File name:"))
        self.eg_gen_dir_button.setText(_translate("Dialog", "Choose directory"))
        self.eg_gen_dir_name.setText(_translate("Dialog", ""))


class EG_Enc(QtWidgets.QTabWidget):
    def __init__(self, *args):
        QtWidgets.QTabWidget.__init__(self, *args)
        self.setObjectName("tab_9")

        self.label_31 = QtWidgets.QLabel(self)
        self.label_31.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_31.setObjectName("label_31")

        self.eg_enc_p_text = QtWidgets.QTextEdit(self)
        self.eg_enc_p_text.setGeometry(QtCore.QRect(80, 20, 301, 64))
        self.eg_enc_p_text.setObjectName("eg_enc_p_text")

        self.label_32 = QtWidgets.QLabel(self)
        self.label_32.setGeometry(QtCore.QRect(60, 230, 21, 16))
        self.label_32.setObjectName("label_32")

        self.eg_enc_key_file_button = QtWidgets.QPushButton(self)
        self.eg_enc_key_file_button.setGeometry(QtCore.QRect(80, 230, 81, 23))
        self.eg_enc_key_file_button.setObjectName("eg_enc_key_file_button")

        self.label_33 = QtWidgets.QLabel(self)
        self.label_33.setGeometry(QtCore.QRect(10, 90, 61, 16))
        self.label_33.setObjectName("label_33")

        self.eg_enc_g_text = QtWidgets.QTextEdit(self)
        self.eg_enc_g_text.setGeometry(QtCore.QRect(80, 90, 301, 64))
        self.eg_enc_g_text.setObjectName("eg_enc_g_text")

        self.label_34 = QtWidgets.QLabel(self)
        self.label_34.setGeometry(QtCore.QRect(10, 290, 61, 16))
        self.label_34.setObjectName("label_34")

        self.eg_enc_m_text = QtWidgets.QTextEdit(self)
        self.eg_enc_m_text.setGeometry(QtCore.QRect(80, 290, 301, 64))
        self.eg_enc_m_text.setObjectName("eg_enc_m_text")

        self.label_35 = QtWidgets.QLabel(self)
        self.label_35.setGeometry(QtCore.QRect(60, 360, 21, 16))
        self.label_35.setObjectName("label_35")

        self.eg_enc_m_file_button = QtWidgets.QPushButton(self)
        self.eg_enc_m_file_button.setGeometry(QtCore.QRect(80, 360, 81, 23))
        self.eg_enc_m_file_button.setObjectName("eg_enc_m_file_button")

        self.label_36 = QtWidgets.QLabel(self)
        self.label_36.setGeometry(QtCore.QRect(10, 0, 47, 14))
        self.label_36.setObjectName("label_36")

        self.label_37 = QtWidgets.QLabel(self)
        self.label_37.setGeometry(QtCore.QRect(10, 270, 47, 14))
        self.label_37.setObjectName("label_37")

        self.line_3 = QtWidgets.QFrame(self)
        self.line_3.setGeometry(QtCore.QRect(0, 260, 411, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.label_38 = QtWidgets.QLabel(self)
        self.label_38.setGeometry(QtCore.QRect(10, 390, 47, 14))
        self.label_38.setObjectName("label_38")

        self.eg_enc_save_file_button = QtWidgets.QPushButton(self)
        self.eg_enc_save_file_button.setGeometry(QtCore.QRect(80, 390, 81, 23))
        self.eg_enc_save_file_button.setObjectName("eg_enc_save_file_button")

        self.eg_enc_button = QtWidgets.QPushButton(self)
        self.eg_enc_button.setGeometry(QtCore.QRect(170, 420, 75, 23))
        self.eg_enc_button.setObjectName("eg_enc_button")

        self.eg_enc_res_text = QtWidgets.QTextEdit(self)
        self.eg_enc_res_text.setGeometry(QtCore.QRect(80, 450, 301, 64))
        self.eg_enc_res_text.setObjectName("eg_enc_res_text")

        self.label_39 = QtWidgets.QLabel(self)
        self.label_39.setGeometry(QtCore.QRect(10, 450, 61, 16))
        self.label_39.setObjectName("label_39")

        self.eg_enc_y_text = QtWidgets.QTextEdit(self)
        self.eg_enc_y_text.setGeometry(QtCore.QRect(80, 160, 301, 64))
        self.eg_enc_y_text.setObjectName("eg_enc_y_text")

        self.label_49 = QtWidgets.QLabel(self)
        self.label_49.setGeometry(QtCore.QRect(10, 160, 61, 16))
        self.label_49.setObjectName("label_49")

        self.eg_enc_key_file_name = QtWidgets.QLabel(self)
        self.eg_enc_key_file_name.setGeometry(QtCore.QRect(170, 240, 211, 16))
        self.eg_enc_key_file_name.setObjectName("eg_enc_key_file_name")

        self.eg_enc_m_file_name = QtWidgets.QLabel(self)
        self.eg_enc_m_file_name.setGeometry(QtCore.QRect(170, 370, 211, 16))
        self.eg_enc_m_file_name.setObjectName("eg_enc_m_file_name")

        self.eg_enc_save_file_name = QtWidgets.QLabel(self)
        self.eg_enc_save_file_name.setGeometry(QtCore.QRect(170, 400, 211, 16))
        self.eg_enc_save_file_name.setObjectName("eg_enc_save_file_name")
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate

        self.label_31.setText(_translate("Dialog", "p"))
        self.label_32.setText(_translate("Dialog", "or"))
        self.eg_enc_key_file_button.setText(_translate("Dialog", "Choose file"))
        self.label_33.setText(_translate("Dialog", "g"))
        self.label_34.setText(_translate("Dialog", "Message"))
        self.label_35.setText(_translate("Dialog", "or"))
        self.eg_enc_m_file_button.setText(_translate("Dialog", "Choose file"))
        self.label_36.setText(_translate("Dialog", "Key"))
        self.label_37.setText(_translate("Dialog", "Plaintext"))
        self.label_38.setText(_translate("Dialog", "Save"))
        self.eg_enc_save_file_button.setText(_translate("Dialog", "Choose file"))
        self.eg_enc_button.setText(_translate("Dialog", "Encrypt"))
        self.label_39.setText(_translate("Dialog", "Result"))
        self.label_49.setText(_translate("Dialog", "y"))
        self.eg_enc_key_file_name.setText(_translate("Dialog", ""))
        self.eg_enc_m_file_name.setText(_translate("Dialog", ""))
        self.eg_enc_save_file_name.setText(_translate("Dialog", ""))


class EG_Dec(QtWidgets.QTabWidget):
    def __init__(self, *args):
        QtWidgets.QTabWidget.__init__(self, *args)
        self.setObjectName("tab_10")

        self.label_40 = QtWidgets.QLabel(self)
        self.label_40.setGeometry(QtCore.QRect(10, 240, 61, 16))
        self.label_40.setObjectName("label_40")

        self.eg_dec_m_text = QtWidgets.QTextEdit(self)
        self.eg_dec_m_text.setGeometry(QtCore.QRect(80, 240, 301, 64))
        self.eg_dec_m_text.setObjectName("eg_dec_m_text")

        self.eg_dec_m_file_text = QtWidgets.QPushButton(self)
        self.eg_dec_m_file_text.setGeometry(QtCore.QRect(80, 310, 81, 23))
        self.eg_dec_m_file_text.setObjectName("eg_dec_m_file_text")

        self.eg_dec_button = QtWidgets.QPushButton(self)
        self.eg_dec_button.setGeometry(QtCore.QRect(170, 370, 75, 23))
        self.eg_dec_button.setObjectName("eg_dec_button")

        self.label_41 = QtWidgets.QLabel(self)
        self.label_41.setGeometry(QtCore.QRect(10, 10, 47, 14))
        self.label_41.setObjectName("label_41")

        self.label_42 = QtWidgets.QLabel(self)
        self.label_42.setGeometry(QtCore.QRect(60, 180, 21, 16))
        self.label_42.setObjectName("label_42")

        self.label_43 = QtWidgets.QLabel(self)
        self.label_43.setGeometry(QtCore.QRect(60, 310, 21, 16))
        self.label_43.setObjectName("label_43")

        self.label_44 = QtWidgets.QLabel(self)
        self.label_44.setGeometry(QtCore.QRect(10, 340, 47, 14))
        self.label_44.setObjectName("label_44")

        self.label_45 = QtWidgets.QLabel(self)
        self.label_45.setGeometry(QtCore.QRect(10, 100, 61, 21))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())

        self.label_45.setSizePolicy(sizePolicy)
        self.label_45.setObjectName("label_45")

        self.eg_dec_save_file_text = QtWidgets.QPushButton(self)
        self.eg_dec_save_file_text.setGeometry(QtCore.QRect(80, 340, 81, 23))
        self.eg_dec_save_file_text.setObjectName("eg_dec_save_file_text")

        self.eg_dec_key_file_button = QtWidgets.QPushButton(self)
        self.eg_dec_key_file_button.setGeometry(QtCore.QRect(80, 180, 81, 23))
        self.eg_dec_key_file_button.setObjectName("eg_dec_key_file_button")

        self.eg_dec_x_text = QtWidgets.QTextEdit(self)
        self.eg_dec_x_text.setGeometry(QtCore.QRect(80, 100, 301, 64))
        self.eg_dec_x_text.setObjectName("eg_dec_x_text")

        self.label_46 = QtWidgets.QLabel(self)
        self.label_46.setGeometry(QtCore.QRect(10, 30, 61, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy)
        self.label_46.setObjectName("label_46")

        self.eg_dec_p_text = QtWidgets.QTextEdit(self)
        self.eg_dec_p_text.setGeometry(QtCore.QRect(80, 30, 301, 64))
        self.eg_dec_p_text.setObjectName("eg_dec_p_text")

        self.label_47 = QtWidgets.QLabel(self)
        self.label_47.setGeometry(QtCore.QRect(10, 220, 61, 16))
        self.label_47.setObjectName("label_47")

        self.line_4 = QtWidgets.QFrame(self)
        self.line_4.setGeometry(QtCore.QRect(0, 210, 411, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.eg_dec_res_text = QtWidgets.QTextEdit(self)
        self.eg_dec_res_text.setGeometry(QtCore.QRect(80, 400, 301, 64))
        self.eg_dec_res_text.setObjectName("eg_dec_res_text")

        self.label_48 = QtWidgets.QLabel(self)
        self.label_48.setGeometry(QtCore.QRect(10, 400, 61, 16))
        self.label_48.setObjectName("label_48")

        self.eg_dec_key_file_name = QtWidgets.QLabel(self)
        self.eg_dec_key_file_name.setGeometry(QtCore.QRect(180, 190, 201, 20))
        self.eg_dec_key_file_name.setObjectName("eg_dec_key_file_name")

        self.eg_dec_m_file_name = QtWidgets.QLabel(self)
        self.eg_dec_m_file_name.setGeometry(QtCore.QRect(170, 320, 211, 16))
        self.eg_dec_m_file_name.setObjectName("eg_dec_m_file_name")

        self.eg_dec_save_file_name = QtWidgets.QLabel(self)
        self.eg_dec_save_file_name.setGeometry(QtCore.QRect(170, 350, 211, 16))
        self.eg_dec_save_file_name.setObjectName("eg_dec_save_file_name")
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate

        self.label_40.setText(_translate("Dialog", "Message"))
        self.eg_dec_m_file_text.setText(_translate("Dialog", "Choose file"))
        self.eg_dec_button.setText(_translate("Dialog", "Decrypt"))
        self.label_41.setText(_translate("Dialog", "Key"))
        self.label_42.setText(_translate("Dialog", "or"))
        self.label_43.setText(_translate("Dialog", "or"))
        self.label_44.setText(_translate("Dialog", "Save"))
        self.label_45.setText(_translate("Dialog", "x"))
        self.eg_dec_save_file_text.setText(_translate("Dialog", "Choose file"))
        self.eg_dec_key_file_button.setText(_translate("Dialog", "Choose file"))
        self.label_46.setText(_translate("Dialog", "p"))
        self.label_47.setText(_translate("Dialog", "Ciphertext"))
        self.label_48.setText(_translate("Dialog", "Result"))
        self.eg_dec_key_file_name.setText(_translate("Dialog", ""))
        self.eg_dec_m_file_name.setText(_translate("Dialog", ""))
        self.eg_dec_save_file_name.setText(_translate("Dialog", ""))