import sys
from unittest import TestCase, main

from PyQt5.QtWidgets import QApplication
from main import Window


app = QApplication(sys.argv)

class TravelingSalesmanTask(TestCase):
    def setUp(self):
        self.window = Window()

    def test_One(self):
        self.assertEqual(self.window.controlPanel.printHelloWorld(), 'hello world')
        self.window.printHelloWorld()
        self.window.controlPanel.lineEditMutpb.setText('Сука')

if __name__ == '__main__':
    print('хелоу')
    main()