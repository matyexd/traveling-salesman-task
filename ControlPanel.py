from PyQt5.QtWidgets import QGroupBox, QGraphicsScene, QPushButton, QLineEdit, QLabel, QFileDialog, QRadioButton, QGridLayout, QCheckBox, QMessageBox
from PyQt5.QtCore import QUrl
from algTravelSal import startGenAlg
import json
from utils import correctUploadedFile

class ControlPanel(QGroupBox):
    def __init__(self, mainWindow, scene: QGraphicsScene, showBestRoute, showLengthRoute):
        super().__init__()
        self.layout = QGridLayout()

        self.showBestRoute = showBestRoute
        self.showLengthRoute = showLengthRoute

        self.setLayout(self.layout)
        self.cityFromFile = []
        self.scene = scene
        self.setParent(mainWindow)
        self.widgetSizeX = 580
        self.widgetSizeY = 400
        self.widgetLeft = 30
        self.widgetTop = 80
        self.setGeometry(self.widgetLeft, self.widgetTop, self.widgetSizeX, self.widgetSizeY)
        self.bestRoute = []

        self.addError()
        self.addUI()

    def addUI(self):
        # Radio button
        self.radiobuttonManual = QRadioButton("Ручной режим")
        self.radiobuttonManual.setChecked(True)
        self.radiobuttonManual.toggled.connect(self.onClickedManualRadioButton)
        self.layout.addWidget(self.radiobuttonManual, 0, 0)

        # Label "кол-во городов"
        labelCountCity = QLabel('Кол-во городов', self)
        self.layout.addWidget(labelCountCity, 1, 0)


        # lineEdit "кол-во" городов
        self.lineEditCityCount = QLineEdit(self)
        self.layout.addWidget(self.lineEditCityCount, 1, 1)

        # Кнопка "Расставить точки случайным образом"
        self.buttonPlaceRandomCity = QPushButton('Расставить точки случайным образом', self)
        self.buttonPlaceRandomCity.clicked.connect(self.onClickPlaceRandomCity)
        self.layout.addWidget(self.buttonPlaceRandomCity, 2, 0)

        # Radio button
        self.radiobuttonUploadFile = QRadioButton("Загрузить матрицу из файла (без графа)")
        self.radiobuttonUploadFile.toggled.connect(self.onClickedUploadFileRadioButton)
        self.layout.addWidget(self.radiobuttonUploadFile, 3, 0)

        # label "Выбранный файл"
        self.labelSelectedFile = QLabel('Выбранный файл:')
        self.layout.addWidget(self.labelSelectedFile, 4, 1)

        # Кнопка "Загрузить матрицу"
        self.buttonUploadMatrixCity = QPushButton('Загрузить матрицу')
        self.buttonUploadMatrixCity.clicked.connect(self.onUploadMatrixCity)
        self.layout.addWidget(self.buttonUploadMatrixCity, 4, 0)
        self.buttonUploadMatrixCity.setDisabled(True)

        # Checkbox
        self.checkbox = QCheckBox('Использовать свои настройки')
        self.checkbox.clicked.connect(self.onClickCheckbox)
        self.layout.addWidget(self.checkbox, 5, 0)

        # размер популяции
        self.labelPopCount = QLabel('Размер популяции:')
        self.layout.addWidget(self.labelPopCount, 6, 0)
        self.lineEditPopCount = QLineEdit(self)
        self.lineEditPopCount.setText('300')
        self.layout.addWidget(self.lineEditPopCount, 6, 1)
        self.lineEditPopCount.setDisabled(True)

        # Количество поколений
        self.labelGenCount = QLabel('Количество поколений:')
        self.layout.addWidget(self.labelGenCount, 7, 0)
        self.lineEditGenCount = QLineEdit(self)
        self.lineEditGenCount.setText('100')
        self.layout.addWidget(self.lineEditGenCount, 7, 1)
        self.lineEditGenCount.setDisabled(True)

        # Вероятность скрещивания
        self.labelCxpb = QLabel('Вероятность скрещивания:')
        self.layout.addWidget(self.labelCxpb, 8, 0)
        self.lineEditCxpb = QLineEdit(self)
        self.lineEditCxpb.setText('0.7')
        self.layout.addWidget(self.lineEditCxpb, 8, 1)
        self.lineEditCxpb.setDisabled(True)

        # Вероятность мутации
        self.labelMutpb = QLabel('Вероятность мутации:')
        self.layout.addWidget(self.labelMutpb, 9, 0)
        self.lineEditMutpb = QLineEdit(self)
        self.lineEditMutpb.setText('0.2')
        self.layout.addWidget(self.lineEditMutpb, 9, 1)
        self.lineEditMutpb.setDisabled(True)

        # Кнопка "Очистить поле"
        buttonClearField = QPushButton('Очистить поле', self)
        buttonClearField.clicked.connect(self.onClearField)
        self.layout.addWidget(buttonClearField, 10, 0)

        # Кнопка "Запуск"
        buttonStart = QPushButton('Запуск', self)
        buttonStart.clicked.connect(self.onClickStart)
        self.layout.addWidget(buttonStart, 11, 0)

    def printHelloWorld(self):
        return 'hello world'

    def addError(self):
        #
        self.errorStart = QMessageBox()
        self.errorStart.setText("В графе должно быть не менее 2 объектов!")
        self.errorStart.setWindowTitle("Error")

        #
        self.errorRandomPointInvalid = QMessageBox()
        self.errorRandomPointInvalid.setText("Невалидные данные! Количество городов должно быть целым неотрицательным числом")
        self.errorRandomPointInvalid.setWindowTitle("Error")

        self.errorRandomPointCount = QMessageBox()
        self.errorRandomPointCount.setText("Число городов на графе должно быть меньше 100!")
        self.errorRandomPointCount.setWindowTitle("Error")

        #
        self.errorClearField = QMessageBox()
        self.errorClearField.setText("Очистите поле!")
        self.errorClearField.setWindowTitle("Error")

        #
        self.errorUploadFile = QMessageBox()
        self.errorUploadFile.setText("Некорректный входные данные")
        self.errorUploadFile.setWindowTitle("Error")

        #
        self.errorChooseFile = QMessageBox()
        self.errorChooseFile.setText("Выберите файл!")
        self.errorChooseFile.setWindowTitle("Error")

        #
        self.errorPopulation = QMessageBox()
        self.errorPopulation.setText("Невалидные данные! Размер популяции должен быть целым положительным числом")
        self.errorPopulation.setWindowTitle("Error")

        #
        self.errorNgen = QMessageBox()
        self.errorNgen.setText("Невалидные данные! Количество поколений должно быть целым положительным числом")
        self.errorNgen.setWindowTitle("Error")

        #
        self.errorCxpb = QMessageBox()
        self.errorCxpb.setText("Невалидные данные! Вероятность скрещивания должна быть от 0 до 1")
        self.errorCxpb.setWindowTitle("Error")

        #
        self.errorMut = QMessageBox()
        self.errorMut.setText("Невалидные данные! Вероятность мутации должна быть от 0 до 1")
        self.errorMut.setWindowTitle("Error")

    def onClickStart(self):

        if (self.scene.getIsGetResult()):
            self.errorClearField.exec_()
            return

        self.citiesMatrix = []
        if self.radiobuttonUploadFile.isChecked():
            if (len(self.cityFromFile) < 2):
                self.errorChooseFile.exec_()
                return
            if (self.checkbox.isChecked()):
                if (self.getDataFromSettings()):
                    npop, ngen, cxpb, mutpb = self.getDataFromSettings()
                    best_ind, best_fitness = startGenAlg(self.citiesMatrix, len(self.citiesMatrix), npop, ngen, cxpb, mutpb)
                else:
                    return
            else:
                best_ind, best_fitness = startGenAlg(self.citiesMatrix, len(self.citiesMatrix))
            self.bestRoute = best_ind
        elif self.radiobuttonManual:
            citiesCoordinates = self.scene.getCities()
            if (len(citiesCoordinates) <= 1):
                self.errorStart.exec_()
                return
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
            if (self.checkbox.isChecked()):
                if (self.getDataFromSettings()):
                    npop, ngen, cxpb, mutpb = self.getDataFromSettings()
                    best_ind, best_fitness = startGenAlg(self.citiesMatrix, len(self.citiesMatrix),npop, ngen, cxpb, mutpb)
                else:
                    return
            else:
                best_ind, best_fitness = startGenAlg(self.citiesMatrix, len(self.citiesMatrix))
            self.scene.drawBestRoute(best_ind)
            self.bestRoute = best_ind
        self.showBestRoute(self.bestRoute)
        self.getLenght()
        self.showLengthRoute(self.lengthRoute)

    def getLenght(self):
        self.lengthRoute = 0
        if self.radiobuttonManual.isChecked():
            for i in range(len(self.bestRoute)):
                if i == 0:
                    continue
                self.lengthRoute += self.citiesMatrix[self.bestRoute[i-1]][self.bestRoute[i]]
        else:
            for i in range(len(self.bestRoute)):
                if i == 0:
                    continue
                self.lengthRoute += self.cityFromFile[self.bestRoute[i-1]][self.bestRoute[i]]

    def getDataFromSettings(self):
        try:
            npop = int(self.lineEditPopCount.text())
            if (npop < 1):
                raise Exception()
        except:
            self.errorPopulation.exec_()
            return False

        try:
            ngen = int(self.lineEditGenCount.text())
            if (ngen < 1):
                raise Exception()
        except:
            self.errorNgen.exec_()
            return False

        try:
            cxpb = float(self.lineEditCxpb.text().replace(",", "."))
            if (cxpb > 1 or cxpb < 0):
                raise Exception()
        except:
            self.errorCxpb.exec_()
            return False

        try:
            mutpb = float(self.lineEditMutpb.text().replace(",", "."))
            if (mutpb > 1 or mutpb < 0):
                raise Exception()
        except:
            self.errorMut.exec_()
            return False

        return npop, ngen, cxpb, mutpb

    def onClickPlaceRandomCity(self):
        print('onClickPlaceRandomCity')
        try:
            n = int(self.lineEditCityCount.text())
            citiesCoordinates = self.scene.getCities()
            if (n + len(citiesCoordinates) > 99):
                self.errorRandomPointCount.exec_()
                return
            if (self.scene.getIsGetResult()):
                self.errorClearField.exec_()
                return
            if (n <= 0):
                raise Exception()
            self.scene.placeRandomCity(n)
        except:
            self.errorRandomPointInvalid.exec_()

    def onUploadMatrixCity(self):
        print('onUploadMatrixCity')
        try:
            fname, _ = QFileDialog.getOpenFileName(self, "Open file", "", "json (*.json)")
            if not fname:
                return
            url = QUrl.fromLocalFile(fname)
            with open(fname) as f:
                templates = json.load(f)
            if (correctUploadedFile.isCorrectUploadedFile(templates["DistanceMatrix"]) != True):
                raise Exception()
            self.cityFromFile = templates["DistanceMatrix"]
            text = self.labelSelectedFile.text() + ' ' + url.fileName()
            self.labelSelectedFile.setText(text)
        except:
            self.errorUploadFile.exec_()
    def onClearField(self):
        self.scene.clearField()
        self.cityFromFile = []
        self.labelSelectedFile.setText("Выбранный файл: ")
        print('onClearField')

    def onClickedManualRadioButton(self):
        state = self.radiobuttonManual.isChecked()
        print("onClickedManualRadioButton", state)
        if (state):
            self.lineEditCityCount.setDisabled(False)
            self.buttonPlaceRandomCity.setDisabled(False)
        else:
            self.lineEditCityCount.setDisabled(True)
            self.buttonPlaceRandomCity.setDisabled(True)

    def onClickedUploadFileRadioButton(self):
        state = self.radiobuttonUploadFile.isChecked()
        print("onClickedUploadFileRadioButton", state)
        if (state):
            self.buttonUploadMatrixCity.setDisabled(False)
        else:
            self.buttonUploadMatrixCity.setDisabled(True)

    def onClickCheckbox(self):
        state = self.checkbox.isChecked()
        print("onClickCheckbox", state)
        if (state):
            self.lineEditPopCount.setDisabled(False)
            self.lineEditGenCount.setDisabled(False)
            self.lineEditCxpb.setDisabled(False)
            self.lineEditMutpb.setDisabled(False)
        else:
            self.lineEditPopCount.setDisabled(True)
            self.lineEditGenCount.setDisabled(True)
            self.lineEditCxpb.setDisabled(True)
            self.lineEditMutpb.setDisabled(True)

    def getBestRoute(self):
        return self.bestRoute


