import string


def dectofloat(dec):
    '''Converts decimal part to binary'''
    if(dec<0):
        signo=str(1)
    else:
        signo=str(0)
    decs=str(dec)
    res=decs.split(".")
    modulos1 = [] # la lista para guardar los bits
    numero_decimal = int(res[0])
    res[1]="0."+ res[1]
    while numero_decimal != 0: 
        modulos1.append(str(numero_decimal % 2))
        numero_decimal //= 2
    partint=""
    for bit in modulos1:
        partint+=bit
    partint=partint[::-1]
    numero_fraccionario = float(res[1])
    modulos2 = []
    while numero_fraccionario > 0:
        numero_fraccionario = numero_fraccionario*2
        flag=str(numero_fraccionario)
        res2=flag.split(".")
        modulos2.append(res2[0])
        flag2="0."+res2[1]
        numero_fraccionario=float(flag2)
    partfrac=""
    for frac in modulos2:
        partfrac+=frac
    mantisa=partint[1:]+partfrac
    exp=int(len(partint)-1+127)
    modulos3=[]
    while exp != 0: 
        modulos3.append(str(exp % 2))
        exp //= 2 
    exponente=""
    for b in modulos3:
        exponente+=b
    exponente=exponente[::-1]
    resultado=signo+exponente+mantisa
    while len(resultado) < 32:
        resultado+="0"
    return resultado



def floattodec(bit):
    '''Converts decimal part to binary'''
    s=int(bit[0])
    n=bit[1:9]
    exp=binario_a_decimal(n)
    mantisa=bit[9:32]
    contador=1
    suma=0
    for i in range(len(mantisa)):
        contador=contador*2
        if mantisa[i]=="1":
            suma=suma+1/(contador)
    suma=suma+1
    d=((-1)**s)*(2**(exp-127))*suma
    print(d)


def binario_a_decimal(binario):
    '''Transforms binary to decimal'''
    posicion = 0
    decimal = 0
    binario = binario[::-1]
    for digito in binario:
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal

#dectofloat(9.625)
# floattodec("01000001000110100000000000000000")


def main():
    '''Main function that starts the program '''
    while(True):
        print("==================================================   ")
        print("BIENVENIDO AL SISTEMA CONVERSIÓN DE NÚMEROS BINARIOS")
        print("ESCOGA UNA OPCION")
        print("1.-PASAR DE FLOTANTE A BINARIO")
        print("2.-PASAR DE BINARIO A FLOTANTE")
        print("3.-SALIR")
        decision = int(input('->'))
        if decision == 1:
            print("INGRESE EL NÚMERO DECIMAL CON PARTE FRACCIONARIA")
            print("LA PARTE FRACCIONARIA DEBEN SER SUMAS DE 2^(-N), POR EJEMPLO .625")
            flotante=float(input("->"))
            resultado=dectofloat(flotante)
            print("RESULTADO: "+resultado)
        elif decision == 2:
            print("INGRESE LOS 32 BITS")
            bits=str(input("->"))
            resultado=str(floattodec(bits))
            print("RESULTADO: "+resultado)
        elif decision == 3:
            return
        else:
            print("INGRESE UN VALOR CORRECTO") 
        print("==================================================\n")

main()
