# Cajero automático

Programa de consola en Python que simula operaciones básicas de un cajero automático.

## Funcionalidades

- Consultar saldo, depositar y retirar dinero.
- Menú que permanece activo con `while` hasta que el usuario elige salir.
- Opciones controladas con `if`, `elif` y `else`.
- Validación de montos, control de saldo suficiente y actualización acumulativa.
- Acceso con PIN (tres intentos por selección de usuario).
- Registro de depósitos y retiros, y opción para consultar el historial.
- Dos usuarios de prueba con PIN y movimientos independientes.

## Ejecuta

```bash
python3 main.py
```

En Windows también se puede ejecutar con `py main.py`.

## Prueba Realizada con el Programa

| Usuario | PIN | Saldo inicial |
|---|---|---|
| Ana (1) | 1234 | B/. 1000.00 |
| Luis (2) | 5678 | B/. 750.00 |

## Archivos

- `main.py`: código del cajero.
- `README.md`: guía para ejecutar programa.
