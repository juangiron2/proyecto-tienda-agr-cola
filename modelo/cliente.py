class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.facturas = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if isinstance(value, str) and value.strip():
            self._nombre = value
        else:
            raise ValueError("El nombre no puede estar vacío.")

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, value):
        if isinstance(value, str) and value.isdigit():
            self._cedula = value
        else:
            raise ValueError("La cédula debe ser un número válido.")

    def agregar_factura(self, factura):
        self.facturas.append(factura)

    def __str__(self):
        return f"Cliente: {self.nombre}, Cédula: {self.cedula}, Total Facturas: {len(self.facturas)}"
