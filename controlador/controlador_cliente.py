class ControladorCliente:
    def __init__(self):
        self.clientes = []  # Lista para almacenar clientes temporalmente

    def crear(self):
        print("\n--- Crear Cliente ---")
        nombre = input("Ingrese el nombre del cliente: ")
        cedula = input("Ingrese la cédula del cliente: ")
        self.clientes.append({"nombre": nombre, "cedula": cedula})
        print(f"Cliente '{nombre}' creado con éxito.")

    def listar(self):
        print("\n--- Lista de Clientes ---")
        if not self.clientes:
            print("No hay clientes registrados.")
        for cliente in self.clientes:
            print(f"Nombre: {cliente['nombre']}, Cédula: {cliente['cedula']}")

    def actualizar(self):
        print("\n--- Actualizar Cliente ---")
        cedula = input("Ingrese la cédula del cliente a actualizar: ")
        for cliente in self.clientes:
            if cliente['cedula'] == cedula:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                cliente['nombre'] = nuevo_nombre
                print(f"Cliente con cédula {cedula} actualizado.")
                return
        print(f"No se encontró un cliente con cédula {cedula}.")

    def eliminar(self):
        print("\n--- Eliminar Cliente ---")
        cedula = input("Ingrese la cédula del cliente a eliminar: ")
        for cliente in self.clientes:
            if cliente['cedula'] == cedula:
                self.clientes.remove(cliente)
                print(f"Cliente con cédula {cedula} eliminado.")
                return
        print(f"No se encontró un cliente con cédula {cedula}.")
