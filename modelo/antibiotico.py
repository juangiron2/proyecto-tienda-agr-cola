import sys
import os

#Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Modelo.producto import Producto

class Antibiotico(Producto):
    def __init__(self, nombre, precio, dosis, tipo_animal):
        super().__init__(nombre, precio)
        self.dosis = dosis
        self.tipo_animal = tipo_animal

    @property
    def dosis(self):
        return self._dosis

    @dosis.setter
    def dosis(self, value):
        if 400 <= value <= 600:
            self._dosis = value
        else:
            raise ValueError("La dosis debe estar entre 400Kg y 600Kg.")

    @property
    def tipo_animal(self):
        return self._tipo_animal

    @tipo_animal.setter
    def tipo_animal(self, value):
        if value in ["Bovinos", "Caprinos", "Porcinos"]:
            self._tipo_animal = value
        else:
            raise ValueError("Tipo de animal no válido. Debe ser Bovinos, Caprinos o Porcinos.")

    def __str__(self):
        return f"Antibiótico: {self.nombre}, Precio: ${self.precio:.2f}, Dosis: {self.dosis}Kg, Animal: {self.tipo_animal}"
