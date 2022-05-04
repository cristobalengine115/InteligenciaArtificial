import unittest
import tarea7

class TestCodificarPalabra(unittest.TestCase):
    def test_dijkstra(self):
        mi_grafo = tarea7.Grafo('A')
        mi_grafo.createGrafo('A,B7,C9;B,A7,D8;D,B8,C6,E5,F12;F,D12,E17;E,C2,D5,F17;C,A9,D6,E2')
        self.assertEqual(mi_grafo.dijkstra('F'),['A', 'B', 'D', 'F'])
        self.assertEqual(mi_grafo.dijkstra('D'),['A', 'B', 'D'])
        self.assertEqual(mi_grafo.dijkstra('E'),['A', 'C', 'E'])
        print('GRAFO 1 CORRECTO')
        

        mi_grafo2 = tarea7.Grafo('A')
        mi_grafo2.createGrafo('A,B3,C1;B,A3,D1,G5;C,A1,D2,F5;D,B1,C2,F2,E4;E,D4,G2,H1;F,C5,D2,H3;G,B5,E2;H,1E,3F')
        self.assertEqual(mi_grafo2.dijkstra('H'),['A', 'C', 'D', 'F', 'H'])
        self.assertEqual(mi_grafo2.dijkstra('D'),['A', 'C', 'D'])
        self.assertEqual(mi_grafo2.dijkstra('E'),['A', 'C', 'D','E'])
        print('GRAFO 2 CORRECTO')

        
    def test_aestrella(self):
        mi_grafo = tarea7.Grafo('A')
        mi_grafo.createGrafo('A55,B15,E20;B40,A15,C20,F40;C25,B20,D25;D40,C25,G40;E45,A20,F30;F20,B40,E30,G20;G0,D40,F20',True)
        self.assertEqual(mi_grafo.a_star('G'),['A', 'E','F', 'G'])
        self.assertEqual(mi_grafo.a_star('D'),['A', 'B', 'C','D'])
        self.assertEqual(mi_grafo.a_star('C'),['A', 'B', 'C'])
        print('GRAFO 1 CORRECTO')
        
        
        mi_grafo2 = tarea7.Grafo('A')
        mi_grafo2.createGrafo('A55,B10,E20;B40,A10,C20,F45;C25,B20,D30;D40,C30,G40;E45,A20,F30;F20,B45,E30,G20;G0,D40,F20',True)
        self.assertEqual(mi_grafo2.a_star('G'),['A', 'E','F', 'G'])
        self.assertEqual(mi_grafo2.a_star('D'),['A', 'B', 'C','D'])
        self.assertEqual(mi_grafo2.a_star('C'),['A', 'B', 'C'])
        print('GRAFO 2 CORRECTO')


 


if __name__ == '__main__':
    unittest.main()
