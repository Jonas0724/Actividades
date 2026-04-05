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
    

# ================================
# PRUEBA DE CONSOLA
# ================================

def menu():
    print("\n--- SISTEMA DEL MUSEO ---")
    print("1. Agregar escultura")
    print("2. Listar obras del catálogo")
    print("3. Consultar valor total de obras")
    print("4. Enviar obra a restauración")
    print("5. Salir")


def main():

    # Crear catálogo
    catalogo = Catalogo()

    # Crear sala
    sala1 = Sala(1, "Sala principal", 1)

    # Crear autor y periodo de prueba
    autor1 = Autor(1, "Autor desconocido", "Italia", "1500")
    periodo1 = Periodo("Renacimiento", "1400", "1600")

    # Crear usuarios del sistema
    director = DirectorMuseo(1, "director", "123", "Carlos", "EMP01")
    restaurador = RestauradorJefe(2, "restaurador", "123", "Ana", "EMP02")
    catalogador = EncargadoCatalogo(3, "catalogo", "123", "Luis", "EMP03")

    lista_usuarios = [director, restaurador, catalogador]

    # LOGIN
    usuario_actual = None

    while usuario_actual is None:
        usuario_actual = login(lista_usuarios)

    # MENÚ PRINCIPAL
    while True:

        menu()
        opcion = input("Seleccione una opción: ")

        # AGREGAR ESCULTURA
        if opcion == "1":

            if isinstance(usuario_actual, EncargadoCatalogo):

                id_obra = int(input("ID obra: "))
                titulo = input("Título: ")
                valor = float(input("Valor económico: "))
                material = input("Material: ")
                estilo = input("Estilo: ")

                escultura = Escultura(
                    material,
                    estilo,
                    id_obra,
                    titulo,
                    valor,
                    "1500",
                    "2024",
                    autor1,
                    periodo1,
                    sala1
                )

                usuario_actual.agregar_obra(catalogo, escultura)
                sala1.agregar_obra(escultura)

                print("Escultura agregada al catálogo")

            else:
                print("No tienes permiso para agregar obras")

        # LISTAR OBRAS
        elif opcion == "2":

            obras = catalogo.listar_obras()

            if not obras:
                print("No hay obras en el catálogo")

            for obra in obras:
                print(f"ID: {obra.id_obra} - {obra.titulo} - ${obra.valor_economico}")

        # VALOR TOTAL
        elif opcion == "3":

            if isinstance(usuario_actual, DirectorMuseo):

                total = usuario_actual.consultar_valor_total_obras(catalogo)
                print(f"Valor total del museo: ${total}")

            else:
                print("Solo el director puede consultar esto")

        # RESTAURACIÓN
        elif opcion == "4":

            if isinstance(usuario_actual, RestauradorJefe):

                id_obra = int(input("Ingrese ID de obra: "))
                obra = catalogo.buscar_obra(id_obra)

                if obra:

                    tipo = input("Tipo de restauración: ")
                    usuario_actual.enviar_restauracion(obra, tipo)

                else:
                    print("Obra no encontrada")

            else:
                print("No tienes permiso")

        # SALIR
        elif opcion == "5":

            usuario_actual.cerrar_sesion()
            print("Fin del programa")
            break

        else:
            print("Opción inválida")


# Ejecutar programa
if __name__ == "__main__":
    main()
