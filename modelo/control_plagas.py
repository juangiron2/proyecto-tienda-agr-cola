import sys
import os

#Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Modelo.producto import Producto

class ControlPlagas(Producto):
    def __init__(self, nombre, precio, registro_ica, frecuencia_aplicacion, periodo_carencia):
        super().__init__(nombre, precio)
        self.registro_ica = registro_ica
        self.frecuencia_aplicacion = frecuencia_aplicacion
        self.periodo_carencia = periodo_carencia

    @property
    def registro_ica(self):
        return self._registro_ica

    @registro_ica.setter
    def registro_ica(self, value):
        if isinstance(value, str) and value.strip():
            self._registro_ica = value
        else:
            raise ValueError("El registro ICA no puede estar vacío.")

    @property
    def frecuencia_aplicacion(self):
        return self._frecuencia_aplicacion

    @frecuencia_aplicacion.setter
    def frecuencia_aplicacion(self, value):
        if isinstance(value, int) and value > 0:
            self._frecuencia_aplicacion = value
        else:
            raise ValueError("La frecuencia de aplicación debe ser un número entero positivo.")

    @property
    def periodo_carencia(self):
        return self._periodo_carencia

    @periodo_carencia.setter
    def periodo_carencia(self, value):
        if isinstance(value, int) and value >= 0:
            self._periodo_carencia = value
        else:
            raise ValueError("El periodo de carencia debe ser un número entero no negativo.")

    def __str__(self):
        return f"Control Plagas: {self.nombre}, Precio: ${self.precio:.2f}, Registro ICA: {self.registro_ica}, " \
               f"Frecuencia: {self.frecuencia_aplicacion} días, Periodo de carencia: {self.periodo_carencia} días"
