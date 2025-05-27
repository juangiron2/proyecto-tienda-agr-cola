import sys
import os

#Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import tkinter as tk
from tkinter import messagebox
from Controladores.controlador_cliente import ControladorCliente
from Controladores.controlador_producto import ControladorProducto
from Controladores.controlador_factura import ControladorFactura

# Instancias de los controladores
controlador_cliente = ControladorCliente()
controlador_producto = ControladorProducto()
controlador_factura = ControladorFactura()

# Funciones para las acciones de GUI
def crear_cliente():
    ventana_cliente = tk.Toplevel(root)
    ventana_cliente.title("Crear Cliente")

    tk.Label(ventana_cliente, text="Nombre:").grid(row=0, column=0)
    nombre = tk.Entry(ventana_cliente)
    nombre.grid(row=0, column=1)

    tk.Label(ventana_cliente, text="Cédula:").grid(row=1, column=0)
    cedula = tk.Entry(ventana_cliente)
    cedula.grid(row=1, column=1)

    def guardar_cliente():
        nombre_val = nombre.get()
        cedula_val = cedula.get()
        if nombre_val and cedula_val:
            controlador_cliente.crear(nombre_val, cedula_val)
            messagebox.showinfo("Éxito", f"Cliente {nombre_val} creado con éxito.")
            ventana_cliente.destroy()
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    tk.Button(ventana_cliente, text="Guardar", command=guardar_cliente).grid(row=2, column=0, columnspan=2)

def listar_clientes():
    clientes = controlador_cliente.listar()
    if not clientes:
        messagebox.showinfo("Clientes", "No hay clientes registrados.")
    else:
        ventana_listado = tk.Toplevel(root)
        ventana_listado.title("Listado de Clientes")
        for i, cliente in enumerate(clientes):
            tk.Label(ventana_listado, text=f"{i + 1}. {cliente.nombre} - {cliente.cedula}").pack()

def crear_producto():
    ventana_producto = tk.Toplevel(root)
    ventana_producto.title("Crear Producto")

    tk.Label(ventana_producto, text="Nombre:").grid(row=0, column=0)
    nombre = tk.Entry(ventana_producto)
    nombre.grid(row=0, column=1)

    tk.Label(ventana_producto, text="Precio:").grid(row=1, column=0)
    precio = tk.Entry(ventana_producto)
    precio.grid(row=1, column=1)

    def guardar_producto():
        nombre_val = nombre.get()
        try:
            precio_val = float(precio.get())
            controlador_producto.crear(nombre_val, precio_val)
            messagebox.showinfo("Éxito", f"Producto {nombre_val} creado con éxito.")
            ventana_producto.destroy()
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número válido.")

    tk.Button(ventana_producto, text="Guardar", command=guardar_producto).grid(row=2, column=0, columnspan=2)

def listar_productos():
    productos = controlador_producto.listar()
    if not productos:
        messagebox.showinfo("Productos", "No hay productos registrados.")
    else:
        ventana_listado = tk.Toplevel(root)
        ventana_listado.title("Listado de Productos")
        for i, producto in enumerate(productos):
            tk.Label(ventana_listado, text=f"{i + 1}. {producto['nombre']} - ${producto['precio']}").pack()

def mostrar_estadisticas_ventas():
    controlador_factura.mostrar_estadisticas_ventas()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Sistema de Facturación - Tienda Agrícola")

# Menú principal
tk.Label(root, text="--- TIENDA AGRÍCOLA---", font=("Helvetica", 16)).pack(pady=10)

tk.Button(root, text="Crear Cliente", command=crear_cliente, width=20).pack(pady=5)
tk.Button(root, text="Listar Clientes", command=listar_clientes, width=20).pack(pady=5)
tk.Button(root, text="Crear Producto", command=crear_producto, width=20).pack(pady=5)
tk.Button(root, text="Listar Productos", command=listar_productos, width=20).pack(pady=5)
tk.Button(root, text="Estadísticas de Ventas", command=mostrar_estadisticas_ventas, width=20).pack(pady=5)

tk.Button(root, text="Salir", command=root.quit, width=20, bg="red", fg="white").pack(pady=10)

root.mainloop()
