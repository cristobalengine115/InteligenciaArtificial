import math

# 1 .- VECTORES DE N-DIMENSIONES
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

# SUMA
# RESTA 
# PRODUCTO POR UN ESCALAR
# NORMA
sumaVec = []
restaVec = []
escalarVec1 = []
escalarVec2 = []
norma = 0
resMult=0
mod1=0
mod2=0

for i in range(dim):
    sumaVec.append(vec1[i]+vec2[i])
    restaVec.append(vec1[i]-vec2[i])
    escalarVec1.append(vec1[i]* escalar)
    escalarVec2.append(vec2[i]* escalar)
    norma += (vec2[i]-vec1[i]) ** 2
    resMult += vec1[i]*vec2[i]
    mod1 += vec1[i]**2
    mod2 +=vec2[i]**2
norma = math.sqrt(norma)
mod=math.sqrt(mod1)*math.sqrt(mod2)


alfa=resMult/mod
print('alfa'+str(alfa))
angulo=math.acos(alfa)


print("La suma es:"+str(sumaVec))
print("La resta es:"+str(restaVec))
print("El escalar del vector 1 es:"+str(escalarVec1))
print("El escalar del vector 2 es:"+str(escalarVec2))
print("La norma es:"+str(norma))
print("El angulo en radianes es:"+str(angulo))
angulo=angulo*(180/math.pi)
print("El angulo en grados es:"+str(angulo))






#2 .- POLINOMIOS GRADO N
# grado = int(input('INGRESE EL GRADO DEL POLINOMIO: '))
# polinomio = []

# print('INGRESE LOS VALORES PARA EL POLINOMIO')
# for i in range(grado):
#     x = int(input('x' +str(i-grado) +' -> '))
#     polinomio.append(x)
# VALOR EN UN PUNTO



# SUMA
# RESTA 
# MULTIPLICACION
# DERIVADA
# INTEGRAL