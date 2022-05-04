import string
import random
import numpy as np
import time
class Nodo:
	'''Clase Nodo que permite almacenar la información independientemente'''
	def __init__(self,nombre,vecinos):
		'''Constructor'''
		self.nombre = nombre
		self.vecinos = vecinos

	def impri_grafo_info(self):
		'''Imprime la información del grafo y si detecta una eurisitica de -1 se desprecia'''
		print('Nodo: ' +str(self.nombre) + ' -Vecinos: '+ str(self.vecinos))

class Grafo:
	'''Clase grafo que almacena los nodos'''
	def __init__(self, nodo_inicial):
		'''Constructor'''
		self.nodos = {}
		self.nodo_inicial = nodo_inicial

	def getNodo(self,nombreNodo):
		'''Devuelve un nodo a partir de un nombre'''
		for i in range (0,len(self.nodos)):
			if (i.nombre == self.nombreNodo):
				return i

	def impriGrafo(self):
		"""Imprimer la información de todos los nodos del grafo"""
		for i in self.nodos:
			self.nodos[i].impri_grafo_info()
		print("==========================================================================================================")

	def createGrafo(self,grafo):
		'''Crea un grafo a partir de una cadena,  '''
		nodes = grafo.split(';')
		for i in nodes:
			vecinos = {}
			vecinos_n = i.split(',')
			tamanio = len(vecinos_n) -1
			for j in range(tamanio):
				vecinos[vecinos_n[j+1][0]] = vecinos_n[j+1][1:]  
			nodo = Nodo(vecinos_n[0],vecinos)


			self.nodos[vecinos_n[0][0]] = nodo
	def Markov(self):
		actual = self.nodos[self.nodo_inicial]
		while 1:	
			probabilidad = random.randrange(100)
			lista = []
			#print("Actualmente se encuentra " + str(actual.nombre))
			print(str(actual.nombre))
			llaves = actual.vecinos.keys()
			nueva_llave = []
			for k in llaves:
				nueva_llave.append(k)
			probable = []
			for i in llaves:
				calc = 0.01*int(actual.vecinos[i])
				probable.append(calc)
				lista += [i]*int(calc*100)

			#lista = np.random.choice(nueva_llave, size = 100, p= probable)

			
			actual = self.nodos[str(random.choice(lista))]
			
			time.sleep(1)
				
					

		
			
	

def aplicacion_Grafo():
	##DIJKSTRA

	#mi_grafo = Grafo('A')
	#mi_grafo.createGrafo('A,B7,C9;B,A7,D8;D,B8,C6,E5,F12;F,D12,E17;E,C2,D5,F17;C,A9,D6,E2')
	#print("===INFORMACIÓN GRAFO CREADO PARA DIJKSTRA===")
	#mi_grafo.impriGrafo()
	#mi_grafo.dijkstra('F')
	#mi_grafo.impriGrafo()

	#mi_grafo = Grafo('A')
	#mi_grafo.createGrafo('A,B7,C9;B,A7,D8;D,B8,C6,E5,F12;F,D12,E17;E,C2,D5,F17;C,A9,D6,E2')
	#print("===INFORMACIÓN GRAFO CREADO PARA DIJKSTRA===")
	#mi_grafo.impriGrafo()
	#mi_grafo.dijkstra('D')
	#mi_grafo.impriGrafo()

	#S,S80,L05,N15;N,N50,L30,S20;L,L60,N20,S20
	graph_two = Grafo('N')
	graph_two.createGrafo('S,S80,L05,N15;N,N50,L30,S20;L,L60,N20,S20')
	print("===INFORMACIÓN GRAFO CREADO PARA A*===")
	graph_two.impriGrafo()
	graph_two.Markov()


aplicacion_Grafo()