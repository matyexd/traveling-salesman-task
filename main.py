from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from SceneGraph import SceneGraph
from GraphField import GraphField
from ControlPanel import ControlPanel
from ResultPanel import ResultPanel

import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.citiesMatrix = []
        self.scene = SceneGraph(self)
        self.bestRouteMain = []

        self.title = "Коммивояжер"
        self.top = 200
        self.left = 500
        self.width = 1280
        self.height = 700

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


        self.title = QLabel('Задача коммивояжера', self)
        self.title.setGeometry(470, 15, 350, 50)
        font = QFont("Times", 16, QFont.Bold)
        self.title.setFont(font)
        self.resultPanel = ResultPanel(self, self.scene)
        GraphField(self, self.scene)
        self.controlPanel = ControlPanel(self, self.scene, self.resultPanel.showBestRoute, self.resultPanel.showLengthRoute)


App = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(App.exec())
