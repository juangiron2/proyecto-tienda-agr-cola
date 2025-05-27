class ControladorProducto:
    def __init__(self):
        self.productos = []
    
    def mostrar_informacion_detallada(self):
        if not self.productos:
            print("No hay productos registrados.")
            return
        
        print("\n--- Información Detallada de Productos ---")
        for producto in self.productos:
                print(f"Nombre: {producto.nombre}")
                print(f"Categoría: {producto.categoria}")
                print(f"Registro ICA: {producto.registro_ica}")
                print(f"Frecuencia de Aplicación: {producto.frecuencia_aplicacion} días")
                print(f"Período de Carencia: {producto.periodo_carencia} días")
                print(f"Precio: ${producto.precio}")
                print(f"Restricciones: {producto.restricciones}")
                print("-" * 40)

    def mostrar_recomendaciones(self):
            print("\n--- Recomendaciones de Uso por Categoría ---")
            print("Fertilizantes:")
            print("  - Aplicar cada 15 días durante la temporada de crecimiento.")
            print("Control de Plagas:")
            print("  - Usar con precaución. Esperar 7 días antes de cosechar.")
            print("Antibióticos:")
            print("  - Consulte a un veterinario antes de aplicar.")
            print("-" * 40)

    def crear(self):
        print("\n--- Crear Producto ---")
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        self.productos.append({"nombre": nombre, "precio": precio})
        print(f"Producto '{nombre}' creado con éxito.")

    def listar(self):
        print("\n--- Lista de Productos ---")
        if not self.productos:
            print("No hay productos registrados.")
        for producto in self.productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}")

    def actualizar(self):
        print("\n--- Actualizar Producto ---")
        nombre = input("Ingrese el nombre del producto a actualizar: ")
        for producto in self.productos:
            if producto['nombre'] == nombre:
                nuevo_precio = float(input("Ingrese el nuevo precio: "))
                producto['precio'] = nuevo_precio
                print(f"Producto '{nombre}' actualizado.")
                return
        print(f"No se encontró un producto con nombre '{nombre}'.")

    def eliminar(self):
        print("\n--- Eliminar Producto ---")
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        for producto in self.productos:
            if producto['nombre'] == nombre:
                self.productos.remove(producto)
                print(f"Producto '{nombre}' eliminado.")
                return
        print(f"No se encontró un producto con nombre '{nombre}'.")


