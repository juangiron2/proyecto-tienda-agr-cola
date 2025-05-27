import sys
import os

#Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from Controladores.controlador_producto import ControladorProducto
from Modelo.antibiotico import Antibiotico
from Modelo.control_fertilizantes import ControlFertilizantes

class TestProducto(unittest.TestCase):
    def setUp(self):
        self.controlador = ControladorProducto()

    def test_crear_antibiotico(self):
        antibiotico = Antibiotico("Amoxicilina", 150.0, 500, "Bovinos")
        self.controlador.create(antibiotico)
        productos = self.controlador.read()
        self.assertEqual(len(productos), 1)
        self.assertEqual(productos[0].nombre, "Amoxicilina")

    def test_crear_fertilizante(self):
        fertilizante = ControlFertilizantes("Fertilizante XYZ", 200.0, "ICA-123", 15, "2023-11-01")
        self.controlador.create(fertilizante)
        productos = self.controlador.read()
        self.assertEqual(len(productos), 1)
        self.assertEqual(productos[0].nombre, "Fertilizante XYZ")

if __name__ == "__main__":
    unittest.main()
