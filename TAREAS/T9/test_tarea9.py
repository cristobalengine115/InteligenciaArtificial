import unittest
import tarea9

class MahalanobisTest(unittest.TestCase):
    def Clasificador(self):
        self.assertEquals(tarea9.main([[[1, 2], [2, 2], [3, 1], [2, 3], [3, 2]], [[8, 10], [9, 8], [9, 9], [8, 9], [7, 9]]],[1,1]),False)
        self.assertEquals(tarea9.main([[[1,2],[2,9],[3,3]],[[1,3],[5,1],[5,7]]],[2,1]),False)
        self.assertEquals(tarea9.main([[[2,0],[8,1]],[[1,1],[5,1],[5,3]]],[9,1]),True)

if __name__ == '__main__':
    unittest.main()