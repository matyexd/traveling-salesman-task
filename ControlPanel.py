from PyQt5.QtWidgets import QGroupBox, QGraphicsScene, QPushButton, QLineEdit, QLabel, QFileDialog, QRadioButton
from PyQt5.QtCore import QUrl
from algTravelSal import GeneticsAlg
import json

class ControlPanel(QGroupBox):
    def __init__(self, mainWindow, scene: QGraphicsScene):
        super().__init__()
        self.cityFromFile = []
        self.scene = scene
        self.setParent(mainWindow)
        self.widgetSizeX = 580
        self.widgetSizeY = 300
        self.widgetLeft = 30
        self.widgetTop = 80
        self.setGeometry(self.widgetLeft, self.widgetTop, self.widgetSizeX, self.widgetSizeY)
        self.addUI()

    def addUI(self):
        # Кнопка "Запуск"
        buttonStart = QPushButton('Запуск', self)
        buttonStart.setGeometry(0, 0, 200, 90)
        buttonStart.move(320, 150)
        buttonStart.clicked.connect(self.onClickStart)

        # Кнопка "Расставить точки случайным образом"
        buttonPlaceRandomCity = QPushButton('Расставить точки случайным образом', self)
        buttonPlaceRandomCity.setGeometry(0, 0, 240, 40)
        buttonPlaceRandomCity.move(50, 50)
        buttonPlaceRandomCity.clicked.connect(self.onClickPlaceRandomCity)

        # lineEdit "кол-во" городов
        self.lineEditCityCount = QLineEdit(self)
        self.lineEditCityCount.setGeometry(0, 0, 100, 40)
        self.lineEditCityCount.move(420, 50)

        # Label "кол-во городов"
        labelCountCity = QLabel('Кол-во городов', self)
        labelCountCity.move(320, 60)

        # Кнопка "Загрузить матрицу"
        buttonUploadMatrixCity = QPushButton('Загрузить матрицу (без графа)', self)
        buttonUploadMatrixCity.setGeometry(0, 0, 240, 40)
        buttonUploadMatrixCity.move(50, 100)
        buttonUploadMatrixCity.clicked.connect(self.onUploadMatrixCity)

        # label "Выбранный файл"
        self.labelSelectedFile = QLabel('Выбранный файл:', self)
        self.labelSelectedFile.setGeometry(55, 140, 240, 50)
        self.labelSelectedFile.wordWrap()

        # Кнопка "Очистить поле"
        buttonClearField = QPushButton('Очистить поле', self)
        buttonClearField.setGeometry(0, 0, 240, 40)
        buttonClearField.move(50, 200)
        buttonClearField.clicked.connect(self.onClearField)



    def onClickStart(self):
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
                    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                    arr.append(round(dist, 3))

            self.citiesMatrix.append(arr)
        print(self.citiesMatrix)
        alg = GeneticsAlg(len(self.citiesMatrix), self.citiesMatrix)
        best_ind = alg.start()
        self.scene.drawBestRoute(best_ind)
        print(best_ind)

    def onClickPlaceRandomCity(self):
        print('onClickPlaceRandomCity')
        n = int(self.lineEditCityCount.text())
        self.scene.placeRandomCity(n)

    def onUploadMatrixCity(self):
        print('onUploadMatrixCity')
        fname, _ = QFileDialog.getOpenFileName(self, "Open file", "", "json (*.json)")
        url = QUrl.fromLocalFile(fname)
        text = self.labelSelectedFile.text() + ' ' + url.fileName()
        self.labelSelectedFile.setText(text)
        with open(fname) as f:
            templates = json.load(f)
        self.cityFromFile = templates["DistanceMatrix"]
    def onClearField(self):
        self.scene.clearField()
        self.cityFromFile = []
        self.labelSelectedFile.setText("Выбранный файл: ")
        print('onClearField')

    def onClickedManualRadioButton(self):
        print('click')

