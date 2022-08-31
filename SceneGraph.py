from PyQt5.QtWidgets import QGraphicsScene, QGraphicsItemGroup, QLabel
from PyQt5.QtGui import QPen, QBrush, QFont
from PyQt5.Qt import Qt
from random import randint

class SceneGraph(QGraphicsScene):
    def __init__(self, graphView):
        super().__init__()
        self.graphView = graphView
        self.sceneSizeWidth = 507
        self.sceneSizeHeight = 507
        self.setSceneRect(0, 0, self.sceneSizeWidth, self.sceneSizeHeight)
        self.citiesCoordinates = []

        self.itemGroupLines = QGraphicsItemGroup()
        self.itemGroupRect = ItemGroupCity(self)

        self.addItem(self.itemGroupLines)
        self.addItem(self.itemGroupRect)

    def mousePressEvent(self, event):
        x = event.scenePos().x()
        y = event.scenePos().y()
        self.drawGraph(x, y)

    def placeRandomCity(self, n):
        for i in range(n):
            x = randint(5, 495)
            y = randint(5, 495)
            self.drawGraph(x, y)

    def drawGraph(self, x, y):
        x = x - 8
        y = y - 7
        self.itemGroupRect.addCityPoint(x, y, len(self.citiesCoordinates)+1)
        x = x + 8
        y = y + 7
        if (self.citiesCoordinates != []):
            for cityCoord in self.citiesCoordinates:
                self.itemGroupLines.addToGroup(self.addLine(x, y, cityCoord[0], cityCoord[1]))
        print(x, y)
        self.citiesCoordinates.append([x, y])

    def getCities(self):
        return self.citiesCoordinates

    def clearField(self):
        self.clear()
        self.citiesCoordinates = []

        self.itemGroupLines = QGraphicsItemGroup()
        self.itemGroupRect = ItemGroupCity(self)

        self.addItem(self.itemGroupLines)
        self.addItem(self.itemGroupRect)


class ItemGroupCity(QGraphicsItemGroup):
    def __init__(self, scene: QGraphicsScene):
        super().__init__()
        self.scene = scene
        self.pen = QPen(Qt.red)
        self.grayBrush = QBrush(Qt.gray)

    def addCityPoint(self, x, y, n):
        self.addToGroup(self.scene.addRect(x, y, 16, 14, self.pen, self.grayBrush))
        font = QFont("Times", 6, QFont.Bold)
        text = self.scene.addText(str(n))
        text.setPos(x-2, y-5)
        text.setFont(font)
        self.addToGroup(text)