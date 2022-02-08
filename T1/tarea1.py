import math

# # 1 .- VECTORES DE N-DIMENSIONES
# print("")
# dim = int(input('INGRESE LAS DIMENSIONES DE LOS VECTORES: '))
# vec1 = []
# print('INGRESE '+str(dim)+' VALORES PARA EL VECTOR 1')
# for i in range(dim):
#     x = int(input('->'))
#     vec1.append(x)
# vec2 = []
# print('INGRESE '+str(dim)+' VALORES PARA EL VECTOR 2')
# for i in range(dim):
#     x = int(input('->'))
#     vec2.append(x)


# escalar = int(input('INGRESE EL ESCALAR AL QUE QUIERE MULTIPLICAR EL VECTOR'))

# # SUMA
# # RESTA 
# # PRODUCTO POR UN ESCALAR
# # NORMA
# sumaVec = []
# restaVec = []
# escalarVec1 = []
# escalarVec2 = []
# norma = 0
# resMult=0
# mod1=0
# mod2=0

# for i in range(dim):
#     sumaVec.append(vec1[i]+vec2[i])
#     restaVec.append(vec1[i]-vec2[i])
#     escalarVec1.append(vec1[i]* escalar)
#     escalarVec2.append(vec2[i]* escalar)
#     norma += (vec2[i]-vec1[i]) ** 2
#     resMult += vec1[i]*vec2[i]
#     mod1 += vec1[i]**2
#     mod2 +=vec2[i]**2
# norma = math.sqrt(norma)
# mod=math.sqrt(mod1)*math.sqrt(mod2)


# alfa=resMult/mod
# print('alfa'+str(alfa))
# angulo=math.acos(alfa)


# print("La suma es:"+str(sumaVec))
# print("La resta es:"+str(restaVec))
# print("El escalar del vector 1 es:"+str(escalarVec1))
# print("El escalar del vector 2 es:"+str(escalarVec2))
# print("La norma es:"+str(norma))
# print("El angulo en radianes es:"+str(angulo))
# angulo=angulo*(180/math.pi)
# print("El angulo en grados es:"+str(angulo))






# 2 .- POLINOMIOS GRADO N
grado1 = int(input('INGRESE EL GRADO DEL POLINOMIO 1: '))
grado2 = int(input('INGRESE EL GRADO DEL POLINOMIO 2: '))
#grado1 = grado1+1
#grado2 = grado2+1
polinomio1 = []
polinomio2 = []

print('INGRESE LOS VALORES PARA EL POLINOMIO 1')
for i in range(grado1):
    x = int(input('x^' +str(grado1-i) +' -> '))
    polinomio1.append(x)

print('INGRESE LOS VALORES PARA EL POLINOMIO 2')
for i in range(grado2):
    x = int(input('x^' +str(grado2-i) +' -> '))
    polinomio2.append(x)
# VALOR EN UN PUNTO
val1=0
val2=0
point = int(input('INGRESE EL PUNTO A EVALUAR LOS POLINOMIOS'))
for i in range(grado1):
    val1 += polinomio1[i] * (point ** (grado1-i))

for i in range(grado2):
    val2 += polinomio2[i] * (point ** (grado2-i))
print(val1)
print(val2)

# SUMA
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

suma=[]
for i in range(len(polinomio1)):
    suma.append(polinomio1[i]+polinomio2[i])
print(suma)
# RESTA 
resta=[]
for i in range(len(polinomio1)):
    resta.append(polinomio1[i]-polinomio2[i])
print(resta)
# MULTIPLICACION
# DERIVADA
# INTEGRAL


[1,3,5,2]

[0,1,1,3]