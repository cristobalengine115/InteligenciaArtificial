import math

# VALOR EN UN PUNTO
def valor_punto_pol(polinomio,grado):
    valor = 0
    point = int(input('INGRESE EL PUNTO A EVALUAR LOS POLINOMIOS'))
    for i in range(grado):
        valor += polinomio[i] * (point ** (grado-i))
    return valor

# SUMA
def convertir_polinomio(polinomio1,polinomio2,grado1,grado2):
    aux=[]
    if grado1 == grado2:
        pass
    elif grado1 > grado2:
        num = grado1-grado2
        for i in range(num):
            aux.append(0)
        polinomio2 = aux + polinomio2
    else:
        num = grado2-grado1
        for i in range(num):
            aux.append(0)
        polinomio1 = aux + polinomio1
    return polinomio1,polinomio2,grado1,grado2
def suma_polinomio(polinomio1,polinomio2):
    suma=[]
    for i in range(len(polinomio1)):
        suma.append(polinomio1[i]+polinomio2[i])
    print(suma)
# RESTA
def resta_polinomio(polinomio1,polinomio2):
    resta=[]
    for i in range(len(polinomio1)):
        resta.append(polinomio1[i]-polinomio2[i])
    print(resta)

# MULTIPLICACION
# DERIVADA
# INTEGRAL



def suma_vectores(dim,vec1,vec2):
    sumaVec = []
    for i in range(dim):
        sumaVec.append(vec1[i]+vec2[i])
    return sumaVec

def resta_vectores(dim,vec1,vec2):
    restaVec = []
    for i in range(dim):
        restaVec.append(vec1[i]-vec2[i])
    return restaVec

def escalar_vec(dim,vec,escalar):
    escalarVec = []
    for i in range(dim):
        escalarVec.append(vec[i]* escalar)
    return escalarVec

def norma_vec(dim,vec1,vec2):
    norma = 0
    for i in range(dim):
        norma += (vec2[i]-vec1[i]) ** 2
    norma = math.sqrt(norma)
    return norma

def angulo_vec(dim,vec1,vec2):
    resMult=0
    mod1=0
    mod2 = 0
    for i in range(dim):
        resMult += vec1[i]*vec2[i]
        mod1 += vec1[i]**2
        mod2 +=vec2[i]**2
    mod=math.sqrt(mod1)*math.sqrt(mod2)
    alfa=resMult/mod
    anguloRad=math.acos(alfa)
    anguloGrad=anguloRad*(180/math.pi)
    return anguloRad, anguloGrad


def operaciones_vectores():
    ## VECTORES DE N-DIMENSIONES
    print("")
    dim = int(input('INGRESE LAS DIMENSIONES DE LOS VECTORES: '))
    vec1 = []
    print('INGRESE '+str(dim)+' VALORES PARA EL VECTOR 1')
    for i in range(dim):
        x = int(input('->'))
        vec1.append(x)
    vec2 = []
    print('INGRESE '+str(dim)+' VALORES PARA EL VECTOR 2')
    for i in range(dim):
        x = int(input('->'))
        vec2.append(x)


    escalar = int(input('INGRESE EL ESCALAR AL QUE QUIERE MULTIPLICAR EL VECTOR'))

    ##OPERACIONES SOLICITADAS PARA VECTORES
    print("La suma es:"+str(suma_vectores(dim,vec1,vec2)))
    print("La resta es:"+str(resta_vectores(dim,vec1,vec2)))
    print("El escalar del vector 1 es:"+str(escalar_vec(dim,vec1,escalar)))
    print("El escalar del vector 2 es:"+str(escalar_vec(dim,vec2,escalar)))
    print("La norma es:"+str(norma_vec(dim,vec1,vec2)))
    anguloRad, anguloGrad = angulo_vec(dim,vec1,vec2)
    print("El angulo en radianes es:"+str(anguloRad))
    print("El angulo en grados es:"+str(anguloGrad))



def operaciones_polinomio():
    ## POLINOMIOS GRADO N
    grado1 = int(input('INGRESE EL GRADO DEL POLINOMIO 1: '))
    grado2 = int(input('INGRESE EL GRADO DEL POLINOMIO 2: '))
    #grado1 = grado1+1
    #grado2 = grado2+1
    polinomio1 = []
    polinomio2 = []

    print('INGRESE LOS VALORES PARA EL POLINOMIO 1')
    for i in range(grado1+1):
        x = int(input('x^' +str(grado1-i) +' -> '))
        polinomio1.append(x)

    print('INGRESE LOS VALORES PARA EL POLINOMIO 2')
    for i in range(grado2+1):
        x = int(input('x^' +str(grado2-i) +' -> '))
        polinomio2.append(x)


    polinomio1,polinomio2,grado1,grado2 = convertir_polinomio(polinomio1,polinomio2,grado1,grado2,)


    ##OPERACIONES SOLICITADAS PARA POLINOMIOS
    print("El valor en un punto para el polinomio 1 es:"+str(valor_punto_pol(polinomio1,grado1)))
    print("El valor en un punto para el polinomio 1 es:"+str(valor_punto_pol(polinomio2,grado2)))
    print("La suma es:"+str(suma_polinomio(polinomio1,polinomio2)))
    print("La resta es:"+str(resta_polinomio(polinomio1,polinomio2)))
    # print("La multiplicación es:"+str(escalar_vec(dim,vec1,escalar)))
    # print("La derivada es:"+str(escalar_vec(dim,vec2,escalar)))
    # print("La integral es:"+str(norma_vec(dim,vec1,vec2)))
















# operaciones_vectores()
operaciones_polinomio()