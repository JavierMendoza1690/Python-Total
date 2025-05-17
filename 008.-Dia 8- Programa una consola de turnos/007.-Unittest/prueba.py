#importando librerias
import unittest
import cambia_texto

class ProbarCambiaTexto(unittest.TestCase):

    #metodos para hacer test deben empezar obligatoriamente con la palabra test
    def test_mayusculas(self):
        palabra = 'buen dia'
        resultado = cambia_texto.todo_mayusculas(palabra)

        #metodo que se encarga de hacer la comparacion entre dos valores
        self.assertEqual(resultado, 'BUEN DIA') #OK
        #self.assertEqual(resultado, 'BueN DIA') #BueN DIA != BUEN DIA


#invocando inicio de test cuando se ejecute el programa
if __name__ == '__main__':
    unittest.main()