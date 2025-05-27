import sys
import os

#Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from Controladores.controlador_cliente import ControladorCliente
from Controladores.controlador_producto import ControladorProducto
from Controladores.controlador_factura import ControladorFactura


controlador_producto = ControladorProducto()

# Inicializamos los controladores
controlador_cliente = ControladorCliente()
controlador_producto = ControladorProducto()
controlador_factura = ControladorFactura()

def mostrar_menu():
    while True:
        print("\n--- Sistema de Facturación ---")
        print("\n--- Tienda Agrícola ---")
        print("1. Crear Cliente")
        print("2. Listar Clientes")
        print("3. Actualizar Cliente")
        print("4. Eliminar Cliente")
        print("5. Crear Producto")
        print("6. Listar Productos")
        print("7. Actualizar Producto")
        print("8. Eliminar Producto")
        print("9. Crear Factura")
        print("10. Listar Facturas")
        print("11. Actualizar Factura")
        print("12. Eliminar Factura")
        print("13. Mostrar Información Detallada de Productos")  
        print("14. Mostrar Estadísticas de Ventas")  
        print("15. Mostrar Recomendaciones de Uso por Categoría")  
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        # Delegamos cada opción al controlador correspondiente
        if opcion == '1':
            controlador_cliente.crear()
        elif opcion == '2':
            controlador_cliente.listar()
        elif opcion == '3':
            controlador_cliente.actualizar()
        elif opcion == '4':
            controlador_cliente.eliminar()
        elif opcion == '5':
            controlador_producto.crear()
        elif opcion == '6':
            controlador_producto.listar()
        elif opcion == '7':
            controlador_producto.actualizar()
        elif opcion == '8':
            controlador_producto.eliminar()
        elif opcion == '9':
            controlador_factura.crear()
        elif opcion == '10':
            controlador_factura.listar()
        elif opcion == '11':
            controlador_factura.actualizar()
        elif opcion == '12':
            controlador_factura.eliminar()
        elif opcion == '13':  
            controlador_producto.mostrar_informacion_detallada()
        elif opcion == '14':  
            controlador_factura.mostrar_estadisticas_ventas()
        elif opcion == '15':  
            controlador_producto.mostrar_recomendaciones()
        elif opcion == '0':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")
