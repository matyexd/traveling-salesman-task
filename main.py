from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem, QGraphicsSceneMouseEvent, QPushButton, QWidget
from PyQt5.QtGui import QPen, QBrush, QPainter, QColor
from PyQt5.Qt import Qt
from PyQt5.QtCore import QRectF

import sys

class GraphField(QWidget):
    def __init__(self):
        super().__init__()

class MyScene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.sceneSizeWidth = 607
        self.sceneSizeHeight = 607
        self.setSceneRect(0, 0, self.sceneSizeWidth, self.sceneSizeHeight)
        self.pen = QPen(Qt.red)
        self.greenBrush = QBrush(Qt.green)
        self.grayBrush = QBrush(Qt.gray)
        self.citiesCoordinates = []
        self.cities = []
    def mousePressEvent(self, event):
        x = event.scenePos().x() - 5
        y = event.scenePos().y() - 5
        self.addRect(x, y, 10, 10, self.pen, self.grayBrush)
        x = x + 5
        y = y + 5
        if (self.citiesCoordinates != []):
            for cityCoord in self.citiesCoordinates:
                self.addLine(x, y, cityCoord[0], cityCoord[1])
                print(((x-cityCoord[0])**2+(y-cityCoord[1])**2) ** 0.5)
                self.cities.append([])
        self.citiesCoordinates.append([x, y])

    def getCities(self):
        return self.citiesCoordinates

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.citiesMatrix = []

        self.title = "PyQt5 QGraphicView"
        self.top = 200
        self.left = 500
        self.width = 1280
        self.height = 670

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createGraphicView()
        button = QPushButton('Сохранить', self)
        button.setToolTip('This is an example button')
        button.move(100, 10)
        button.clicked.connect(self.on_click)
        self.show()

    def on_click(self):
        self.citiesMatrix = []
        print('PyQt5 button click')
        citiesCoordinates = self.scene.getCities()
        for i in range(len(citiesCoordinates)):
            arr = []
            x1 = citiesCoordinates[i][0]
            y1 = citiesCoordinates[i][1]
            for j in range(len(citiesCoordinates)):
                x2 = citiesCoordinates[j][0]
                y2 = citiesCoordinates[j][1]
                if (i == j):
                    arr.append(0)
                else:
                    dist = ((x1-x2)**2+(y1-y2)**2) ** 0.5
                    arr.append(round(dist, 3))

            self.citiesMatrix.append(arr)
        print(self.citiesMatrix)

    def createGraphicView(self):
        self.pen = QPen(Qt.red)
        self.scene = MyScene()
        self.greenBrush = QBrush(Qt.green)
        self.grayBrush = QBrush(Qt.gray)
        sizeGraphViewWidth = 610
        sizeGraphViewHeight = 610

        graphicView = QGraphicsView(self.scene, self)
        graphicView.setGeometry(640, 30, sizeGraphViewWidth, sizeGraphViewHeight)





App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())