def identificar_cuadrilatero(lados):
    lados.sort()
    
    if lados[0] == lados[1] == lados[2] == lados[3]:
        return "Cuadrado"
    elif lados[0] == lados[1] and lados[2] == lados[3]:
        return "Rectángulo"
    else:
        return "Otro cuadrilátero"

lados = []
for i in range(4):
    lado = float(input(f"Ingresa la longitud del lado {i+1}: "))
    lados.append(lado)

tipo = identificar_cuadrilatero(lados)
print(f"Es un {tipo}.")


