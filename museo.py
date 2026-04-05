from datetime import date


class Usuario:
    """Representa un usuario del sistema."""

    def __init__(self, id_usuario, nombre_usuario, contrasena):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

    def iniciar_sesion(self):
        print(f"{self.nombre_usuario} ha iniciado sesión")

    def cerrar_sesion(self):
        print(f"{self.nombre_usuario} ha cerrado sesión")


class Trabajador(Usuario):
    """Usuario que trabaja en el museo."""

    def __init__(self, id_usuario, nombre_usuario, contrasena,
                 nombre, id_empleado):
        super().__init__(id_usuario, nombre_usuario, contrasena)
        self.nombre = nombre
        self.id_empleado = id_empleado


class DirectorMuseo(Trabajador):
    """Director encargado de gestionar cesiones."""

    def registrar_cesion(self, obra, museo, fecha_inicio,
                         fecha_fin, importe):

        cesion = Cesion(obra, museo, fecha_inicio, fecha_fin, importe)
        obra.cesiones.append(cesion)
        print("Cesión registrada")

    def consultar_valor_total_obras(self, catalogo):
        total = 0
        for obra in catalogo.lista_obras:
            total += obra.valor_economico
        return total


class RestauradorJefe(Trabajador):
    """Responsable de restauraciones."""

    def enviar_restauracion(self, obra, tipo_restauracion):
        restauracion = Restauracion(
            obra,
            tipo_restauracion,
            date.today()
        )

        obra.restauraciones.append(restauracion)
        obra.estado = "RESTAURACION"

        print("Obra enviada a restauración")

    def finalizar_restauracion(self, restauracion, fecha_fin):
        restauracion.fecha_fin = fecha_fin
        restauracion.obra.estado = "EXHIBICION"

        print("Restauración finalizada")

    def consultar_historico(self, obra):
        return obra.restauraciones


class EncargadoCatalogo(Trabajador):
    """Persona encargada del catálogo."""

    def agregar_obra(self, catalogo, obra):
        catalogo.lista_obras.append(obra)

    def eliminar_obra(self, catalogo, obra):
        catalogo.lista_obras.remove(obra)

    def actualizar_obra(self, obra, nuevo_valor):
        obra.valor_economico = nuevo_valor


class Autor:
    """Autor de una obra de arte."""

    def __init__(self, id_autor, nombre, nacionalidad, fecha_nacimiento):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento


class Periodo:
    """Periodo artístico."""

    def __init__(self, nombre, fecha_inicio, fecha_fin):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin


class Sala:
    """Sala del museo donde se exponen obras."""

    def __init__(self, id_sala, nombre, piso):
        self.id_sala = id_sala
        self.nombre = nombre
        self.piso = piso
        self.obras = []

    def agregar_obra(self, obra):
        self.obras.append(obra)

    def listar_obras(self):
        return self.obras


class Obra:
    """Clase base para todas las obras de arte."""

    def __init__(self, id_obra, titulo, valor_economico,
                 fecha_creacion, fecha_ingreso_museo,
                 autor, periodo, sala):

        self.id_obra = id_obra
        self.titulo = titulo
        self.valor_economico = valor_economico
        self.fecha_creacion = fecha_creacion
        self.fecha_ingreso_museo = fecha_ingreso_museo

        self.autor = autor
        self.periodo = periodo
        self.sala = sala

        self.estado = "EXHIBICION"

        self.restauraciones = []
        self.cesiones = []

    def cambiar_sala(self, nueva_sala):
        self.sala = nueva_sala

    def actualizar_valor(self, valor):
        self.valor_economico = valor

    def consultar_historico(self):
        return self.restauraciones

    def consultar_cesiones(self):
        return self.cesiones


class Cuadro(Obra):
    """Tipo de obra: cuadro."""

    def __init__(self, tecnica, estilo, *args):
        super().__init__(*args)
        self.tecnica = tecnica
        self.estilo = estilo


class Escultura(Obra):
    """Tipo de obra: escultura."""

    def __init__(self, material, estilo, *args):
        super().__init__(*args)
        self.material = material
        self.estilo = estilo


class OtroObjeto(Obra):
    """Otros objetos artísticos."""

    def __init__(self, descripcion, *args):
        super().__init__(*args)
        self.descripcion = descripcion


class Museo:
    """Museo que puede recibir obras en cesión."""

    def __init__(self, id_museo, nombre, ciudad, pais):
        self.id_museo = id_museo
        self.nombre = nombre
        self.ciudad = ciudad
        self.pais = pais


