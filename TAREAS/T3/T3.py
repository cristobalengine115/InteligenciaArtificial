import random
import math
# Desarrollar un código que muestre la evolución 
# de un autómata celular unidimensional:
def crear_poblacion(num_poblacion):
	'''Crea una poblacion de cierto tamaño, que depende del valor dado'''
	poblacion = []
	for i in range(num_poblacion):
		poblacion.append(random.randint(0, 1))
	return poblacion
def crear_tabla_reglas():
	'''Crea la tabla de reglas a seguir'''
	reglas = {}
	reglas["000"] = [0]
	reglas["001"] = [1]
	reglas["010"] = [1]
	reglas["011"] = [1]
	reglas["100"] = [1]
	reglas["101"] = [1]
	reglas["110"] = [1]
	reglas["111"] = [0]

	return reglas

def paso_gen(reglas,poblacion):
	'''Crea una generacion nueva a a partir de las reglas a seguir y la poblacion'''
	large = len(poblacion)
	next_gen = []
	for i in range(large):
		if i == 0:
			
			alrededor = str(poblacion[large-1])
			alrededor = alrededor + str(poblacion[i])
			alrededor = alrededor + str(poblacion[i+1])
			estado = reglas[alrededor]
		elif i == large-1:
			alrededor = str(poblacion[i-1])
			alrededor = alrededor + str(poblacion[i])
			alrededor = alrededor + str(poblacion[0])
			estado = reglas[alrededor]
		else:
			alrededor = str(poblacion[i-1])
			alrededor = alrededor + str(poblacion[i])
			alrededor = alrededor + str(poblacion[i+1])
			estado = reglas[alrededor]
		next_gen.append(estado[0])
	return next_gen
def construir_primer_lado(longitud):
	'''Construye el primer lado del triangulo'''
	primer = []
	for i in range(longitud):
		if i == (math.floor(longitud/2)):
			primer.append(1)
		else:
			primer.append(0)
	return primer
def triangulo_sierpinski(reglas,num_iter):
	'''Construye el triangulo Sierpinski'''
	triangulo = construir_primer_lado(num_iter)

	for i in range(num_iter):
		
		triangulo_i = str(triangulo).replace(","," ")
		triangulo_i = str(triangulo_i).replace("1","*")
		triangulo_i = str(triangulo_i).replace("0"," ")
		print(triangulo_i)
		triangulo = paso_gen(reglas,triangulo)

def main():
	'''Lleva a cabo el avance de generaciones, a partir de cierto numero de poblacion y determinadas generaciones'''
	poblacion = int(input('Ingrese la cantidad de población requerida\n-->'))
	num_gen = int(input('Ingrese el numero de generaciones\n-->'))
	poblacion_actual = crear_poblacion(poblacion)
	print("Poblacion Inicial:       ", end=' ')
	print(poblacion_actual)
	reglas = crear_tabla_reglas()
	for i in range(num_gen):
		poblacion_actual = paso_gen(reglas,poblacion_actual)
		print("Poblacion Generacion "+str(i+1)+" : ", end=' ' + str(poblacion_actual))
		print(' ')
	tria = int(input('Ingrese el numero de renglones del triangulo\n-->'))
	triangulo_sierpinski(reglas,tria)
	
if __name__ == '__main__':
    
    main()
    
