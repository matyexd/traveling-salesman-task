from unittest import TestCase, main
from algTravelSal import cx

class CxTest(TestCase):
    def test_cxUnic(self):
        status = False
        parent1 = [5,2,4,1,3,6]
        parent2 = [4,2,5,1,3,6]
        child1, child2 = cx(parent1, parent2)
        setarr1 = set(child1)
        setarr2 = set(child2)
        # проверка на уникальность значений в массиве
        if len(child1) == len(setarr1) and len(child2) == len(setarr2) and len(child2) == len(child1):
            if (child1 != parent2, parent1) and (child2 != parent2, parent1):
                status = True
        self.assertTrue(status)

    def test_cxDifferentSizeParents(self):
        parent1 = [5,2,4,1,3,6]
        parent2 = [4,2,5,1,3]
        with self.assertRaises(ValueError) as e:
            cx(parent1, parent2)
        self.assertEqual("Не идентичные по размеру родители", e.exception.args[0])
