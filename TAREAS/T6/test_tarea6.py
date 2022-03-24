import unittest
import tarea5

class TestCodificarPalabra(unittest.TestCase):
    def test_binary_to_decimal(self):
        self.assertEqual(tarea5.binary_to_float('01000001100111100010000000000000'),19.765625)
        self.assertEqual(tarea5.binary_to_float('01000010000010111000000000000000'),34.875)
        self.assertEqual(tarea5.binary_to_float('01000010100010101101000000000000'),69.40625)
        self.assertEqual(tarea5.binary_to_float('01000001001100001000000000000000'),11.03125)
        self.assertEqual(tarea5.binary_to_float('01000010100110100101000000000000'),77.15625)

    def test_decodificar(self):
        self.assertEqual(tarea5.float_to_binary(54.125),'01000010010110001000000000000000')
        self.assertEqual(tarea5.float_to_binary(33.140625),'01000010000001001001000000000000')
        self.assertEqual(tarea5.float_to_binary(101.5625),'01000010110010110010000000000000')
        self.assertEqual(tarea5.float_to_binary(10256.283203125),'01000110001000000100000100100010')
        self.assertEqual(tarea5.float_to_binary(77.15625),'01000010100110100101000000000000')


if __name__ == '__main__':
    unittest.main()
