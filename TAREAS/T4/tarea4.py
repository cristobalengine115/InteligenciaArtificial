import string, random



def codificar_palabra(frase,clave):
    '''Takes the word to be coded and prints it. Returns nothing'''
    frase= normalizar_cadena(frase)
    tabla_codificacion = []    
    frase_codificada = ''
    for i in range(len(frase)//clave):
        if i==0:
            tabla_codificacion.append(frase[0:clave])
        else:
            tabla_codificacion.append(frase[i*clave:(i*clave)+clave])
    if(len(frase)%clave != 0):
        frase_con_digitos= frase[(len(frase)//clave)*clave:((len(frase)//clave)*clave)+(len(frase)%clave)]
        for i in range(clave-len(frase)%clave): 
            frase_con_digitos+= random.choice(string.ascii_letters).upper()
        tabla_codificacion.append(frase_con_digitos)
    print(tabla_codificacion)
    for j in range(clave):
        for i in range(len(tabla_codificacion)):
            frase_codificada += tabla_codificacion[i][j]
    print(frase_codificada)
   
    
def decodificar_palabra(frase_codif,clave):
    '''Takes the coded word and prints it. Returns None if the coded word is invalid'''
    tabla_decod = []
    frase_decodificada=''
    factor_codif = len(frase_codif)//clave
    for i in range(clave):
        if i==0:
            tabla_decod.append(frase_codif[0:factor_codif])
        else:
            tabla_decod.append(frase_codif[i*factor_codif:(i*factor_codif)+factor_codif])

    print(tabla_decod)
    for j in range(factor_codif):
        for i in range(len(tabla_decod)):
            frase_decodificada += tabla_decod[i][j]
    print(frase_decodificada)
    #return frase_decodificada

def normalizar_cadena(frase):
    '''Takeas a sentence. returns the sentence without spaces and all in uppercase'''
    frase = frase.upper()
    frase = frase.replace(" ","")
    return frase


def main():
    '''Main function that starts the program '''
    while(True):
        print("====================================")
        print("BIENVENIDO AL SISTEMA DECODIFICADOR AGENTE SECRETO")
        print("ESCOGA UNA OPCION")
        print("1.-CODIFICAR MENSAJE")
        print("2.-DECODIFICAR MENSAJE")
        print("3.-SALIR")
        decision = int(input('->'))
        if decision == 1:
            word =  input('INGRESE LA FRASE A CODIFICAR\n-->')
            key = int(input('INGRESE LA CLAVE PARA CODIFICAR\n-->'))
            codificado = codificar_palabra(word,key)  
            if codificado != None:
                print("LA PALABRA CODIFICADA ES: "+codificado)
            else:
                print('LA PALABRA CONTIENE CARACTERES ILEGALES')
        elif decision == 2:
            code = input('INGRESE LA FRASE A DECODIFICAR\n-->')
            key = int(input('INGRESE LA CLAVE PARA DECODIFICAR\n-->'))
            decodificado = decodificar_palabra(code,key)  
            if decodificado != None:
                print("LA PALABRA DECODIFICADA ES: "+decodificado)
            else:
                print("INGRESE UNA PALABRA CODIFICADA VÁLIDA")
        elif decision == 3:
            return
        else:
            print("INGRESE UN VALOR CORRECTO") 
        print("====================================")

main()