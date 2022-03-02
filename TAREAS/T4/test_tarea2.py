import unittest
import tarea4

class TestCodificarPalabra(unittest.TestCase):
    def test_codificar(self):
        #Test when phrase is hola mundo
        self.assertEqual(tarea4.codificar_palabra('la criptografia es romantica',4)[:10],'LIGIRNAAPR')
        self.assertEqual(tarea4.codificar_palabra('HOLA MUNDO'),'827370907164729373')
        self.assertEqual(tarea4.codificar_palabra('hOla   MunDo'),'827370907164729373')
        self.assertEqual(tarea4.codificar_palabra('hOla   MuñDo'),None)
    
    def test_decodificar(self):
        self.assertEqual(tarea4.decodificar_palabra('LIGIRNAAPRAOTZCTAEMIIROFSACG'),'LACRIPTOGRAFIAESROMANTICAZIG')
        self.assertEqual(tarea4.decodificar_palabra('82737097164729373'),None)
    
    def test_normalizar(self):
        self.assertEqual(tarea4.normalizar_cadena('HOLA COMO TE VA'),'HOLACOMOTEVA')
        self.assertEqual(tarea4.normalizar_cadena('saludos a  todos'),'SALUDOSATODOS')

if __name__ == '__main__':
    unittest.main()