import sys
import os

#Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from Controladores.controlador_factura import ControladorFactura
from Controladores.controlador_cliente import ControladorCliente
from datetime import datetime

class TestFactura(unittest.TestCase):
    def setUp(self):
        self.controlador_cliente = ControladorCliente()
        self.controlador_factura = ControladorFactura()
        self.cliente = self.controlador_cliente.create("Pedro Gómez", "1231231230")

    def test_crear_factura(self):
        factura = self.controlador_factura.create(self.cliente, "2024-01-01")
        self.assertEqual(factura.cliente, self.cliente)
        self.assertEqual(factura.fecha, datetime(2024, 1, 1).date())

    def test_buscar_facturas_por_cedula(self):
        self.controlador_factura.create(self.cliente, "2024-01-01")
        facturas = self.controlador_factura.find_by_cliente("1231231230")
        self.assertEqual(len(facturas), 1)

if __name__ == "__main__":
    unittest.main()
