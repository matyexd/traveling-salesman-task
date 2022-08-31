from PyQt5.QtWidgets import QGraphicsView, QLabel, QGroupBox, QGraphicsScene
from SceneGraph import SceneGraph

class GraphField(QGroupBox):
    def __init__(self, mainWindow, scene: QGraphicsScene):
        super().__init__()
        self.scene = scene
        self.setParent(mainWindow)
        self.widgetSizeX = 600
        self.widgetSizeY = 600
        self.widgetLeft = 650
        self.widgetTop = 80

        self.sizeGraphViewWidth = 510
        self.sizeGraphViewHeight = 510
        self.sizeGraphViewLeft = 40
        self.sizeGraphViewTop = 40
        self.setGeometry(self.widgetLeft, self.widgetTop, self.widgetSizeX, self.widgetSizeY)
        self.graphicView = QGraphicsView(self.scene, self)
        self.graphicView.setGeometry(self.sizeGraphViewLeft, self.sizeGraphViewTop, self.sizeGraphViewWidth, self.sizeGraphViewHeight)

        self.initUiCoord()

    def initUiCoord(self):
        QLabel('100', self).move(self.sizeGraphViewLeft - 25, self.sizeGraphViewTop + 100)
        QLabel('200', self).move(self.sizeGraphViewLeft - 25, self.sizeGraphViewTop + 200)
        QLabel('300', self).move(self.sizeGraphViewLeft - 25, self.sizeGraphViewTop + 300)
        QLabel('400', self).move(self.sizeGraphViewLeft - 25, self.sizeGraphViewTop + 400)
        QLabel('500', self).move(self.sizeGraphViewLeft - 25, self.sizeGraphViewTop + 500)

        QLabel('0', self).move(self.sizeGraphViewLeft - 13, self.sizeGraphViewTop - 18)
        QLabel('100', self).move(self.sizeGraphViewLeft + 100, self.sizeGraphViewTop - 18)
        QLabel('200', self).move(self.sizeGraphViewLeft + 200, self.sizeGraphViewTop - 18)
        QLabel('300', self).move(self.sizeGraphViewLeft + 300, self.sizeGraphViewTop - 18)
        QLabel('400', self).move(self.sizeGraphViewLeft + 400, self.sizeGraphViewTop - 18)
        QLabel('500', self).move(self.sizeGraphViewLeft + 500, self.sizeGraphViewTop - 18)