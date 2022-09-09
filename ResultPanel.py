from PyQt5.QtWidgets import QGroupBox, QGraphicsScene, QLabel
from PyQt5.QtGui import QFont

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
        self.bestRouteLabel = QLabel(self)
        self.bestRouteLabel.setStyleSheet("QLabel {"
                             "border-style: solid;"
                             "border-width: 1px;"
                             "border-color: black; "
                             "}")
        self.bestRouteLabel.setFont(self.bestRouteFont)
        self.bestRouteLabel.setGeometry(20, 40, 560, 80)
        self.bestRouteLabel.wordWrap()
        self.bestRouteLabel.setText("Лучший маршрут:")

        self.lengthRouteLabel = QLabel(self)
        self.lengthRouteLabel.setFont(self.bestRouteFont)
        self.lengthRouteLabel.setGeometry(20, 100, 580, 80)
        self.lengthRouteLabel.setText("Длина маршрута:")

    def showBestRoute(self, bestRoute):
        text = "Лучший маршрут: " + str(bestRoute)
        self.bestRouteLabel.setText(text)

    def showLengthRoute(self, lengthRoute):
        self.lengthRoute = lengthRoute
        text = "Лучший маршрут: " + str(lengthRoute)
        self.lengthRouteLabel.setText(text)