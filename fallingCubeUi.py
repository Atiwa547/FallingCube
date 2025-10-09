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

        self.setWindowTitle('AmaZing FallingCube')
        self.resize(500, 500)

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.setStyleSheet("""
            QDialog {
                background-color: #F9E1D9;
            }
            QLabel {
                color: #4A1A14;
                font-size: 14px;
                font-weight: bold;
            }
            QLineEdit {
                border: 2px solid #E36346;
                border-radius: 4px;
                padding: 4px;
                background-color: #FFF5F3;
                font-size: 13px;
            }
            QPushButton {
                background-color: #E36346;
                color: white;
                border-radius: 6px;
                padding: 8px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #FF7255;
            }
            QSlider::groove:horizontal {
                background: #E3C4BD;
                height: 6px;
                border-radius: 3px;
            }
            QSlider::handle:horizontal {
                background: #E36346;
                width: 16px;
                border-radius: 8px;
                margin: -5px 0;
            }
        """)

        bestLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.addLayout(bestLayout)
        bestLabel = QtWidgets.QLabel("BEST SCORE")
        self.bestScoreLine = QtWidgets.QLineEdit("0")
        self.bestScoreLine.setReadOnly(True)
        bestLayout.addWidget(bestLabel)
        bestLayout.addWidget(self.bestScoreLine)

        nameLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.addLayout(nameLayout)
        nameLabel = QtWidgets.QLabel('PLAYER NAME')
        self.nameLineEdit = QtWidgets.QLineEdit()
        nameLayout.addWidget(nameLabel)
        nameLayout.addWidget(self.nameLineEdit)

        spawnLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.addLayout(spawnLayout)
        spawnLabel = QtWidgets.QLabel('CUBE COUNT')
        self.spawnSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.spawnSlider.setMinimum(1)
        self.spawnSlider.setMaximum(50)
        self.spawnSlider.setValue(10)
        self.spawnValue = QtWidgets.QLabel(str(self.spawnSlider.value()))
        spawnLayout.addWidget(spawnLabel)
        spawnLayout.addWidget(self.spawnSlider)
        spawnLayout.addWidget(self.spawnValue)
        self.spawnSlider.valueChanged.connect(lambda v: self.spawnValue.setText(str(v)))

        speedLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.addLayout(speedLayout)
        speedLabel = QtWidgets.QLabel('CUBE SPEED')
        self.speedSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.speedSlider.setMinimum(1)
        self.speedSlider.setMaximum(20)
        self.speedSlider.setValue(5)
        self.speedValue = QtWidgets.QLabel(str(self.speedSlider.value()))
        speedLayout.addWidget(speedLabel)
        speedLayout.addWidget(self.speedSlider)
        speedLayout.addWidget(self.speedValue)
        self.speedSlider.valueChanged.connect(lambda v: self.speedValue.setText(str(v)))

        buttonLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.addLayout(buttonLayout)
        self.startButton = QtWidgets.QPushButton('START GAME')
        self.stopButton = QtWidgets.QPushButton('STOP GAME')
        buttonLayout.addWidget(self.startButton)
        buttonLayout.addWidget(self.stopButton)

        self.mainLayout.addStretch()

        self.startButton.clicked.connect(self.startGame)
        self.stopButton.clicked.connect(self.stopGame)

    def startGame(self):
        player = self.nameLineEdit.text() or "Player"
        cubes = self.spawnSlider.value()
        speed = self.speedSlider.value()
        QtWidgets.QMessageBox.information(
            self, "Game Start",
            f"Welcome, {player}!\n\nCubes: {cubes}\nSpeed: {speed}"
        )

    def stopGame(self):
        QtWidgets.QMessageBox.warning(
            self, "Game Over",
            "You stopped the game!"
        )


def run():
    global ui
    try:
        ui.close()
    except:
        pass
    ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
    ui = FallingCubeDialog(parent=ptr)
    ui.show()
