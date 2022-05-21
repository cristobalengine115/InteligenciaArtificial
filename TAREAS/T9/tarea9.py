#Programa correspondiente al cálculo de la función discriminante (Mahalanobis)de un grupo de muestras.
#Si el método devuelve True el punto muestrado pertenece a la primera clase
#De caso contrario pertenece a la segunda clase
import numpy as np
import math 
from ast import Str
from scipy.stats import chi2


def main(muestras,punto):
    #muestras = defineMuestras()
    medias = calculaMedias(muestras)
    covarianzas = calculaCovarianza(muestras,medias)
    print("Covarianza calculada")
    #print("==Ingrese el punto a evaluar==")
    #a1 = int(input("Ingrese el dato de la fila 1: "))
    #a2 = int(input("Ingrese el dato de la fila 2: "))
    #punto = np.array(([a1],[a2]))
    punto=np.array((punto[0],punto[1]))
    resultado = mahalanobis(punto,medias,covarianzas)
    return resultado

def defineMuestras():
    muestras = []
    for i in range (0, 2):
        exec('muestra{} = []'.format(i+1))
        contador = 1
        continua = True
        print("Para la clase "+str(i+1))
        while(continua):
            print("Muestra "+str(contador)+" de la clase "+str(i+1))
            a1 = int(input("Ingrese el dato de la fila 1: "))
            a2 = int(input("Ingrese el dato de la fila 2: "))
            exec('muestra{}.append([a1,a2])'.format(i+1))
            print("Desea agregar otra matriz a la muestra "+str(i+1))
            print("1.- Sí")
            print("0.- No")
            des=int(input("-> "))
            if (des == 0):
                continua = False
            contador+=1
        exec('muestras.append(muestra{})'.format(i+1))
    return muestras

def calculaMedias(muestras):
    medias=[]
    for i in range (0, len(muestras)):
        exec('media{} = []'.format(i+1))
        contador1 = 0
        contador2 = 0
        for j in range (0,len(muestras[i])):
            contador1+=muestras[i][j][0]
            contador2+=muestras[i][j][1]
        m1=contador1/len(muestras[i])
        m2=contador2/len(muestras[i])
        exec('media{}.append([m1,m2])'.format(i+1))
        exec('medias.append(media{})'.format(i+1))
    return medias

def calculaCovarianza(muestras,medias):
    covarianzas = []
    for i in range(0, len(muestras)):
        exec('covarianza{} = []'.format(i+1))
        for j in range (0,4):
            contador = 0
            for k in range (0,len(muestras[i])):
                if(j==0):
                    contador+=(muestras[i][k][0]-medias[i][0][0])**2
                elif(j==1):
                    contador+=(muestras[i][k][0]-medias[i][0][0])*(muestras[i][k][1]-medias[i][0][1])
                elif(j==2):
                    contador+=(muestras[i][k][1]-medias[i][0][1])*(muestras[i][k][0]-medias[i][0][0])
                elif(j==3):
                    contador+=(muestras[i][k][1]-medias[i][0][1])**2
            exec('covarianza{}.append(contador/len(muestras[i]))'.format(i+1))
        exec('covarianzas.append(covarianza{})'.format(i+1))
    return covarianzas

def mahalanobis(punto,m,c):

    medias1=np.array(([m[0][0][0]],[m[0][0][1]]))
    medias2=np.array(([m[1][0][0]],[m[1][0][1]]))
    covarianza1 = np.array(([c[0][0],c[0][1]],[c[0][2],c[0][3]]))
    covarianza2 = np.array(([c[1][0],c[1][1]],[c[1][2],c[1][3]]))
    print(covarianza2)
    covarianza1I=np.linalg.inv(covarianza1)
    covarianza2I=np.linalg.inv(covarianza2)
    
    #Distancia 1
    diferencia1 = punto-medias1
    diferencia1T= np.transpose(diferencia1)
    mul1=np.dot(diferencia1T, covarianza1I)
    cuadrado1=np.dot(mul1,diferencia1)
    res1=math.sqrt(cuadrado1[0][0])

    #Distancia 2
    diferencia2 = punto-medias2
    diferencia2T= np.transpose(diferencia2)
    mul2=np.dot(diferencia2T, covarianza2I)
    cuadrado2=np.dot(mul2,diferencia2)
    print(cuadrado2[0][0])
    res2=math.sqrt(cuadrado2[0][0])
    if(res1>res2):
        print("El punto pertenece a la clase 1")
        return True
    else:
        print("El punto pertenece a la clase 2")
        return False
    

main([[[2,0],[8,1]],[[1,1],[5,1],[5,3]]],[9,1])