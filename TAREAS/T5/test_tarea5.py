import unittest
import tarea5

class TestCodificarPalabra(unittest.TestCase):
    def test_codificar(self):
        #Test when phrase is hola mundo
        self.assertEqual(tarea5.codificar_palabra('la criptografia es romantica',4)[:10],'LIGIRNAAPR')
        self.assertEqual(tarea5.codificar_palabra('estudiamos en la facultad de ingenieria',6)[:15],'EALLIESMATNRTOF')
        self.assertEqual(tarea5.codificar_palabra('Somos alberto cristobal y angel',10)[:14],'STLOOYMCAORNSI')
        self.assertEqual(tarea5.codificar_palabra('Hola',5),None)
    
    def test_decodificar(self):
        self.assertEqual(tarea5.decodificar_palabra('LIGIRNAAPRAOTZCTAEMIIROFSACG',4),'LACRIPTOGRAFIAESROMANTICAZIG')
        self.assertEqual(tarea5.decodificar_palabra('HLOA',2),'HOLA')
        self.assertEqual(tarea5.decodificar_palabra('SOLRCSBYGOSBTRTAAEMAEOIOLNL',3),'SOMOSALBERTOCRISTOBALYANGEL')
    
    def test_normalizar(self):
        self.assertEqual(tarea5.normalizar_cadena('HOLA COMO TE VA'),'HOLACOMOTEVA')
        self.assertEqual(tarea5.normalizar_cadena('saludos a  todos'),'SALUDOSATODOS')

if __name__ == '__main__':
    unittest.main()