import unittest
from retroexcavadora import Retroexcavadora

class TestRetroexcavadora (unittest.TestCase):
    def setUp (self):
        self.retroexcavadora = Retroexcavadora (maxialtura=10, velocidadmaxi=20)
        
    def test_excavar (self):
        resultado = self.retroexcavadora.excavar(100, 2)
        self.assertEqual(resultado, 50)
        
    def testlevantarcarga(self):
        resultado = self.retroexcavadora.levantarcarga(500,8)
        self.assertTrue(resultado)
        self.assertEqual(self.retroexcavadora.cargaactual, 500)
        resultado = self.retroexcavadora.levantarcarga(500, 12)
        self.assertFalse (resultado)
        
    def test_movimiento (self):
        resultado = self.retroexcavadora.movimiento(10,2)
        self.assertEqual(resultado, 20)
        resultado = self.retroexcavadora.movimiento(25, 2)
        self.assertEqual(resultado, "La velocidad excede el limite maximo")
          
    def test_str(self):
        resultado = str(self.retroexcavadora)
        self.assertEqual(resultado, "La Retroexcavadora tiene una altura maxima 10 y con una velocidad maxima 20")
        
    if __name__ == '__main__':
        unittest.main()        