import unittest
from src.logica.Suma import Suma

class PruebaSuma(unittest.TestCase):
    def setUp(self):
        self.suma = Suma()

    def tearDown(self):
        self.suma=None

    def test_operacionSuma_dosNumerosPositivos_retornaSuma(self):
        # Arrange
        self.sumando1=19
        self.sumando2=50
        self.resultado=69

        # Do
        self.resultadoActual=self.suma.operacionSuma(self.sumando1,self.sumando2)

        # Assert
        self.assertEqual(self.resultado, self.resultadoActual)

    def test_operacionSuma_dosNumerosNegativos_retornaSuma(self):
        # Arrange
        self.sumando1=-3
        self.sumando2=-7
        self.resultado=-10

        # Do
        self.resultadoActual=self.suma.operacionSuma(self.sumando1,self.sumando2)

        # Assert
        self.assertEqual(self.resultado, self.resultadoActual)

    def test_operacionSuma_dosNumerosPositivos_retornaResta(self):
        # Arrange
        self.Minuendo = 50
        self.Sustraendo = 30
        self.resultado = 20

        # Do
        self.resultadoActual = self.suma.operacionSuma(self.Minuendo, self.Sustraendo)

        # Assert
        self.assertEqual(self.resultado, self.resultadoActual)