import math
import csv

######## Operaciones para archivo ########
def leer_archivo():
	documento = []
	dim=[]
	vector1=[]
	vector2=[]
	escalar=0
	grad1= 0
	grad2= 0
	poli1=[]
	poli2=[]
	pnt=0
	with open('datos.csv', newline='') as File:
		reader = csv.reader(File)
		for row in reader:
			documento.append(row)
	vector1 = list(map(int,documento[0]))
	vector2 = list(map(int,documento[1]))
	escalar=int(''.join(documento[2]))
	poli1 = list(map(int,documento[3]))
	poli2 = list(map(int,documento[4]))
	pnt = int(''.join(documento[5]))
	dim = valida_dimension(vector1,vector2)
	grad1 = valida_grado(poli1)
	grad2 = valida_grado(poli2)
	return dim,vector1,vector2,escalar,grad1,grad2,poli1,poli2,pnt

def valida_dimension(vector1, vector2):
    dim1 = len(vector1)
    dim2 = len(vector2)
    if dim1 == dim2:
        return dim1
    else:
        return None

def valida_grado(polinomio):
    return len(polinomio)-1


######## Polinomios ########

# Valor en un punto
def valor_punto_pol(polinomio,grado,point):
    valor = 0
    polinomio_to_val = []
    for i in range(len(polinomio)):
        if (polinomio[i]==0 and len(polinomio_to_val) == 0):
            pass
        else:
            polinomio_to_val.append(polinomio[i])
    for i in range(len(polinomio_to_val)):
        valor += polinomio_to_val[i] * (point ** (grado-i))
    return valor

#Convertir polinomios a listas del mismo tamaño para mejor manejo de operaciones
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

# Suma de polinomios
def suma_polinomio(polinomio1,polinomio2):
    suma=[]
    for i in range(len(polinomio1)):
        suma.append(polinomio1[i]+polinomio2[i])
    imprimir_polinomios(suma)

# Resta de polinomios
def resta_polinomio(polinomio1,polinomio2):
    resta=[]
    for i in range(len(polinomio1)):
        resta.append(polinomio1[i]-polinomio2[i])
    imprimir_polinomios(resta)

# Multiplicacion de polinomio
def multiplicacion_polinomio(polinomio1,polinomio2,gp1,gp2):
	mul=[]
	ngrado=gp1+gp2
	for i in range(ngrado+1):
		mul.append(0)
	for j in range(gp1+1):
		for k in range(gp2+1):
			mul[j+k] += polinomio1[len(polinomio1)-1-gp1+j]*polinomio2[len(polinomio2)-1-gp2+k]
	imprimir_polinomios(mul)

# Derivada de de polinomio
def derivada_polinomio(polinomio):
	derivada=[]
	for i in range(len(polinomio)-1):
		derivada.append((len(polinomio)-i-1)*polinomio[i])
	imprimir_polinomios(derivada)

# Integral de polinomio
def integral_polinomio(polinomio):
	integral=[]
	for i in range(len(polinomio)):
		integral.append(((polinomio[i]*1.0)*(1/(len(polinomio)-i))))
	integral.append(0)
	imprimir_polinomios(integral)

# Imprimir polinomios
def imprimir_polinomios(polinomio):
	for i in range(len(polinomio)):
		exp=len(polinomio)-i-1
		if i != len(polinomio)-1:
			#print(i)
			print(str(polinomio[i]) + "x^"+str(exp),end=' + ')
		else:
			#print(i,end='')
			print(str(polinomio[i]) + "x^"+str(exp),end = '')
	print(" ")

######## Vectores ########
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

##### OPERACIONES EN GENERAL #####

def operaciones_vectores(dim,vec1,vec2,escalar):
    ##OPERACIONES SOLICITADAS PARA VECTORES
    print("="*(25+(dim*3)))
    print("EL VECTOR 1 INGRESADO:  "+str(vec1))
    print("EL VECTOR 2 INGRESADO:  "+str(vec2))
    print("="*(25+(dim*3)))
    print("La suma es:   "+str(suma_vectores(dim,vec1,vec2)))
    print("La resta es:  "+str(resta_vectores(dim,vec1,vec2)))
    print("El escalar del vector 1 es:  "+str(escalar_vec(dim,vec1,escalar)))
    print("El escalar del vector 2 es:  "+str(escalar_vec(dim,vec2,escalar)))
    print("La norma es:               "+str(norma_vec(dim,vec1,vec2)))
    anguloRad, anguloGrad = angulo_vec(dim,vec1,vec2)
    print("El angulo en radianes es:  "+str(anguloRad))
    print("El angulo en grados es:    "+str(anguloGrad))
    print("="*(35+(dim*3)))


def operaciones_polinomio(polinomio1,polinomio2,grado1,grado2,point):
    polinomio1,polinomio2,grado1,grado2 = convertir_polinomio(polinomio1,polinomio2,grado1,grado2,)
    ##OPERACIONES SOLICITADAS PARA POLINOMIOS
    print("="*(50+(grado1*3)))
    print("EL POLINOMIO 1 INGRESADO:  ",end='')
    imprimir_polinomios(polinomio1)
    print("EL POLINOMIO 2 INGRESADO:  ",end='')
    imprimir_polinomios(polinomio2)
    print("")
    print("="*(50+(grado1*3)))
    print("El valor en el punto "+str(point)+ " para el polinomio 1 es:  "+str(valor_punto_pol(polinomio1,grado1,point)))
    print("El valor en el punto "+str(point)+ " para el polinomio 2 es:  "+str(valor_punto_pol(polinomio2,grado2,point)))
    print("La suma es:                            ", end = '')
    suma_polinomio(polinomio1,polinomio2)
    print("La resta es:                           ", end = '')
    resta_polinomio(polinomio1,polinomio2)
    print("La multiplicacion es:                  ", end = '')
    multiplicacion_polinomio(polinomio1,polinomio2,grado1,grado2)
    print("La derivada del primer polinomio es:   ", end = '')
    derivada_polinomio(polinomio1)
    print("La derivada del segundo polinomio es:  ", end = '')
    derivada_polinomio(polinomio2)
    print("La integral del primer polinomio es:   ", end = '')
    integral_polinomio(polinomio1)
    print("La integral del segundo polinomio es:  ", end = '')
    integral_polinomio(polinomio2)
    print("="*(60+(grado1*3)))


def tarea1():
    dim,vector1,vector2,escalar,grad1,grad2,poli1,poli2,pnt = leer_archivo()
    if dim == None:
        print("INGRESE VECOTRES DE LA MISMA DIMENSIÓN")
    else:
        operaciones_vectores(dim,vector1,vector2,escalar)
    print("")
    operaciones_polinomio(poli1,poli2,grad1,grad2,pnt)

tarea1()