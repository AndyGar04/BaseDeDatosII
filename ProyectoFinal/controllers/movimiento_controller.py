from models.movimiento import Movimiento
from db import productos, movimientos
from bson import ObjectId
from datetime import datetime

class MovimientoController:
    def __init__(self):
        self.modelo = Movimiento(movimientos, productos)
    def registrar_movimiento(self):
        print("Registrar movimiento")
        producto_id = input("ID del producto: ")
        if not isinstance(producto_id, str) or producto_id=="" or producto_id.isspace():
            raise ValueError("El producto debe ser un id valido")
        tipo = input("Tipo (entrada/salida): ").strip()
        if not isinstance(tipo, str) or tipo=="" or tipo.isspace():
            raise ValueError("El tipo debe ser string valido")
        cantidad = int(input("Cantidad: "))
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un numero entero valido")
        motivo = input("Motivo: ").strip()
        if not isinstance(motivo, str) or motivo == "" or motivo.isspace():
            raise ValueError("El motivo debe ser un string")

        movimiento = {
            "productoId": producto_id,
            "tipo": tipo,
            "cantidad": cantidad,
            "motivo": motivo,
        }

        self.modelo.registrar(movimiento)

    def generar_reporte(self):
        print("Reporte de movimientos")
        
        fecha_inicio_str = input("Fecha inicio (YYYY-MM-DD): ").strip()
        fecha_fin_str = input("Fecha fin (YYYY-MM-DD): ").strip()

        try:
            fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d")
            fecha_fin = datetime.strptime(fecha_fin_str, "%Y-%m-%d")

            if fecha_inicio > fecha_fin:
                print("Error: La fecha de inicio no puede ser posterior a la fecha de fin.")
                return 

            if self.modelo:
                self.modelo.reporte(fecha_inicio, fecha_fin)
            else:
                print("Error: El modelo de reporte no está inicializado.")

        except ValueError:
            print("Error: Se ingresó una fecha con formato inválido. Por favor, use el formato YYYY-MM-DD.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
