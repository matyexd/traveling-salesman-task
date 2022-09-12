from PyQt5.QtWidgets import QGroupBox, QGraphicsScene, QLabel, QStyleOption, QStyle
from PyQt5.QtGui import QFont, QPainter
from PyQt5.QtCore import Qt

class SuperQLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super(SuperQLabel, self).__init__(*args, **kwargs)

        self.textalignment = Qt.AlignLeft | Qt.TextWrapAnywhere
        self.isTextLabel = True
        self.align = None

    def paintEvent(self, event):

        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)

        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)

        self.style().drawItemText(painter, self.rect(),
                                  self.textalignment, self.palette(), True, self.text())

class ResultPanel(QGroupBox):
    def __init__(self, mainWindow, scene: QGraphicsScene):
        super().__init__()
        self.scene = scene
        self.setParent(mainWindow)
        self.widgetSizeX = 580
        self.widgetSizeY = 180
        self.widgetLeft = 30
        self.widgetTop = 500
        self.setGeometry(self.widgetLeft, self.widgetTop, self.widgetSizeX, self.widgetSizeY)
        self.resultsFont = QFont("Times", 10, QFont.Bold)
        self.bestRouteFont = QFont("Times", 8, QFont.Bold)
        self.addUI()

    def addUI(self):
        # результаты
        results = QLabel(self)
        results.move(20, 10)
        results.setText("Результаты")
        results.setFont(self.resultsFont)

        # лучший маршрут
        self.bestRouteLabel = SuperQLabel(self)
        self.bestRouteLabel.setFont(self.bestRouteFont)
        self.bestRouteLabel.setGeometry(20, 40, 500, 80)
        self.bestRouteLabel.wordWrap()
        self.bestRouteLabel.setText("Лучший маршрут:")

        self.lengthRouteLabel = QLabel(self)
        self.lengthRouteLabel.setFont(self.bestRouteFont)
        self.lengthRouteLabel.setGeometry(20, 100, 580, 80)
        self.lengthRouteLabel.setText("Длина маршрута:")

    def showBestRoute(self, bestRoute):
        bestRouteString = ''
        for i in range(len(bestRoute)):
            bestRouteString = bestRouteString + str(bestRoute[i]+1)+' '
        text = "Лучший маршрут: " + bestRouteString
        self.bestRouteLabel.setText(text)

    def showLengthRoute(self, lengthRoute):
        self.lengthRoute = round(lengthRoute, 2)
        text = "Длина маршрута: " + str(self.lengthRoute)
        self.lengthRouteLabel.setText(text)