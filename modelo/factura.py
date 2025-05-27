from datetime import datetime

class factura:
    def __init__(self, cliente, fecha):
        self.cliente = cliente
        self.fecha = fecha
        self.productos = []
        self.total = 0

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, value):
        self._cliente = value

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        try:
            self._fecha = datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("La fecha debe estar en formato YYYY-MM-DD.")

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.total += producto.precio

    def __str__(self):
        productos_detalle = "\n".join(str(p) for p in self.productos)
        return f"Factura - Cliente: {self.cliente.nombre}\nFecha: {self.fecha}\nProductos:\n{productos_detalle}\nTotal: ${self.total:.2f}"
