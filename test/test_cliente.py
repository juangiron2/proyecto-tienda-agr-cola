import sys
import os

#Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from Controladores.controlador_cliente import ControladorCliente

class TestCliente(unittest.TestCase):
    def setUp(self):
        self.controlador = ControladorCliente()

    def test_crear_cliente(self):
        cliente = self.controlador.create("Juan Pérez", "1234567890")
        self.assertEqual(cliente.nombre, "Juan Pérez")
        self.assertEqual(cliente.cedula, "1234567890")

    def test_buscar_cliente(self):
        self.controlador.create("Ana López", "9876543210")
        cliente = self.controlador.find_by_id("9876543210")
        self.assertIsNotNone(cliente)
        self.assertEqual(cliente.nombre, "Ana López")

    def test_eliminar_cliente(self):
        self.controlador.create("Carlos Ruiz", "111222333")
        self.controlador.delete("111222333")
        cliente = self.controlador.find_by_id("111222333")
        self.assertIsNone(cliente)

if __name__ == "__main__":
    unittest.main()
