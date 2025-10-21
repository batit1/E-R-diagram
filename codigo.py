from datetime import datetime
from typing import List

class Cliente:
    def __init__(self, id: int, nombre: str, email: str, puntos: int = 0):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.puntos = puntos
        self.pedidos: List[Pedido] = []  # Relación 1:N

class Empleado:
    def __init__(self, id: int, nombre: str, rol: str, turno: str):
        self.id = id
        self.nombre = nombre
        self.rol = rol
        self.turno = turno
        self.pedidos_atendidos: List[Pedido] = []  # Relación 1:N

class Producto:
    def __init__(self, id: int, nombre: str, tipo: str, precio: float):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio

class PedidoProducto:
    def __init__(self, producto: Producto, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad

class Pedido:
    def __init__(self, id: int, cliente: Cliente, empleado: Empleado, fecha_hora: datetime):
        self.id = id
        self.fecha_hora = fecha_hora
        self.cliente = cliente
        self.empleado = empleado
        self.productos: List[PedidoProducto] = []  # Relación N:M

    def agregar_producto(self, producto: Producto, cantidad: int):
        self.productos.append(PedidoProducto(producto, cantidad))
