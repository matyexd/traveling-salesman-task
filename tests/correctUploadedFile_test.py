from unittest import TestCase, main
from utils import correctUploadedFile
from ControlPanel import ControlPanel

class CorrectUploadedFile(TestCase):
    def test_isCorrectFile(self):
        distCity1 = [
            [0, 43,56,3,6,34],
            [43,0,34,523,23, 53],
            [56,34,0,23,43,52],
            [3,523,23,0,34,3423],
            [6,23,43,34,0,23],
            [34,53,52,3423,23,0]
        ]
        self.assertEqual(correctUploadedFile.isCorrectUploadedFile(distCity1), True)

    def test_isCorrectFileString(self):
        distCity2 = [[0, 43,56,3,6,34],
                    [43,0,34,523,23, 53],
                    [56,34,0,23,43,52],
                    [3,523,23,0,34,3423],
                    [6,23,43,34,0,23],
                    [34,53,52,3423,'dfd',0]]
        self.assertEqual(correctUploadedFile.isCorrectUploadedFile(distCity2), False)
    def test_isCorrectFileZero(self):
        distCity3 = [[1, 43, 56, 3, 6, 34],
                    [43, 0, 34, 523, 23, 53],
                    [56, 34, 0, 23, 43, 52],
                    [3, 523, 23, 0, 34, 3423],
                    [6, 23, 43,  34, 0, 23],
                    [34, 53, 52, 3423, 23, 0]]
        self.assertEqual(correctUploadedFile.isCorrectUploadedFile(distCity3), False)

    def test_isCorrectFileZero(self):
        distCity3 = [[1, 43, 56, 3, 6, 34],
                    [43, 0, 34, 523, 23, 53],
                    [56, 34, 0, 23, 43, 52],
                    [3, 523, 23, 0, 34, 3423],
                    [6, 23, 43,  34, 0, 23],
                    [34, 53, 52, 3423, 23, 0]]
        self.assertEqual(correctUploadedFile.isCorrectUploadedFile(distCity3), False)

    def test_underAndAboveDiagonalEqualValuesForMatrix(self):
        distCity4 = [[1, 43, 56, 3, 6, 34],
                    [43, 0, 34, 523, 23, 53],
                    [56, 34, 0, 23, 43, 52],
                    [30, 523, 23, 0, 34, 3423],
                    [6, 23, 43,  34, 0, 23],
                    [34, 53, 52, 3423, 23, 0]]
        self.assertEqual(correctUploadedFile.isCorrectUploadedFile(distCity4), False)

if __name__ == '__main__':
    main()