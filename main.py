
def concaternar(linea):
    elementos = linea.split(";")
    conComa = elementos[1] + ","
    listaDeNumeros.append(conComa)


listaDeNumeros = []
###MAIN###
try:
    with open("entrada.csv", "r") as f:
        for line in f:
            concaternar(line)
except OSError:
    print("Error al abrir el archivo")
    exit()

with open("salida.txt", "w") as f:
    for numero in listaDeNumeros:
        f.write(numero + ",")