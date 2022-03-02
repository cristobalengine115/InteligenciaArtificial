import string, random

def codificar_palabra(frase,clave):
    '''Takes the phrase to be coded, transforms it to the coded table and returns the frase coded. Returns coded phrase'''
    frase= normalizar_cadena(frase)
    if(validar_key(frase,clave) == None):
        return None
    tabla_codificacion = []    
    frase_codificada = ''
    valores_completos = len(frase)//clave
    extra_val = len(frase)%clave
    for i in range(valores_completos):
        if i==0:
            tabla_codificacion.append(frase[0:clave])
        else:
            tabla_codificacion.append(frase[i*clave:(i*clave)+clave])
    if(extra_val != 0):
        frase_con_digitos= frase[(valores_completos)*clave:((valores_completos)*clave)+(extra_val)]
        for i in range(clave-extra_val): 
            frase_con_digitos+= random.choice(string.ascii_letters).upper()
        tabla_codificacion.append(frase_con_digitos)
    #print(tabla_codificacion)
    for j in range(clave):
        for i in range(len(tabla_codificacion)):
            frase_codificada += tabla_codificacion[i][j]
    return(frase_codificada)
   
    
def decodificar_palabra(frase_codif,clave):
    '''Takes the coded phrase, decodes the table and retruns it decoded. Returns None if the key is invalid'''
    tabla_decod = []
    frase_decodificada=''
    if(validar_key(frase_codif,clave) == None):
        return None
    factor_codif = len(frase_codif)//clave
    for i in range(clave):
        if i==0:
            tabla_decod.append(frase_codif[0:factor_codif])
        else:
            tabla_decod.append(frase_codif[i*factor_codif:(i*factor_codif)+factor_codif])
    #print(tabla_decod)
    for j in range(factor_codif):
        for i in range(len(tabla_decod)):
            frase_decodificada += tabla_decod[i][j]
    #print(frase_decodificada)
    return frase_decodificada

def normalizar_cadena(frase):
    '''Takeas a sentence. returns the sentence without spaces and all in uppercase'''
    frase = frase.upper()
    frase = frase.replace(" ","")
    return frase

def validar_key(frase,key):
    """Validates if the key is above one and is not under the length of the phrase to be coded // uncoded"""
    if(len(frase) <= key or len(frase) == 0 or key <=1):
        return None
    else:
        return True

def main():
    '''Main function that starts the program '''
    while(True):
        print("==================================================   ")
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
                print("LA FRASE CODIFICADA ES: "+codificado)
            else:
                print('LA FRASE NO SE PUDO CODIFICAR, VERIFIQUE SU CLAVE')
        elif decision == 2:
            code = input('INGRESE LA FRASE A DECODIFICAR\n-->')
            key = int(input('INGRESE LA CLAVE PARA DECODIFICAR\n-->'))
            decodificado = decodificar_palabra(code,key)  
            if decodificado != None:
                print("LA FRASE DECODIFICADA ES: "+decodificado)
            else:
                print("LA FRASE NO SE PUDO CODIFICAR, VERIFIQUE SU CLAVE")
        elif decision == 3:
            return
        else:
            print("INGRESE UN VALOR CORRECTO") 
        print("==================================================")

main()