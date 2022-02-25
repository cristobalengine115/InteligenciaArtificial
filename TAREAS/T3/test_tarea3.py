import unittest
import T3

class TestGeneracion(unittest.TestCase):
    def test_generacion(self):
        gen = T3.paso_gen(T3.crear_tabla_reglas(),[0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1])
        self.assertEqual(gen,[1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        gen = T3.paso_gen(T3.crear_tabla_reglas(),[0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0])
        self.assertEqual(gen,[1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1])
        gen = T3.paso_gen(T3.crear_tabla_reglas(),[0, 0, 0, 1, 0, 1, 1, 0, 1, 1])
        self.assertEqual(gen,[1, 0, 1, 1, 1, 1, 1, 1, 1, 1])
if __name__ == '__main__':
    unittest.main()