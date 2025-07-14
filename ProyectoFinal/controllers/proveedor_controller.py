from models.proveedor import Proveedor
from db import proveedores

class ProveedorController:
    def __init__(self):
        self.modelo = Proveedor(proveedores)

    def registrar_proveedor(self):
        print("Registrar nuevo proveedor")
        nombre = input("Nombre: ").strip()
        if not isinstance(nombre, str) or nombre.isspace() or nombre=="":
            raise ValueError("El nombre debe ser un string valido")
        contacto = input("Contacto: ").strip()
        if not isinstance(contacto, str) or contacto.isspace() or contacto=="":
            raise ValueError("El contacto debe ser un string valido")
        telefono = input("Teléfono: ").strip()
        if not isinstance(telefono, str) or telefono.isspace() or telefono=="":
            raise ValueError("El telefono debe ser un string valido")
        email = input("Email: ").strip()
        if not isinstance(email, str) or email.isspace() or email=="":
            raise ValueError("El email debe ser un string valido")
        
        proveedor = {
            "nombre": nombre,
            "contacto": contacto,
            "telefono": telefono,
            "email": email
        }

        self.modelo.agregar(proveedor)

    def listar_proveedores(self):
        print("== Lista de proveedores ==")
        self.modelo.listar()