class Cesion:
    """Representa una cesión de una obra a otro museo."""

    def __init__(self, obra, museo, fecha_inicio, fecha_fin, importe):
        self.obra = obra
        self.museo = museo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.importe = importe

    def iniciar_cesion(self):
        print("Cesión iniciada")

    def finalizar_cesion(self):
        print("Cesión finalizada")


class Restauracion:
    """Proceso de restauración de una obra."""

    def __init__(self, obra, tipo_restauracion, fecha_inicio):
        self.obra = obra
        self.tipo_restauracion = tipo_restauracion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = None

    def iniciar_restauracion(self):
        print("Restauración iniciada")

    def finalizar_restauracion(self):
        print("Restauración finalizada")


class Catalogo:
    """Catálogo de obras del museo."""

    def __init__(self):
        self.lista_obras = []

    def agregar_obra(self, obra):
        self.lista_obras.append(obra)

    def eliminar_obra(self, obra):
        self.lista_obras.remove(obra)

    def buscar_obra(self, id_obra):

        for obra in self.lista_obras:
            if obra.id_obra == id_obra:
                return obra

        return None

    def listar_obras(self):
        return self.lista_obras


class Visitante:
    """Persona que consulta el catálogo."""

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def consultar_catalogo(self, catalogo):
        return catalogo.listar_obras()

    def consultar_obras_por_sala(self, sala):
        return sala.listar_obras()
    

def main():

    # =========================
    # Crear catálogo
    # =========================
    catalogo = Catalogo()

    # =========================
    # Crear autor y periodo
    # =========================
    autor1 = Autor(
        1,
        "Leonardo da Vinci",
        "Italiano",
        date(1452, 4, 15)
    )

    autor2 = Autor(
        2,
        "Miguel Angel",
        "Italiano",
        date(1455, 4, 15)
    )

    periodo1 = Periodo(
        "Renacimiento",
        date(1400, 1, 1),
        date(1600, 1, 1)
    )

    # =========================
    # Crear sala
    # =========================
    sala1 = Sala(1, "Sala Renacimiento", 1)

    # =========================
    # Crear obras
    # =========================
    obra1 = Cuadro(
        "Óleo",
        "Renacentista",
        1,
        "La Gioconda",
        1000000,
        date(1503, 1, 1),
        date(2000, 1, 1),
        autor1,
        periodo1,
        sala1
    )

    obra2 = Escultura(
        "Mármol",
        "Renacentista",
        1,
        "La piedad",
        2000000,
        date(1503, 1, 1),
        date(2000, 1, 1),
        autor2,
        periodo1,
        sala1
    )
    # Agregar obra a la sala
    sala1.agregar_obra(obra1)

    # =========================
    # Encargado del catálogo
    # =========================
    encargado = EncargadoCatalogo(
        1,
        "encargado1",
        "1234",
        "Carlos",
        100
    )

    encargado.agregar_obra(catalogo, obra1)
    encargado.agregar_obra(catalogo, obra2)

    print("Obras en catálogo:")
    for obra in catalogo.listar_obras():
        print(obra.titulo)

    # =========================
    # Restaurador jefe
    # =========================
    restaurador = RestauradorJefe(
        2,
        "restaurador1",
        "1234",
        "Ana",
        101
    )

    restaurador.enviar_restauracion(obra1, "Limpieza")

    print("Estado de la obra", obra1.titulo, "es:", obra1.estado)

    restauracion = obra1.restauraciones[0]

    restaurador.finalizar_restauracion(
        restauracion,
        date.today()
    )

    print("Estado de la obra", obra1.titulo, "es:", obra1.estado)

    # =========================
    # Director del museo
    # =========================
    director = DirectorMuseo(
        3,
        "director1",
        "1234",
        "Luis",
        102
    )

    museo_destino = Museo(
        1,
        "Museo de Arte Moderno",
        "Madrid",
        "España"
    )

    director.registrar_cesion(
        obra1,
        museo_destino,
        date.today(),
        date(2026, 12, 31),
        50000
    )

    print("Número de cesiones de", obra1.titulo, ":", len(obra1.cesiones))

    # =========================
    # Visitante consultando catálogo
    # =========================
    visitante = Visitante("Juan", "Pérez")

    obras_catalogo = visitante.consultar_catalogo(catalogo)

    print("Catálogo consultado por visitante:")
    for obra in obras_catalogo:
        print(obra.titulo)


# Ejecutar programa
if __name__ == "__main__":
    main()