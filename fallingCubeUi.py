try:
    from PySide2 import QtCore, QtGui, QtWidgets
    from shiboken2 import wrapInstance
except:
    from PySide2 import QtCore, QtGui, QtWidgets
    from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui 


class FallingCubeDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('AmaZing FallingCube ')
        self.resize(500,500)

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)
        self.setStyleSheet(
            '''
                QDialog {
                    background-color: #E3C4BD;
                }
            '''

        self.nameLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.addLayout(self.nameLayout)
        self.nameLabel = QtWidgets.QLabel('PLAYER NAME')
        self.nameLineEdit = QtWidgets.QLineEdit()
        self.nameLineEdit.setStyleSheet(

        self.nameLayout.addWidget(self.nameLabel)
        self.nameLayout.addWidget(self.nameLineEdit)

        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.addLayout(self.buttonLayout)
        self.selectButton = QtWidgets.QPushButton('START GAME')
        self.selectButton.setStyleSheet(

        self.cancelButton = QtWidgets.QPushButton('STOP GAME')
        self.buttonLayout.addWidget(self.selectButton)
        self.buttonLayout.addWidget(self.cancelButton)

        self.mainLayout.addStretch()



def run():
    global ui 
    try:
        ui.close()
    except:
        pass
    ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
    ui = FallingCubeDialog(parent=ptr)
    ui.show()