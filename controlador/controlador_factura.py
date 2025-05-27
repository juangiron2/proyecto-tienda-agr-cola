import sys
import os

#Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from Icrud.utils import ICrud

class ControladorFactura(ICrud):
    def __init__(self):
        self.facturas = []

    
    def mostrar_estadisticas_ventas(self):
        if not self.facturas:  # Verificar si hay facturas registradas
            print("No hay facturas registradas.")
            return

        total_ventas = 0
        productos_vendidos = {}

        for factura in self.facturas:
            total_ventas += factura.total
            for producto in factura.productos:
                productos_vendidos[producto.nombre] = productos_vendidos.get(producto.nombre, 0) + 1

        producto_mas_vendido = max(productos_vendidos, key=productos_vendidos.get)

        print("\n--- Estadísticas de Ventas ---")
        print(f"Total de Ventas: ${total_ventas}")
        print(f"Producto Más Vendido: {producto_mas_vendido} ({productos_vendidos[producto_mas_vendido]} unidades)")
        print("-" * 40)

    def create(self, cliente, fecha):
        factura = factura(cliente, fecha)
        self.facturas.append(factura)
        cliente.agregar_factura(factura)
        print(f"Factura creada con éxito para el cliente {cliente.nombre}.")
        return factura

    def read(self):
        if not self.facturas:
            print("No hay facturas registradas.")
            return []
        for factura in self.facturas:
            print(factura)
        return self.facturas

    def update(self, id_factura, nuevos_productos=None):
        factura = self.find_by_id(id_factura)
        if factura:
            if nuevos_productos:
                for producto in nuevos_productos:
                    factura.agregar_producto(producto)
            print(f"Factura actualizada: {factura}")
        else:
            print(f"No se encontró una factura con ID: {id_factura}.")

    def delete(self, id_factura):
        factura = self.find_by_id(id_factura)
        if factura:
            self.facturas.remove(factura)
            print(f"Factura con ID {id_factura} eliminada con éxito.")
        else:
            print(f"No se pudo eliminar la factura con ID: {id_factura}.")

    def find_by_id(self, id_factura):
        return next((f for f in self.facturas if str(f.id_factura) == str(id_factura)), None)

    def find_by_cliente(self, cedula):
        return [f for f in self.facturas if f.cliente.cedula == cedula]

    def calcular_total_factura(self, id_factura):
        factura = self.find_by_id(id_factura)
        if factura:
            return factura.total
        else:
            print(f"No se encontró una factura con ID: {id_factura}.")
            return 0

    def calcular_total_general(self):
        total = sum(factura.total for factura in self.facturas)
        print(f"Total acumulado de todas las facturas: ${total:.2f}")
        return total

