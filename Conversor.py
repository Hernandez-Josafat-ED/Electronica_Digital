# =============================================================================
#  CONVERSIONES ENTRE SISTEMAS NUMÉRICOS
#  Materia: Electrónica Digital
#  Descripción: Programa que realiza las 12 conversiones entre sistemas
#               numéricos (Binario, Octal, Decimal, Hexadecimal) mostrando
#               el procedimiento paso a paso.
# =============================================================================

# Diccionario para convertir valor numérico a dígito hexadecimal
HEX_DIGITOS = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

# Diccionario para convertir dígito hexadecimal a valor numérico
HEX_VALORES = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


# =============================================================================
#  FUNCIONES DE VALIDACIÓN
# =============================================================================

def es_binario_valido(numero_str):
    """Verifica que la cadena contenga solo dígitos 0 y 1."""
    return all(c in '01' for c in numero_str) and len(numero_str) > 0


def es_octal_valido(numero_str):
    """Verifica que la cadena contenga solo dígitos del 0 al 7."""
    return all(c in '01234567' for c in numero_str) and len(numero_str) > 0


def es_decimal_valido(numero_str):
    """Verifica que la cadena sea un número entero no negativo."""
    return numero_str.isdigit() and len(numero_str) > 0


def es_hexadecimal_valido(numero_str):
    """Verifica que la cadena contenga solo dígitos hexadecimales válidos."""
    digitos_validos = set('0123456789ABCDEFabcdef')
    return all(c in digitos_validos for c in numero_str) and len(numero_str) > 0


# =============================================================================
#  FUNCIONES DE ENTRADA
# =============================================================================

def pedir_binario():
    """Solicita y valida un número binario al usuario."""
    while True:
        num = input("  Ingresa el número BINARIO: ").strip()
        if es_binario_valido(num):
            return num
        print("  ✗ Entrada inválida. Solo se permiten dígitos 0 y 1.\n")


def pedir_octal():
    """Solicita y valida un número octal al usuario."""
    while True:
        num = input("  Ingresa el número OCTAL: ").strip()
        if es_octal_valido(num):
            return num
        print("  ✗ Entrada inválida. Solo se permiten dígitos del 0 al 7.\n")


def pedir_decimal():
    """Solicita y valida un número decimal al usuario."""
    while True:
        num = input("  Ingresa el número DECIMAL (entero positivo): ").strip()
        if es_decimal_valido(num):
            return int(num)
        print("  ✗ Entrada inválida. Ingresa un número entero positivo.\n")


def pedir_hexadecimal():
    """Solicita y valida un número hexadecimal al usuario."""
    while True:
        num = input("  Ingresa el número HEXADECIMAL: ").strip().upper()
        if es_hexadecimal_valido(num):
            return num
        print("  ✗ Entrada inválida. Solo se permiten 0-9 y letras A-F.\n")


# =============================================================================
#  FUNCIONES AUXILIARES
# =============================================================================

def separador():
    """Imprime una línea separadora decorativa."""
    print("  " + "-" * 54)


def titulo_conversion(origen, destino):
    """Imprime el encabezado de una conversión."""
    print("\n" + "=" * 58)
    print(f"   CONVERSIÓN: {origen.upper()} → {destino.upper()}")
    print("=" * 58)


def valor_hex_a_decimal(digito):
    """
    Convierte un dígito hexadecimal (str) a su valor decimal (int).
    Ejemplo: 'A' -> 10, 'F' -> 15, '7' -> 7
    """
    digito = digito.upper()
    if digito in HEX_VALORES:
        return HEX_VALORES[digito]
    return int(digito)


def decimal_a_hex_digito(valor):
    """
    Convierte un valor decimal (0-15) a su dígito hexadecimal (str).
    Ejemplo: 10 -> 'A', 15 -> 'F', 7 -> '7'
    """
    if valor in HEX_DIGITOS:
        return HEX_DIGITOS[valor]
    return str(valor)


# =============================================================================
#  CONVERSIONES DESDE BINARIO
# =============================================================================

def binario_a_decimal():
    """
    Conversión Binario → Decimal.
    Procedimiento: multiplica cada bit por su potencia de 2 correspondiente
    y suma todos los resultados.
    """
    titulo_conversion("Binario", "Decimal")
    binario = pedir_binario()

    print(f"\n  Número binario: {binario}")
    separador()
    print("  Procedimiento: multiplicar cada bit por 2^(posición)")
    separador()

    n = len(binario)
    suma_total = 0
    terminos = []

    # Recorre cada bit de izquierda a derecha
    for i, bit in enumerate(binario):
        potencia = n - 1 - i          # La potencia disminuye de izquierda a derecha
        valor = int(bit) * (2 ** potencia)
        terminos.append(str(valor))
        print(f"    {bit} × 2^{potencia}  =  {int(bit)} × {2**potencia:>5}  =  {valor}")
        suma_total += valor

    separador()
    print(f"  Suma: {' + '.join(terminos)} = {suma_total}")
    separador()
    print(f"\n  ✔ Resultado: ({binario})₂  =  ({suma_total})₁₀\n")


