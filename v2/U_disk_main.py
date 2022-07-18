from numpy import double
import U_disk_convert
from U_disk_UI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class fun_main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(fun_main, self).__init__(parent)
        self.setupUi(self)

        # setup button connect
        self.pushButton.clicked.connect(self.convert)

    def convert(self):
        if len(self.textEdit_GBinput.toPlainText()) == 0:
            self.textEdit_GBinput_2.setText('0')
        else:
            GB_in = self.textEdit_GBinput.toPlainText()
            temp1 = U_disk_convert.B2G(U_disk_convert.G2B(double(GB_in)))
            s1 = str(round(temp1*0.93, 4))+'~'+str(round(temp1, 4))
            self.textEdit_GBinput_2.setText(str(s1))
        if len(self.textEdit_TBinput.toPlainText()) == 0:
            self.textEdit_TBinput_2.setText('0')
        else:
            TB_in = self.textEdit_TBinput.toPlainText()
            temp2 = U_disk_convert.B2T(U_disk_convert.T2B(double(TB_in)))
            s2 = str(round(temp2*0.93, 4))+'~'+str(round(temp2, 4))
            self.textEdit_TBinput_2.setText(str(s2))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = fun_main()
    ui.show()
    sys.exit(app.exec_())
