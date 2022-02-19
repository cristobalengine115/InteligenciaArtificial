def normalizar_cadena(palabra):
    palabra = palabra.upper()
    palabra = palabra.replace(" ","")
    return palabra

def codificar_letra(letra):
    if letra == 'A':
        return '09'
    elif letra == 'B':
        return '19'
    elif letra == 'C':
        return '29'
    elif letra == 'D':
        return '39'
    elif letra == 'E':
        return '49'
    elif letra == 'F':
        return '08'
    elif letra == 'G':
        return '18'
    elif letra == 'H':
        return '28'
    elif letra == 'I' or letra == 'J':
        return '38'
    elif letra == 'K':
        return '48'
    elif letra == 'L':
        return '07'
    elif letra == 'M':
        return '17'
    elif letra == 'N':
        return '27'
    elif letra == 'O':
        return '37'
    elif letra == 'P':
        return '47'
    elif letra == 'Q':
        return '06'
    elif letra == 'R':
        return '16'
    elif letra == 'S':
        return '26'
    elif letra == 'T':
        return '36'
    elif letra == 'U':
        return '46'
    elif letra == 'V':
        return '05'
    elif letra == 'W':
        return '15'
    elif letra == 'X':
        return '25'
    elif letra == 'Y':
        return '35'
    elif letra == 'Z':
        return '45'

def decodificar_letra():
    if letra == '09':
        return 'A'
    elif letra == '19':
        return 'B'
    elif letra == '29':
        return 'C'
    elif letra == '39':
        return 'D'
    elif letra == '49':
        return 'E'
    elif letra == '08':
        return 'F'
    elif letra == '18':
        return 'G'
    elif letra == '28':
        return 'H'
    elif letra == '38':
        return 'I'
    elif letra == '48':
        return 'K'
    elif letra == '07':
        return 'L'
    elif letra == '17':
        return 'M'
    elif letra == '27':
        return 'N'
    elif letra == '37':
        return 'O'
    elif letra == '47':
        return 'P'
    elif letra == '06':
        return 'Q'
    elif letra == '16':
        return 'R'
    elif letra == '26':
        return 'S'
    elif letra == '36':
        return 'T'
    elif letra == '46':
        return 'U'
    elif letra == '05':
        return 'V'
    elif letra == '15':
        return 'W'
    elif letra == '25':
        return 'X'
    elif letra == '35':
        return 'Y'
    elif letra == '45':
        return 'Z'

def codificar_palabra(palabra):
    palabra_codificada = ''
    palabra_limpia = normalizar_cadena(palabra)
    for i in range(len(palabra)):
        palabra_codificada += codificar_letra(palabra[i])
    print("LA PALABRA CODIFICADA ES: "+palabra_codificada)


def main():
    print("BIENVENIDO AL SISTEMA DECODIFICADOR")
    print("ESCOGA UNA OPCION")
    print("1.-CODIFICAR MENSAJE")
    print("2.-DECODIFICAR MENSAJE")
    desicion = int(input('->'))
    if desicion == 1:
        
    elif desicion == 2:

    else:
        print("INGRESE UN VALOR CORRECTO") 