def binario_a_octal():
    """
    Conversión Binario → Octal.
    Procedimiento: agrupar los bits de 3 en 3 (de derecha a izquierda),
    convertir cada grupo a su dígito octal equivalente.
    """
    titulo_conversion("Binario", "Octal")
    binario = pedir_binario()

    print(f"\n  Número binario: {binario}")
    separador()
    print("  Procedimiento: agrupar bits de 3 en 3 (de derecha a izquierda)")
    separador()

    # Rellenar con ceros a la izquierda para completar grupos de 3
    while len(binario) % 3 != 0:
        binario = '0' + binario

    grupos = [binario[i:i+3] for i in range(0, len(binario), 3)]
    resultado_octal = ""

    print(f"  Binario agrupado: {' | '.join(grupos)}")
    separador()

    for grupo in grupos:
        # Convertir cada grupo de 3 bits a decimal (que es el dígito octal)
        valor = int(grupo[0]) * 4 + int(grupo[1]) * 2 + int(grupo[2]) * 1
        print(f"    [{grupo}]  →  {int(grupo[0])}×4 + {int(grupo[1])}×2 + {int(grupo[2])}×1 = {valor}")
        resultado_octal += str(valor)

    separador()
    print(f"\n  ✔ Resultado: ({binario.replace(' ','')}  )₂  =  ({resultado_octal})₈\n")


def binario_a_hexadecimal():
    """
    Conversión Binario → Hexadecimal.
    Procedimiento: agrupar los bits de 4 en 4 (de derecha a izquierda),
    convertir cada grupo a su dígito hexadecimal equivalente.
    """
    titulo_conversion("Binario", "Hexadecimal")
    binario = pedir_binario()

    print(f"\n  Número binario: {binario}")
    separador()
    print("  Procedimiento: agrupar bits de 4 en 4 (de derecha a izquierda)")
    separador()

    # Rellenar con ceros a la izquierda para completar grupos de 4
    while len(binario) % 4 != 0:
        binario = '0' + binario

    grupos = [binario[i:i+4] for i in range(0, len(binario), 4)]
    resultado_hex = ""

    print(f"  Binario agrupado: {' | '.join(grupos)}")
    separador()

    for grupo in grupos:
        # Convertir el grupo de 4 bits a su valor decimal
        valor = (int(grupo[0]) * 8 + int(grupo[1]) * 4 +
                 int(grupo[2]) * 2 + int(grupo[3]) * 1)
        digito_hex = decimal_a_hex_digito(valor)
        print(f"    [{grupo}]  →  {int(grupo[0])}×8 + {int(grupo[1])}×4 + "
              f"{int(grupo[2])}×2 + {int(grupo[3])}×1 = {valor}  →  {digito_hex}")
        resultado_hex += digito_hex

    separador()
    print(f"\n  ✔ Resultado: ({binario})₂  =  ({resultado_hex})₁₆\n")


# =============================================================================
#  CONVERSIONES DESDE OCTAL
# =============================================================================

def octal_a_binario():
    """
    Conversión Octal → Binario.
    Procedimiento: convertir cada dígito octal a su equivalente en 3 bits.
    """
    titulo_conversion("Octal", "Binario")
    octal = pedir_octal()

    print(f"\n  Número octal: {octal}")
    separador()
    print("  Procedimiento: cada dígito octal se convierte a 3 bits")
    separador()

    # Tabla de equivalencias octal → 3 bits
    tabla_3bits = {
        '0': '000', '1': '001', '2': '010', '3': '011',
        '4': '100', '5': '101', '6': '110', '7': '111'
    }

    resultado_bin = ""
    for digito in octal:
        bits = tabla_3bits[digito]
        print(f"    Dígito  {digito}  →  {bits}")
        resultado_bin += bits

    # Quitar ceros a la izquierda (excepto si el resultado es '0')
    resultado_bin_limpio = resultado_bin.lstrip('0') or '0'

    separador()
    print(f"\n  ✔ Resultado: ({octal})₈  =  ({resultado_bin_limpio})₂\n")


