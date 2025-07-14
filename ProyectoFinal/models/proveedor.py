from datetime import datetime

class Proveedor:
    def __init__(self, coleccion):
        self.proveedores = coleccion

    def agregar(self, proveedor):
        proveedor["fechaRegistro"] = datetime.utcnow()
        result = self.proveedores.insert_one(proveedor)
        print(f" Proveedor agregado con _id: {result.inserted_id}")

    def listar(self):
        proveedores = self.proveedores.find()
        print("📋 Lista de proveedores:")
        for p in proveedores:
            print(f"- ID: {p['_id']} | Nombre: {p['nombre']} | Contacto: {p['contacto']} | Email: {p['email']}")
