from PyQt5.QtWidgets import QGroupBox, QGraphicsScene

class ResultPanel(QGroupBox):
    def __init__(self, mainWindow, scene: QGraphicsScene):
        super().__init__()
        self.scene = scene
        self.setParent(mainWindow)
        self.widgetSizeX = 580
        self.widgetSizeY = 280
        self.widgetLeft = 30
        self.widgetTop = 400
        self.setGeometry(self.widgetLeft, self.widgetTop, self.widgetSizeX, self.widgetSizeY)