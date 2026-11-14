"""Simulador de cajero automático para practicar Python en consola."""

from decimal import Decimal, InvalidOperation


# Cuentas de ejemplo para probar el cajero.
# Los saldos y movimientos se mantienen durante esta ejecución.
usuarios = {
    "1": {"nombre": "Ana", "pin": "1234", "saldo": Decimal("1000.00"), "movimientos": []},
    "2": {"nombre": "Luis", "pin": "5678", "saldo": Decimal("750.00"), "movimientos": []},
}


def mostrar_dinero(cantidad):
    return f"B/. {cantidad:.2f}"


def iniciar_sesion():
    print("\n=== BIENVENIDO AL CAJERO ===")
    print("Usuarios de prueba: 1. Ana | 2. Luis")
    print("PIN de prueba: Ana 1234 | Luis 5678")

    while True:
        numero = input("Elegí un usuario (1 o 2), o 0 para salir: ").strip()
        if numero == "0":
            return None
        if numero not in usuarios:
            print("Elegí un usuario de la lista.")
            continue

        usuario = usuarios[numero]
        for intento in range(1, 4):
            pin = input("Ingresá el PIN: ").strip()
            if pin == usuario["pin"]:
                print(f"\n¡Bienvenido, {usuario['nombre']}!")
                return usuario
            print(f"PIN incorrecto. Intento {intento} de 3.")
        print("Se agotaron los intentos. Elegí un usuario para volver a empezar.")


def pedir_monto():
    while True:
        texto = input("Ingresá el monto (o 0 para cancelar): ").strip().replace(",", ".")
        try:
            monto = Decimal(texto)
        except InvalidOperation:
            print("Escribí un monto válido, por ejemplo 25.50.")
            continue
        if not monto.is_finite():
            print("Ingresá un monto válido.")
        elif monto == 0:
            return None
        elif monto < 0 or monto != monto.quantize(Decimal("0.01")):
            print("Ingresá un monto positivo con hasta dos decimales.")
        else:
            return monto


def consultar_saldo(usuario):
    print(f"Tu saldo actual es {mostrar_dinero(usuario['saldo'])}.")


def depositar(usuario):
    monto = pedir_monto()
    if monto is None:
        print("Operación cancelada.")
        return
    usuario["saldo"] += monto
    usuario["movimientos"].append(("Depósito", monto, usuario["saldo"]))
    print(f"Depósito realizado. Saldo actual: {mostrar_dinero(usuario['saldo'])}.")


def retirar(usuario):
    monto = pedir_monto()
    if monto is None:
        print("Operación cancelada.")
        return
    if monto > usuario["saldo"]:
        print("Saldo insuficiente para realizar el retiro.")
        return
    usuario["saldo"] -= monto
    usuario["movimientos"].append(("Retiro", monto, usuario["saldo"]))
    print(f"Retiro realizado. Saldo actual: {mostrar_dinero(usuario['saldo'])}.")


def ver_historial(usuario):
    print("\n--- HISTORIAL DE MOVIMIENTOS ---")
    if not usuario["movimientos"]:
        print("Todavía no hay depósitos ni retiros registrados.")
        return
    for numero, (tipo, monto, saldo) in enumerate(usuario["movimientos"], start=1):
        print(f"{numero}. {tipo}: {mostrar_dinero(monto)} | Saldo: {mostrar_dinero(saldo)}")


# ESPACIO PARA EL COMPAÑERO 1:
# Puede mejorar los mensajes, la presentación del menú o añadir un resumen.
# El cajero ya funciona con las opciones que aparecen a continuación.


# ESPACIO PARA EL COMPAÑERO 2:
# Puede crear una búsqueda de movimientos o un reporte final por usuario.
# Los movimientos ya se guardan por separado para cada cuenta.


def usar_cajero(usuario):
    opcion = ""
    while opcion != "6":
        print("\n================================")
        print("        MENÚ DEL CAJERO")
        print("================================")
        print(f"Usuario: {usuario['nombre']}")
        print(f"Saldo actual: {mostrar_dinero(usuario['saldo'])}")
        print("================================")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Ver historial")
        print("5. Cambiar de usuario")
        print("6. Salir")
        opcion = input("Seleccioná una opción: ").strip()

        if opcion == "1":
            consultar_saldo(usuario)
        elif opcion == "2":
            depositar(usuario)
        elif opcion == "3":
            retirar(usuario)
        elif opcion == "4":
            ver_historial(usuario)
        elif opcion == "5":
            print("Cerrando esta sesión...")
            return True
        elif opcion == "6":
            print("¡Gracias por utilizar nuestro cajero!")
            return False
        else:
            print("Opción no válida. Por favor, selecciona un número del 1 al 6.")
    return False


def main():
    while True:
        usuario = iniciar_sesion()
        if usuario is None:
            print("¡Hasta luego!")
            break
        if not usar_cajero(usuario):
            break


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nSesión finalizada.")