def octal_a_decimal():
    """
    Conversión Octal → Decimal.
    Procedimiento: multiplica cada dígito por su potencia de 8 y suma.
    """
    titulo_conversion("Octal", "Decimal")
    octal = pedir_octal()

    print(f"\n  Número octal: {octal}")
    separador()
    print("  Procedimiento: multiplicar cada dígito por 8^(posición)")
    separador()

    n = len(octal)
    suma_total = 0
    terminos = []

    for i, digito in enumerate(octal):
        potencia = n - 1 - i
        valor = int(digito) * (8 ** potencia)
        terminos.append(str(valor))
        print(f"    {digito} × 8^{potencia}  =  {int(digito)} × {8**potencia:>7}  =  {valor}")
        suma_total += valor

    separador()
    print(f"  Suma: {' + '.join(terminos)} = {suma_total}")
    separador()
    print(f"\n  ✔ Resultado: ({octal})₈  =  ({suma_total})₁₀\n")


def octal_a_hexadecimal():
    """
    Conversión Octal → Hexadecimal.
    Procedimiento intermedio: Octal → Decimal → Hexadecimal.
    Se muestra cada etapa para que quede claro el proceso.
    """
    titulo_conversion("Octal", "Hexadecimal")
    octal = pedir_octal()

    print(f"\n  Número octal: {octal}")
    separador()
    print("  Procedimiento: Octal → Decimal → Hexadecimal (2 pasos)")

    # --- PASO 1: Octal → Decimal ---
    print("\n  [ PASO 1 ]  Octal → Decimal")
    separador()
    print("  Multiplicar cada dígito por 8^(posición)")
    separador()

    n = len(octal)
    decimal = 0
    for i, digito in enumerate(octal):
        potencia = n - 1 - i
        valor = int(digito) * (8 ** potencia)
        print(f"    {digito} × 8^{potencia} = {int(digito)} × {8**potencia:>7} = {valor}")
        decimal += valor

    print(f"\n  Resultado parcial: ({octal})₈  =  ({decimal})₁₀")

    # --- PASO 2: Decimal → Hexadecimal ---
    print("\n  [ PASO 2 ]  Decimal → Hexadecimal")
    separador()
    print("  Dividir entre 16 y leer residuos de abajo hacia arriba")
    separador()

    temp = decimal
    residuos = []

    if temp == 0:
        residuos.append(0)
    else:
        while temp > 0:
            residuo = temp % 16
            cociente = temp // 16
            hex_dig = decimal_a_hex_digito(residuo)
            print(f"    {temp:>6}  ÷  16  =  cociente {cociente:>5},  residuo {residuo} → {hex_dig}")
            residuos.append(hex_dig)
            temp = cociente

    resultado_hex = ''.join(reversed(residuos))
    separador()
    print(f"  Leyendo residuos de abajo hacia arriba: {resultado_hex}")
    separador()
    print(f"\n  ✔ Resultado: ({octal})₈  =  ({resultado_hex})₁₆\n")


# =============================================================================
#  CONVERSIONES DESDE DECIMAL
# =============================================================================

def decimal_a_binario():
    """
    Conversión Decimal → Binario.
    Procedimiento: dividir sucesivamente entre 2, guardar residuos
    y leer de abajo hacia arriba.
    """
    titulo_conversion("Decimal", "Binario")
    decimal = pedir_decimal()

    print(f"\n  Número decimal: {decimal}")
    separador()
    print("  Procedimiento: dividir entre 2 y leer residuos de abajo hacia arriba")
    separador()

    temp = decimal
    residuos = []

    if temp == 0:
        residuos.append('0')
        print(f"    0  ÷  2  =  cociente 0,  residuo 0")
    else:
        while temp > 0:
            residuo = temp % 2
            cociente = temp // 2
            print(f"    {temp:>6}  ÷  2  =  cociente {cociente:>6},  residuo {residuo}")
            residuos.append(str(residuo))
            temp = cociente

    resultado_bin = ''.join(reversed(residuos))
    separador()
    print(f"  Leyendo residuos de abajo hacia arriba: {resultado_bin}")
    separador()
    print(f"\n  ✔ Resultado: ({decimal})₁₀  =  ({resultado_bin})₂\n")


