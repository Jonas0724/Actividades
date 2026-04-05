from abc import ABC, abstractmethod
from datetime import date


class Producto:
    def __init__(self, codigo: int, descripcion: str,
                 precio: float, cantidad_disponible: int):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def actualizar_stock(self, cantidad: int) -> None:
        self.cantidad_disponible += cantidad

    def es_disponible(self, cantidad: int) -> bool:
        return self.cantidad_disponible >= cantidad


class Catalogo:
    def __init__(self, id_catalogo: int):
        self.id_catalogo = id_catalogo
        self.productos = []

    def enviar_catalogo(self):
        return self.productos

    def listar_productos(self):
        for producto in self.productos:
            print(producto.descripcion)

    def buscar_producto(self, codigo: int):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None


class DetalleOrden:
    def __init__(self, producto: Producto,
                 cantidad: int, precio_unitario: float):
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def calcular_subtotal(self) -> float:
        return self.cantidad * self.precio_unitario


class TipoPago(ABC):

    @abstractmethod
    def procesar_pago(self, monto: float):
        pass


class TarjetaCredito(TipoPago):
    def __init__(self, numero_tarjeta: str,
                 titular: str, fecha_expiracion: date, cvv: int):
        self.numero_tarjeta = numero_tarjeta
        self.titular = titular
        self.fecha_expiracion = fecha_expiracion
        self.cvv = cvv

    def validar_tarjeta(self) -> bool:
        return True

    def procesar_pago(self, monto: float):
        if self.validar_tarjeta():
            print(f"Pago de {monto} procesado con tarjeta de crédito")
        else:
            print("Tarjeta inválida")


class OrdenCompra:
    def __init__(self, id_orden: int, fecha: date):
        self.id_orden = id_orden
        self.fecha = fecha
        self.estado = "pendiente"
        self.detalles = []
        self.total = 0

    def agregar_producto(self, producto: Producto, cantidad: int):
        detalle = DetalleOrden(producto, cantidad, producto.precio)
        self.detalles.append(detalle)

    def eliminar_producto(self, producto: Producto):
        self.detalles = [
            d for d in self.detalles if d.producto != producto
        ]

    def calcular_total(self):
        self.total = sum(
            detalle.calcular_subtotal() for detalle in self.detalles
        )
        return self.total

    def confirmar_orden(self):
        self.estado = "confirmada"

    def cancelar_orden(self):
        self.estado = "cancelada"


class Envio:
    def __init__(self, id_envio: int, fecha_envio: date,
                 direccion_entrega: str):
        self.id_envio = id_envio
        self.fecha_envio = fecha_envio
        self.estado = "pendiente"
        self.direccion_entrega = direccion_entrega

    def actualizar_estado(self, estado: str):
        self.estado = estado

    def confirmar_entrega(self):
        self.estado = "entregado"


class EmpresaTransporte:
    def __init__(self, nit: str, nombre: str):
        self.nit = nit
        self.nombre = nombre

    def entregar_orden(self, envio: Envio):
        envio.confirmar_entrega()
        print("Orden entregada")


class Cliente:
    def __init__(self, id_cliente: int, nombre: str,
                 email: str, direccion: str):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.direccion = direccion

    def generar_orden(self, id_orden: int):
        return OrdenCompra(id_orden, date.today())

    def confirmar_orden(self, orden: OrdenCompra):
        orden.confirmar_orden()

    def cancelar_orden(self, orden: OrdenCompra):
        orden.cancelar_orden()

    def consultar_producto(self, catalogo: Catalogo, codigo: int):
        return catalogo.buscar_producto(codigo)

    def solicitar_catalogo(self, catalogo: Catalogo):
        return catalogo.enviar_catalogo()

    def presentar_queja(self, descripcion: str):
        return Queja(1, date.today(), descripcion)


class AgenteDeposito:
    def __init__(self, id_agente: int, nombre: str, email: str):
        self.id_agente = id_agente
        self.nombre = nombre
        self.email = email

    def procesar_orden(self, orden: OrdenCompra):
        print("Procesando orden")

    def armar_pedido(self, orden: OrdenCompra):
        print("Pedido armado")


class Queja:
    def __init__(self, id_queja: int, fecha: date, descripcion: str):
        self.id_queja = id_queja
        self.fecha = fecha
        self.descripcion = descripcion
        self.estado = "abierta"

    def remitir_gerente(self, gerente):
        gerente.recibir_queja(self)


class Gerente:
    def __init__(self, nombre: str, apellido: str):
        self.nombre = nombre
        self.apellido = apellido

    def recibir_queja(self, queja: Queja):
        print("Queja recibida por el gerente")


def main():

    producto = Producto(1, "Laptop", 2000, 10)

    catalogo = Catalogo(1)
    catalogo.productos.append(producto)

    cliente = Cliente(1, "Juan", "juan@email.com", "Bogotá")

    orden = cliente.generar_orden(1)

    orden.agregar_producto(producto, 2)

    total = orden.calcular_total()

    tarjeta = TarjetaCredito(
        "12345678",
        "Juan",
        date(2028, 5, 1),
        123
    )

    tarjeta.procesar_pago(total)

    envio = Envio(1, date.today(), "Bogotá")

    transporte = EmpresaTransporte("123", "Servientrega")

    transporte.entregar_orden(envio)


if __name__ == "__main__":
    main()