import unittest
from Calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    # Test de la función Suma
    def test_suma_casos_validos(self):
        self.assertEqual(self.calc.Suma(10, 5), 15)
        self.assertEqual(self.calc.Suma(-10, -5), -15)
        self.assertAlmostEqual(self.calc.Suma(1.5, 2.3), 3.8, places=1)

    def test_suma_errores(self):
        with self.assertRaises(ValueError):
            self.calc.Suma(float('nan'), 5)
        with self.assertRaises(ValueError):
            self.calc.Suma(5, float('nan'))

    def test_suma_grandes_valores(self):
        self.assertEqual(self.calc.Suma(1e100, 1e100), 2e100)

    # Test de la función Resta
    def test_resta_casos_validos(self):
        self.assertEqual(self.calc.Resta(10, 5), 5)
        self.assertEqual(self.calc.Resta(-10, -5), -5)
        self.assertAlmostEqual(self.calc.Resta(1.5, 2.3), -0.8, places=1)

    def test_resta_errores(self):
        with self.assertRaises(ValueError):
            self.calc.Resta(float('nan'), 5)
        with self.assertRaises(ValueError):
            self.calc.Resta(5, float('nan'))

    def test_resta_grandes_valores(self):
        self.assertEqual(self.calc.Resta(1e100, 1e100), 0)

    # Test de la función Producto
    def test_producto_casos_validos(self):
        self.assertEqual(self.calc.Producto(10, 5), 50)
        self.assertEqual(self.calc.Producto(-10, -5), 50)
        self.assertAlmostEqual(self.calc.Producto(1.5, 2.3), 3.45, places=2)

    def test_producto_errores(self):
        with self.assertRaises(ValueError):
            self.calc.Producto(float('nan'), 5)
        with self.assertRaises(ValueError):
            self.calc.Producto(5, float('nan'))

    def test_producto_grandes_valores(self):
        self.assertAlmostEqual(self.calc.Producto(1e50, 1e50), 1e100, delta=1e98)

    # Test de la función División
    def test_division_casos_validos(self):
        self.assertEqual(self.calc.Division(10, 2), 5)
        self.assertAlmostEqual(self.calc.Division(1.5, 0.5), 3, places=1)
        self.assertEqual(self.calc.Division(-10, -2), 5)

    def test_division_errores(self):
        with self.assertRaises(ValueError):
            self.calc.Division(10, 0)
        with self.assertRaises(ValueError):
            self.calc.Division(float('nan'), 2)

    def test_division_grandes_valores(self):
        self.assertAlmostEqual(self.calc.Division(1e100, 1e50), 1e50, delta=1e48)

    # Test de la función Potencia_2
    def test_potencia_2_casos_validos(self):
        self.assertEqual(self.calc.Potencia_2(3), 9)
        self.assertEqual(self.calc.Potencia_2(-3), 9)
        self.assertAlmostEqual(self.calc.Potencia_2(1.5), 2.25, places=2)

    def test_potencia_2_errores(self):
        with self.assertRaises(ValueError):
            self.calc.Potencia_2(float('nan'))

    def test_potencia_2_grandes_valores(self):
        self.assertAlmostEqual(self.calc.Potencia_2(1e50), 1e100, delta=2e84)

    # Test de la función Potencia_n
    def test_potencia_n_casos_validos(self):
        self.assertEqual(self.calc.Potencia_n(3, 3), 27)
        self.assertEqual(self.calc.Potencia_n(2, -2), 0.25)
        self.assertAlmostEqual(self.calc.Potencia_n(1.5, 2), 2.25, places=2)

    def test_potencia_n_errores(self):
        with self.assertRaises(ValueError):
            self.calc.Potencia_n(float('nan'), 2)
        with self.assertRaises(ValueError):
            self.calc.Potencia_n(2, float('nan'))

    def test_potencia_n_grandes_valores(self):
        self.assertAlmostEqual(self.calc.Potencia_n(1e10, 2), 1e20, places=1)

    # Test de la función Raiz_cuadrada
    def test_raiz_cuadrada_casos_validos(self):
        self.assertEqual(self.calc.Raiz_cuadrada(4), 2)
        self.assertAlmostEqual(self.calc.Raiz_cuadrada(2.25), 1.5, places=2)

    def test_raiz_cuadrada_errores(self):
        with self.assertRaises(ValueError):
            self.calc.Raiz_cuadrada(-4)
        with self.assertRaises(ValueError):
            self.calc.Raiz_cuadrada(float('nan'))

    def test_raiz_cuadrada_grandes_valores(self):
        self.assertAlmostEqual(self.calc.Raiz_cuadrada(1e100), 1e50, places=1)

if __name__ == "__main__":
    unittest.main()
