import unittest
import Cambia_texto

class Test_CambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = 'buen dia'
        resultado = Cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'Buen Dia')


if __name__ == '__main__':
    unittest.main()
