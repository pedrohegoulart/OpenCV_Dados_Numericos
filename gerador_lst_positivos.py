arquivo = open("comando_lst.txt", "a")
frases = list()

# Informações especificas
prefixo_img = "cubo_numerico_"
dimensao = 48
numero_exemplos = 36
numero_imagens = 140


var1 = "opencv_createsamples -img "
var2 = ".png -bg ../negativas/bg.txt -info positivas"
var3 = "/positivas.lst -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -w "
var4 = " -h "
var5 = " -num "
var6 = " -bgcolor 255 -bgthresh 8"

contador = 1

dimensao_str = str(dimensao)
numero_exemplos_str = str(numero_exemplos)

while (contador <= (numero_imagens)):
    contador_str = str(contador)

    if contador < numero_imagens:
        imprimir = var1 + prefixo_img + contador_str + var2 + contador_str + var3 + \
            dimensao_str + var4 + dimensao_str + var5 + numero_exemplos_str + var6 + " && "
    else:
        imprimir = var1 + prefixo_img + contador_str + var2 + contador_str + var3 + \
            dimensao_str + var4 + dimensao_str + var5 + numero_exemplos_str + var6

    frases.append(imprimir)
    contador = contador + 1


arquivo.writelines(frases)

# O codigo deve ser rodado dentro da pasta positivo
