from unittest import TestCase, main
from algTravelSal import mut

class MutTest(TestCase):
    def test_mut(self):
        status = False
        child1 = [1,2,3,4,5,6,7,8,9]
        mutant = mut(child1)
        k = 0
        for i in range(len(mutant)):
            if (child1[i] != mutant[i]):
                k += 1
        if k == 2: status = True
        self.assertTrue(status)


