from PyQt5.QtWidgets import QGraphicsScene, QGraphicsItemGroup, QMessageBox
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
        self.isGetResult = False
        self.bestRoute = []

        self.linePen = QPen(Qt.gray, 1) # обычные линии графа
        self.lineBestRoadPen = QPen(Qt.blue, 3)
        self.circlePen = QPen(Qt.red, 3) # линии лучшего маршрута графа

        self.itemGroupLines = QGraphicsItemGroup()
        self.itemGroupLinesBestRoad = QGraphicsItemGroup()
        self.itemGroupRect = ItemGroupCity(self)
        self.itemGroupCircle = QGraphicsItemGroup()

        self.addItem(self.itemGroupLines)
        self.addItem(self.itemGroupLinesBestRoad)
        self.addItem(self.itemGroupRect)
        self.addItem(self.itemGroupCircle)

        #
        self.errorPointCount = QMessageBox()
        self.errorPointCount.setText("Число городов на графе должно быть меньше 100!")
        self.errorPointCount.setWindowTitle("Error")

    def mousePressEvent(self, event):
        if (self.isGetResult):
            return
        if (len(self.citiesCoordinates) > 98):
            self.errorPointCount.exec_()
            return
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
        if (self.citiesCoordinates == []):
            self.itemGroupCircle.addToGroup(self.addEllipse(x-14, y-14, 30, 30, self.circlePen))
        if (self.citiesCoordinates != []):
            for cityCoord in self.citiesCoordinates:
                self.itemGroupLines.addToGroup(self.addLine(x, y, cityCoord[0], cityCoord[1], self.linePen))
        self.citiesCoordinates.append([x, y])

    def getCities(self):
        return self.citiesCoordinates

    def getIsGetResult(self):
        return self.isGetResult

    def clearField(self):
        self.clear()
        self.citiesCoordinates = []
        self.isGetResult = False

        self.itemGroupLines = QGraphicsItemGroup()
        self.itemGroupLinesBestRoad = QGraphicsItemGroup()
        self.itemGroupRect = ItemGroupCity(self)
        self.itemGroupCircle = QGraphicsItemGroup()

        self.addItem(self.itemGroupLines)
        self.addItem(self.itemGroupLinesBestRoad)
        self.addItem(self.itemGroupRect)
        self.addItem(self.itemGroupCircle)

    def drawBestRoute(self, bestRoute):
        self.isGetResult = True
        for i in range(len(bestRoute)):
            if bestRoute[i] == 0:
                continue
            currentPoint = bestRoute[i]
            prevPoint = bestRoute[i-1]
            x1 = self.citiesCoordinates[prevPoint][0]
            y1 = self.citiesCoordinates[prevPoint][1]
            x2 = self.citiesCoordinates[currentPoint][0]
            y2 = self.citiesCoordinates[currentPoint][1]
            self.itemGroupLinesBestRoad.addToGroup(self.addLine(x1, y1, x2, y2, self.lineBestRoadPen))

        x1 = self.citiesCoordinates[bestRoute[0]][0]
        y1 = self.citiesCoordinates[bestRoute[0]][1]
        x2 = self.citiesCoordinates[bestRoute[-1]][0]
        y2 = self.citiesCoordinates[bestRoute[-1]][1]
        self.itemGroupLinesBestRoad.addToGroup(self.addLine(x1, y1, x2, y2, self.lineBestRoadPen))



class ItemGroupCity(QGraphicsItemGroup):
    def __init__(self, scene: QGraphicsScene):
        super().__init__()
        self.scene = scene
        self.pen = QPen(Qt.red)
        self.grayBrush = QBrush(Qt.gray)
        self.yellowBrush = QBrush(Qt.yellow)

    def addCityPoint(self, x, y, n):
        self.addToGroup(self.scene.addRect(x, y, 16, 14, self.pen, self.yellowBrush))
        font = QFont("Times", 6, QFont.Bold)
        text = self.scene.addText(str(n))
        text.setPos(x-2, y-5)
        text.setFont(font)
        self.addToGroup(text)