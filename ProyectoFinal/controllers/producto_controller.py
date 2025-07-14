from models.producto import Producto
from db import productos

class ProductoController:
    def __init__(self):
        self.modelo = Producto(productos)

    def agregar_producto(self):
        codigo = int(input("Código: "))
        if not isinstance(codigo, int) or codigo<0:
            raise ValueError("El codigo debe ser un entero mayor a 0")
        nombre = input("Nombre: ").strip()
        if not isinstance(nombre, str) or nombre.isspace() or nombre=="":
            raise ValueError("El nombre debe ser un string")
        categoria = input("Categoría: ").strip()
        if not isinstance(categoria, str) or categoria.isspace() or categoria=="":
            raise ValueError("La categoria debe ser un string")
        precio = float(input("Precio: "))
        if not isinstance(precio, (float, int)) or precio < 0:
            raise ValueError("El precio no puede ser negativo")
        stock = int(input("Stock actual: "))
        if not isinstance(stock, int) or stock < 0:
            raise ValueError("El stock debe ser un entero positivo")
        stock_min = int(input("Stock mínimo: "))
        if not isinstance(stock_min, int) or stock_min < 0:
            raise ValueError("El stock minimo debe ser un entero positivo")
        proveedor_id = input("ID proveedor: ").strip()
        if not isinstance(proveedor_id, str) or proveedor_id.isspace() or proveedor_id=="":
            raise ValueError("El id del proveedor debe ser un string valido")

        producto = {
            "codigo": codigo,
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "stockActual": stock,
            "stockMinimo": stock_min,
            "proveedorId": proveedor_id
        }

        self.modelo.agregar(producto)

    def listar_productos(self):
        print("== Lista de todos los productos ==")
        self.modelo.listar_todos()

    def consultar_stock(self):
        print("== Consultar stock ==")
        codigo = input("Código de producto: ").strip()
        self.modelo.consultar_stock(codigo)

    def listar_stock_bajo(self):
        print("== Productos con stock bajo ==")
        self.modelo.listar_stock_bajo()
