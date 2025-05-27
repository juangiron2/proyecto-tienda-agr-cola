import sys
import os

#Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from datetime import date
from Modelo.factura import factura
from Modelo.producto import Producto
from Controladores.controlador_factura import ControladorFactura
from Modelo.cliente import Cliente

class TestControladorFactura(unittest.TestCase):
    def setUp(self):
        self.controlador = ControladorFactura()
        self.cliente = Cliente("12345678", "Juan Pérez")
        self.producto1 = Producto("Producto 1", 100.50)
        self.producto2 = Producto("Producto 2", 50.75)
        self.factura = self.controlador.create(self.cliente, "2024-11-20")
        self.factura.agregar_producto(self.producto1)
        self.factura.agregar_producto(self.producto2)

    def test_calcular_total_factura(self):
        total = self.controlador.calcular_total_factura(self.factura.id_factura)
        self.assertEqual(total, 151.25)

    def test_calcular_total_general(self):
        total_general = self.controlador.calcular_total_general()
        self.assertEqual(total_general, 151.25)

    def test_find_by_cliente(self):
        facturas_cliente = self.controlador.find_by_cliente("12345678")
        self.assertEqual(len(facturas_cliente), 1)

    def test_delete_factura(self):
        self.controlador.delete(self.factura.id_factura)
        self.assertEqual(len(self.controlador.facturas), 0)

if __name__ == "__main__":
    unittest.main()
