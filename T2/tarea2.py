def codificar_letra(letra):
    if letra == 'A':
        return '90'
    elif letra == 'B':
        return '91'
    elif letra == 'C':
        return '92'
    elif letra == 'D':
        return '93'
    elif letra == 'E':
        return '94'
    elif letra == 'F':
        return '80'
    elif letra == 'G':
        return '81'
    elif letra == 'H':
        return '82'
    elif letra == 'I' or letra == 'J':
        return '83'
    elif letra == 'K':
        return '84'
    elif letra == 'L':
        return '70'
    elif letra == 'M':
        return '71'
    elif letra == 'N':
        return '72'
    elif letra == 'O':
        return '73'
    elif letra == 'P':
        return '74'
    elif letra == 'Q':
        return '60'
    elif letra == 'R':
        return '61'
    elif letra == 'S':
        return '62'
    elif letra == 'T':
        return '63'
    elif letra == 'U':
        return '64'
    elif letra == 'V':
        return '50'
    elif letra == 'W':
        return '51'
    elif letra == 'X':
        return '52'
    elif letra == 'Y':
        return '53'
    elif letra == 'Z':
        return '54'

def decodificar_letra(par_num):
    if par_num == '90':
        return 'A'
    elif par_num == '91':
        return 'B'
    elif par_num == '92':
        return 'C'
    elif par_num == '93':
        return 'D'
    elif par_num == '94':
        return 'E'
    elif par_num == '80':
        return 'F'
    elif par_num == '81':
        return 'G'
    elif par_num == '82':
        return 'H'
    elif par_num == '83':
        return 'I'
    elif par_num == '84':
        return 'K'
    elif par_num == '70':
        return 'L'
    elif par_num == '71':
        return 'M'
    elif par_num == '72':
        return 'N'
    elif par_num == '73':
        return 'O'
    elif par_num == '74':
        return 'P'
    elif par_num == '60':
        return 'Q'
    elif par_num == '61':
        return 'R'
    elif par_num == '62':
        return 'S'
    elif par_num == '63':
        return 'T'
    elif par_num == '64':
        return 'U'
    elif par_num == '50':
        return 'V'
    elif par_num == '51':
        return 'W'
    elif par_num == '52':
        return 'X'
    elif par_num == '53':
        return 'Y'
    elif par_num == '54':
        return 'Z'
    else:
        return None

def codificar_palabra(palabra):
    palabra_codificada = ''
    for i in range(len(palabra)):
        if(codificar_letra(palabra[i]) != None):
            palabra_codificada += codificar_letra(palabra[i])
        else:
            print('LA PALABRA CONTIENE CARACTERES ILEGALES')
            return None
    print("LA PALABRA CODIFICADA ES: "+palabra_codificada)

def decodificar_palabra(code):
    if(not(code.isnumeric() and len(code)%2 == 0)):
        print("INGRESE UNA PALABRA CODIFICADA VÁLIDA")
        return None
    palabra_decodificada = ''
    for i in range(len(code)):
        if(i%2 == 0):
            if(decodificar_letra(code[i:i+2]) == None):
                print("LA PALABRA NO SE PUDO DECODIFICAR")
                return None
            else:
                palabra_decodificada += str(decodificar_letra(code[i:i+2]))
        else:
            pass
    print("LA PALABRA DECODIFICADA ES: "+palabra_decodificada)

def normalizar_cadena(palabra):
    palabra = palabra.upper()
    palabra = palabra.replace(" ","")
    return palabra


def main():
    print("BIENVENIDO AL SISTEMA DECODIFICADOR")
    print("ESCOGA UNA OPCION")
    print("1.-CODIFICAR MENSAJE")
    print("2.-DECODIFICAR MENSAJE")
    decision = int(input('->'))
    if decision == 1:
        word =  input('INGRESE LA FRASE A CODIFICAR\n-->')
        codificar_palabra(normalizar_cadena(word))
    elif decision == 2:
        code = input('INGRESE LA FRASE A DECODIFICAR\n-->')
        decodificar_palabra(code)    
    else:
        print("INGRESE UN VALOR CORRECTO") 

main()