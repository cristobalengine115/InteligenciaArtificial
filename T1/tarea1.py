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
sumaVec = []
restaVec = []
escalarVec1 = []
escalarVec2 = []

for i in range(dim):
    sumaVec.append(vec1[i]+vec2[i])
    restaVec.append(vec1[i]-vec2[i])
    escalarVec1.append(vec1[i]* escalar)
    escalarVec2.append(vec2[i]* escalar)
print(sumaVec)
print(restaVec)
print(escalarVec1)
print(escalarVec2)


# NORMA
# ÁNGULO ENTRE VECTORES

#2 .- POLINOMIOS GRADO N
# VALOR EN UN PUNTO
# SUMA
# RESTA 
# MULTIPLICACION
# DERIVADA
# INTEGRAL