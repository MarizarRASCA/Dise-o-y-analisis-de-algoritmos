UNIDADES = ["", "UN", "DOS", "TRES", "CUATRO", "CINCO", "SEIS", "SIETE", "OCHO", "NUEVE"]
DECENAS = ["", "DIEZ", "VEINTE", "TREINTA", "CUARENTA", "CINCUENTA", "SESENTA", "SETENTA", "OCHENTA", "NOVENTA"]
ESPECIALES = ["", "ONCE", "DOCE", "TRECE", "CATORCE", "QUINCE", "DIECISEIS", "DIECISIETE", "DIECIOCHO", "DIECINUEVE"]
CENTENAS = ["", "CIENTO", "DOSCIENTOS", "TRESCIENTOS", "CUATROCIENTOS", "QUINIENTOS", "SEISCIENTOS", "SETECIENTOS", "OCHOCIENTOS", "NOVECIENTOS"]

MILES = ["", " MIL", " MILLON", " MIL MILLONES", " BILLON", " MIL BILLONES", " TRILLON"]

def convertir_a_letras(numero):
    numero = int(numero)
    if numero == 0:
        return "CERO"

    resultado = ""
    i = 0

    while numero > 0:
        grupo = numero % 1000
        if grupo:
            resultado = f"{convertir_grupo(grupo)}{MILES[i]}{resultado}"
        numero //= 1000
        i += 1

    return resultado.strip()

def convertir_grupo(grupo):
    centena, decena, unidad = grupo // 100, (grupo % 100) // 10, grupo % 10
    resultado = f"{CENTENAS[centena]}{DECENAS[decena]}{UNIDADES[unidad]}"
    return resultado.strip()

# Ejemplo de uso
numero = input("Ingrese un número: ")
letras = convertir_a_letras(numero)
print(f"El número {numero} en letras es: {letras}")
