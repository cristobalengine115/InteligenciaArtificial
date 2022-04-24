import string
class Nodo:
	'''Clase Nodo que permite almacenar la infromación independientemente'''
	def __init__(self,nombre,dist_tentativa,vecinos,euristica):
		'''Constructor'''
		self.nombre = nombre
		self.anterior = None
		self.dist_tentativa = dist_tentativa
		self.dist_tentativa_f = dist_tentativa
		self.euristica = euristica
		self.vecinos = vecinos
		self.orden = []
		self.visitado = False
	def impri_grafo_info(self):
		'''Imprime la información del grafo y si detecta una eurisitica de -1 se desprecia'''
		print('Nodo: ' +str(self.nombre) + ' -Distancia tentativa: '+ str('infinito' if self.dist_tentativa == 1000 else self.dist_tentativa) +' -Vecinos: '+ str(self.vecinos) +' -Anterior: '+ str(self.anterior), end = '')
		if self.euristica != -1:
			print(' -Euristica: '+str(self.euristica)+' Distancia tentativa F: '+ str(self.dist_tentativa_f))
		else:
			print('')

class Grafo:
	'''Clase grafo que almacena los nodos'''
	def __init__(self, nodo_inicial):
		'''Constructor'''
		self.nodos = {}
		self.nodo_no_visitados = []
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

	def createGrafo(self,grafo,banderaEuristica = None):
		'''Crea un grafo a partir de una cadena, si se incluye un boolen al final se guardaran laseuristicas '''
		nodes = grafo.split(';')
		for i in nodes:
			vecinos = {}
			vecinos_n = i.split(',')
			tamanio = len(vecinos_n) -1
			for j in range(tamanio):
				vecinos[vecinos_n[j+1][0]] = vecinos_n[j+1][1:]  
				#Euristicas
				if banderaEuristica is None:
					if (len(self.nodos) == 0):
						nodo = Nodo(vecinos_n[0],0,vecinos,-1)
					else:
						nodo = Nodo(vecinos_n[0],1000,vecinos,-1)
				else:
					if (len(self.nodos) == 0):
						nodo = Nodo(vecinos_n[0][0],0,vecinos,vecinos_n[0][1:])
					else:
						nodo = Nodo(vecinos_n[0][0],1000,vecinos,vecinos_n[0][1:])		

			self.nodos[vecinos_n[0][0]] = nodo
			
	

	def minimo(self, nodos):
		'''Método que determina el menor costo de la distancia entre el nodo origen y final'''
		if len(nodos) > 0:
			minus = self.nodos[nodos[0]].dist_tentativa
			vector = nodos[0]
			for e in nodos:
				if minus > self.nodos[e].dist_tentativa:
					minus = self.nodos[e].dist_tentativa
					vector = e
			return vector
		return None

	def minimo_euristico(self, nodos):
		'''Método que determina el menor costo de la distancia entre el nodo origen y final'''
		if len(nodos) > 0:
			minus = self.nodos[nodos[0].nombre].dist_tentativa_f
			vector = nodos[0]
			for e in nodos:
				if minus > self.nodos[e.nombre].dist_tentativa_f:
					minus = self.nodos[e.nombre].dist_tentativa_f
					vector = e
			return vector
		return None

	def find(self, cerrado,nodo):
		if len(cerrado) > 0:
			for e in cerrado:
				if nodo == e.nombre:
					return True
			return False


	def rutaD(self,destino):
		'''Indica la ruta mas corta que existe entre el nodo origen y el nodo destino'''
		end = False
		route = []
		route.append(destino)
		ant = destino
		while end != True:
			if ant == str(self.nodo_inicial):
				
				end = True
			else:
				ant = str(self.nodos[ant].anterior)
				# print('Valor ant')
				# print(ant)
				route.append(ant)

		route.reverse()
		print('La distancia mas corta es: '+ str(route))
		return route
	#def reconstruir(self,)
	def dijkstra(self,destino):
		'''Algoritmo Dijkstra que calcula la distancia minima y su respectiva ruta entre un punto A y un punto B'''
		actual = self.nodos[self.nodo_inicial].nombre
		for v in self.nodos:
			self.nodo_no_visitados.append(v)
		while len(self.nodo_no_visitados) > 0:
			if actual == destino :
				return self.rutaD(destino)
				#return True
			for i in self.nodos[actual].vecinos:
				if self.nodos[i[0]].visitado == False:
					if self.nodos[actual].dist_tentativa + int(self.nodos[actual].vecinos[i]) < self.nodos[i].dist_tentativa:
						self.nodos[i].dist_tentativa = self.nodos[actual].dist_tentativa + int(self.nodos[actual].vecinos[i])
						self.nodos[i].anterior = actual
			self.nodos[actual].visitado = True
			self.nodo_no_visitados.remove(actual)
			actual = self.minimo(self.nodo_no_visitados)

	def a_star(self,nodo_final):	
		'''Algoritmo de A*'''
		self.nodo_no_visitados.append(self.nodos[str(self.nodo_inicial)])
		cerrado = []
		actual = self.nodo_no_visitados[0]
		while(len(self.nodo_no_visitados) != 0 ):
			if(actual.nombre == self.nodos[nodo_final].nombre ):
				finales = []
				for i in self.nodos[actual.nombre].vecinos:
					finales.append(self.nodos[i])

				anterior = self.minimo_euristico(finales)
				actual.anterior = anterior.nombre
				self.nodos[actual.nombre].dist_tentativa = self.nodos[anterior.nombre].dist_tentativa + int(self.nodos[anterior.nombre].vecinos[actual.nombre])
				self.nodos[actual.nombre].dist_tentativa_f = self.nodos[actual.nombre].dist_tentativa + int(self.nodos[actual.nombre].euristica)
				pass			
			self.nodo_no_visitados.remove(actual)
			cerrado.append(self.nodos[actual.nombre]) 

			for i in actual.vecinos:
				if self.find(cerrado,i):
					pass
				else:
					if self.find(self.nodo_no_visitados,i):
						pass
					else:
						self.nodo_no_visitados.append(self.nodos[i])
					if self.nodos[actual.nombre].dist_tentativa > int(self.nodos[actual.nombre].vecinos[i]):
						pass
					else:
						self.nodos[i].anterior = actual.nombre
						self.nodos[i].dist_tentativa = self.nodos[actual.nombre].dist_tentativa + int(self.nodos[actual.nombre].vecinos[i])
						self.nodos[i].dist_tentativa_f = self.nodos[i].dist_tentativa + int(self.nodos[i].euristica)


			actual = self.minimo_euristico(self.nodo_no_visitados)
		return self.rutaD(nodo_final)
	




def aplicacion_Grafo():
	##DIJKSTRA

	mi_grafo = Grafo('A')
	mi_grafo.createGrafo('A,B7,C9;B,A7,D8;D,B8,C6,E5,F12;F,D12,E17;E,C2,D5,F17;C,A9,D6,E2')
	print("===INFORMACIÓN GRAFO CREADO PARA DIJKSTRA===")
	mi_grafo.impriGrafo()
	mi_grafo.dijkstra('D')
	mi_grafo.impriGrafo()

	##A*
	graph_two = Grafo('A')
	graph_two.createGrafo('A55,B15,E20;B40,A15,C20,F40;C25,B20,D30;D40,C25,G40;E45,A20,F30;F20,E30,G20;G0,D40,F20',True)
	print("===INFORMACIÓN GRAFO CREADO PARA A*===")
	graph_two.impriGrafo()
	graph_two.a_star('G')
	graph_two.impriGrafo()

aplicacion_Grafo()