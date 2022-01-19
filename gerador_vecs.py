arquivo = open("comando_vec.txt", "a")
frases = list()

# Variaveis Especificas
numero_exemlos = 5000
dimensoes = 24
numero_imagens = 140

# Transformando variaveis em strings
numero_exemlos_str = str(numero_exemlos)
dimensoes_str = str(dimensoes)


var1 = "opencv_createsamples -info positivas"
var2 = "/positivas.lst -num "
var3 = " -w "
var4 = " -h "
var5 = " -vec vetor"
var6 = ".vec"


contador = 1

while (contador <= numero_imagens):
    contador_str = str(contador)

    if contador < numero_imagens:
        imprimir = var1 + contador_str + var2 + numero_exemlos_str + var3 + \
            dimensoes_str + var4 + dimensoes_str + var5 + contador_str + var6 + " && "
    else:
        imprimir = var1 + contador_str + var2 + numero_exemlos_str + var3 + \
            dimensoes_str + var4 + dimensoes_str + var5 + contador_str + var6
    frases.append(imprimir)
    contador = contador + 1


arquivo.writelines(frases)

# O comando na pasta positivas