def decimal_a_octal():
    """
    Conversión Decimal → Octal.
    Procedimiento: dividir sucesivamente entre 8, guardar residuos
    y leer de abajo hacia arriba.
    """
    titulo_conversion("Decimal", "Octal")
    decimal = pedir_decimal()

    print(f"\n  Número decimal: {decimal}")
    separador()
    print("  Procedimiento: dividir entre 8 y leer residuos de abajo hacia arriba")
    separador()

    temp = decimal
    residuos = []

    if temp == 0:
        residuos.append('0')
        print(f"    0  ÷  8  =  cociente 0,  residuo 0")
    else:
        while temp > 0:
            residuo = temp % 8
            cociente = temp // 8
            print(f"    {temp:>6}  ÷  8  =  cociente {cociente:>6},  residuo {residuo}")
            residuos.append(str(residuo))
            temp = cociente

    resultado_oct = ''.join(reversed(residuos))
    separador()
    print(f"  Leyendo residuos de abajo hacia arriba: {resultado_oct}")
    separador()
    print(f"\n  ✔ Resultado: ({decimal})₁₀  =  ({resultado_oct})₈\n")


def decimal_a_hexadecimal():
    """
    Conversión Decimal → Hexadecimal.
    Procedimiento: dividir sucesivamente entre 16, convertir residuos
    mayores a 9 en letras (A-F) y leer de abajo hacia arriba.
    """
    titulo_conversion("Decimal", "Hexadecimal")
    decimal = pedir_decimal()

    print(f"\n  Número decimal: {decimal}")
    separador()
    print("  Procedimiento: dividir entre 16 y leer residuos de abajo hacia arriba")
    print("  Nota: 10=A  11=B  12=C  13=D  14=E  15=F")
    separador()

    temp = decimal
    residuos = []

    if temp == 0:
        residuos.append('0')
        print(f"    0  ÷  16  =  cociente 0,  residuo 0 → 0")
    else:
        while temp > 0:
            residuo = temp % 16
            cociente = temp // 16
            hex_dig = decimal_a_hex_digito(residuo)
            print(f"    {temp:>6}  ÷  16  =  cociente {cociente:>5},  residuo {residuo:>2} → {hex_dig}")
            residuos.append(hex_dig)
            temp = cociente

    resultado_hex = ''.join(reversed(residuos))
    separador()
    print(f"  Leyendo residuos de abajo hacia arriba: {resultado_hex}")
    separador()
    print(f"\n  ✔ Resultado: ({decimal})₁₀  =  ({resultado_hex})₁₆\n")


# =============================================================================
#  CONVERSIONES DESDE HEXADECIMAL
# =============================================================================

def hexadecimal_a_binario():
    """
    Conversión Hexadecimal → Binario.
    Procedimiento: cada dígito hexadecimal se convierte a su equivalente
    de 4 bits.
    """
    titulo_conversion("Hexadecimal", "Binario")
    hexadecimal = pedir_hexadecimal()

    print(f"\n  Número hexadecimal: {hexadecimal}")
    separador()
    print("  Procedimiento: cada dígito hexadecimal se convierte a 4 bits")
    separador()

    resultado_bin = ""
    for digito in hexadecimal:
        # Obtener el valor decimal del dígito hex y convertir a 4 bits
        valor = valor_hex_a_decimal(digito)
        bits = format(valor, '04b')   # Formato de 4 bits con ceros a la izquierda
        print(f"    Dígito  {digito.upper()}  (={valor:>2})  →  {bits}")
        resultado_bin += bits

    resultado_bin_limpio = resultado_bin.lstrip('0') or '0'
    separador()
    print(f"\n  ✔ Resultado: ({hexadecimal.upper()})₁₆  =  ({resultado_bin_limpio})₂\n")


def hexadecimal_a_octal():
    """
    Conversión Hexadecimal → Octal.
    Procedimiento intermedio: Hexadecimal → Decimal → Octal.
    Se muestra cada etapa para claridad.
    """
    titulo_conversion("Hexadecimal", "Octal")
    hexadecimal = pedir_hexadecimal()

    print(f"\n  Número hexadecimal: {hexadecimal.upper()}")
    separador()
    print("  Procedimiento: Hexadecimal → Decimal → Octal (2 pasos)")

    # --- PASO 1: Hexadecimal → Decimal ---
    print("\n  [ PASO 1 ]  Hexadecimal → Decimal")
    separador()
    print("  Multiplicar cada dígito por 16^(posición)")
    print("  Nota: A=10  B=11  C=12  D=13  E=14  F=15")
    separador()

    n = len(hexadecimal)
    decimal = 0
    for i, digito in enumerate(hexadecimal.upper()):
        potencia = n - 1 - i
        valor = valor_hex_a_decimal(digito)
        resultado_parcial = valor * (16 ** potencia)
        print(f"    {digito} (={valor:>2}) × 16^{potencia} = {valor} × {16**potencia:>8} = {resultado_parcial}")
        decimal += resultado_parcial

    print(f"\n  Resultado parcial: ({hexadecimal.upper()})₁₆  =  ({decimal})₁₀")

    # --- PASO 2: Decimal → Octal ---
    print("\n  [ PASO 2 ]  Decimal → Octal")
    separador()
    print("  Dividir entre 8 y leer residuos de abajo hacia arriba")
    separador()

    temp = decimal
    residuos = []

    if temp == 0:
        residuos.append('0')
        print(f"    0  ÷  8  =  cociente 0,  residuo 0")
    else:
        while temp > 0:
            residuo = temp % 8
            cociente = temp // 8
            print(f"    {temp:>6}  ÷  8  =  cociente {cociente:>6},  residuo {residuo}")
            residuos.append(str(residuo))
            temp = cociente

    resultado_oct = ''.join(reversed(residuos))
    separador()
    print(f"  Leyendo residuos de abajo hacia arriba: {resultado_oct}")
    separador()
    print(f"\n  ✔ Resultado: ({hexadecimal.upper()})₁₆  =  ({resultado_oct})₈\n")


