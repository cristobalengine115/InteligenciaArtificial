import unittest
import tarea7

class TestCodificarPalabra(unittest.TestCase):
    def test_dijkstra(self):
        mi_grafo = tarea7.Grafo('A')
        mi_grafo.createGrafo('A,B7,C9;B,A7,D8;D,B8,C6,E5,F12;F,D12,E17;E,C2,D5,F17;C,A9,D6,E2')
        # print("===INFORMACIÓN GRAFO CREADO PARA DIJKSTRA===")
        # mi_grafo.impriGrafo()
        self.assertEqual(mi_grafo.dijkstra('F'),['A', 'B', 'D', 'F'])
        self.assertEqual(mi_grafo.dijkstra('D'),['A', 'B', 'D'])
        self.assertEqual(mi_grafo.dijkstra('E'),['A', 'C', 'E'])
        print('GRAFO 1 CORRECTO')
        

        mi_grafo2 = tarea7.Grafo('A')
        mi_grafo2.createGrafo('A,B3,C1;B,A3,D1,G5;C,A1,D2,F5;D,B1,C2,F2,E4;E,D4,G2,H1;F,C5,D2,H3;G,B5,E2;H,1E,3F')
        # print("===INFORMACIÓN GRAFO CREADO PARA DIJKSTRA===")
        # mi_grafo.impriGrafo()
        self.assertEqual(mi_grafo2.dijkstra('H'),['A', 'C', 'D', 'F', 'H'])
        self.assertEqual(mi_grafo2.dijkstra('D'),['A', 'C', 'D'])
        self.assertEqual(mi_grafo2.dijkstra('E'),['A', 'C', 'D','E'])
        print('GRAFO 2 CORRECTO')

        
    # def test_decodificar(self):
    #     self.assertEqual(tarea5.float_to_binary(54.125),'01000010010110001000000000000000')
    #     self.assertEqual(tarea5.float_to_binary(33.140625),'01000010000001001001000000000000')
    #     self.assertEqual(tarea5.float_to_binary(101.5625),'01000010110010110010000000000000')
    #     self.assertEqual(tarea5.float_to_binary(10256.283203125),'01000110001000000100000100100010')
    #     self.assertEqual(tarea5.float_to_binary(77.15625),'01000010100110100101000000000000')


if __name__ == '__main__':
    unittest.main()
