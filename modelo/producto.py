class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if isinstance(value, str) and value.strip():
            self._nombre = value
        else:
            raise ValueError("El nombre del producto no puede estar vacío.")

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._precio = value
        else:
            raise ValueError("El precio debe ser un número positivo.")

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}"