def hexadecimal_a_decimal():
    """
    Conversión Hexadecimal → Decimal.
    Procedimiento: multiplica cada dígito por su potencia de 16 y suma.
    """
    titulo_conversion("Hexadecimal", "Decimal")
    hexadecimal = pedir_hexadecimal()

    print(f"\n  Número hexadecimal: {hexadecimal.upper()}")
    separador()
    print("  Procedimiento: multiplicar cada dígito por 16^(posición)")
    print("  Nota: A=10  B=11  C=12  D=13  E=14  F=15")
    separador()

    n = len(hexadecimal)
    decimal = 0
    terminos = []

    for i, digito in enumerate(hexadecimal.upper()):
        potencia = n - 1 - i
        valor = valor_hex_a_decimal(digito)
        resultado_parcial = valor * (16 ** potencia)
        terminos.append(str(resultado_parcial))
        print(f"    {digito} (={valor:>2}) × 16^{potencia} = {valor} × {16**potencia:>8} = {resultado_parcial}")
        decimal += resultado_parcial

    separador()
    print(f"  Suma: {' + '.join(terminos)} = {decimal}")
    separador()
    print(f"\n  ✔ Resultado: ({hexadecimal.upper()})₁₆  =  ({decimal})₁₀\n")


# =============================================================================
#  MENÚ PRINCIPAL
# =============================================================================

def mostrar_menu():
    """Muestra el menú principal de conversiones."""
    print("\n" + "=" * 58)
    print("       CONVERSIONES ENTRE SISTEMAS NUMÉRICOS")
    print("             Electrónica Digital")
    print("=" * 58)
    print("   1.  Binario      →  Decimal")
    print("   2.  Binario      →  Octal")
    print("   3.  Binario      →  Hexadecimal")
    print("   4.  Octal        →  Binario")
    print("   5.  Octal        →  Decimal")
    print("   6.  Octal        →  Hexadecimal")
    print("   7.  Decimal      →  Binario")
    print("   8.  Decimal      →  Octal")
    print("   9.  Decimal      →  Hexadecimal")
    print("  10.  Hexadecimal  →  Binario")
    print("  11.  Hexadecimal  →  Octal")
    print("  12.  Hexadecimal  →  Decimal")
    print("  13.  Salir")
    print("=" * 58)


def ejecutar_opcion(opcion):
    """Ejecuta la función de conversión correspondiente a la opción elegida."""
    opciones = {
        '1':  binario_a_decimal,
        '2':  binario_a_octal,
        '3':  binario_a_hexadecimal,
        '4':  octal_a_binario,
        '5':  octal_a_decimal,
        '6':  octal_a_hexadecimal,
        '7':  decimal_a_binario,
        '8':  decimal_a_octal,
        '9':  decimal_a_hexadecimal,
        '10': hexadecimal_a_binario,
        '11': hexadecimal_a_octal,
        '12': hexadecimal_a_decimal,
    }

    if opcion in opciones:
        opciones[opcion]()   # Llama a la función de conversión correspondiente
        input("  Presiona ENTER para volver al menú...")
    elif opcion == '13':
        print("\n  ¡Hasta luego! Programa cerrado.\n")
        return False          # Señal para salir del bucle principal
    else:
        print("\n  ✗ Opción inválida. Elige un número del 1 al 13.\n")
        input("  Presiona ENTER para continuar...")

    return True               # Señal para continuar en el menú


def main():
    """Función principal: controla el flujo del programa."""
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("\n  Elige una opción (1-13): ").strip()
        continuar = ejecutar_opcion(opcion)


# =============================================================================
#  PUNTO DE ENTRADA
# =============================================================================

if __name__ == "__main__":
    main()