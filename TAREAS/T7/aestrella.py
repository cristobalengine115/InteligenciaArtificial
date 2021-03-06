class Nodo:
	def __init__(self,nombre,dist_tentativa,vecinos):
		self.nombre = nombre
		self.anterior = None
		self.dist_tentativa = dist_tentativa
		self.vecinos = vecinos
		self.orden = []
		self.visitado = False
	def impri_grafo_info(self):
		print('Nodo: ' +str(self.nombre) + ' -Distancia tentativa: '+ str('infinito' if self.dist_tentativa == 1000 else self.dist_tentativa) +' -Vecinos: '+ str(self.vecinos) +' -Anterior: '+ str(self.anterior))
class Grafo:

	def __init__(self, nodo_inicial):
		self.nodos = {}
		self.nodo_no_visitados = []
		self.nodo_inicial = nodo_inicial

	def getNodo(self,nombreNodo):
		for i in range (0,len(self.nodos)):
			if (i.nombre == self.nombreNodo):
				return i

	def impriGrafo(self):
		for i in self.nodos:
			self.nodos[i].impri_grafo_info()
		print("==========================================================================================================")

	def createGrafo(self,grafo):
		nodes = grafo.split(';')
		for i in nodes:
			vecinos = {}
			vecinos_n = i.split(',')
			tamanio = len(vecinos_n) -1
			for j in range(tamanio):

				vecinos[vecinos_n[j+1][0]] = vecinos_n[j+1][1:]  ####que
				if (len(self.nodos) == 0):
					nodo = Nodo(vecinos_n[0],0,vecinos)
				else:
					nodo = Nodo(vecinos_n[0],1000,vecinos)

			self.nodos[vecinos_n[0]] = nodo

	def minimo(self, nodos):
		if len(nodos) > 0:
			minus = self.nodos[nodos[0]].dist_tentativa
			vector = nodos[0]
			for e in nodos:
				if minus > self.nodos[e].dist_tentativa:
					minus = self.nodos[e].dist_tentativa
					vector = e
			return vector
		return None


	def rutaD(self,destino):
		end = False
		route = []
		route.append(destino)
		ant = destino
		while end != True:
			if ant == str(self.nodo_inicial):
				
				end = True
			else:
				ant = str(self.nodos[ant].anterior)
				route.append(ant)

		route.reverse()
		print('La distancia mas corta es: '+ str(route))

	def dijkstra(self,destino):
		actual = self.nodos[self.nodo_inicial].nombre
		for v in self.nodos:
			self.nodo_no_visitados.append(v)
		while len(self.nodo_no_visitados) > 0:
			if actual == destino :
				self.rutaD(destino)
				return True
			for i in self.nodos[actual].vecinos:
				if self.nodos[i[0]].visitado == False:
					if self.nodos[actual].dist_tentativa + int(self.nodos[actual].vecinos[i]) < self.nodos[i].dist_tentativa:
						self.nodos[i].dist_tentativa = self.nodos[actual].dist_tentativa + int(self.nodos[actual].vecinos[i])
						self.nodos[i].anterior = actual
			self.nodos[actual].visitado = True
			self.nodo_no_visitados.remove(actual)
			actual = self.minimo(self.nodo_no_visitados)
		
	




def aplicacion_Grafo():
	mi_grafo = Grafo('A')
	mi_grafo.createGrafo('A,B7,C9;B,A7,D8;D,B8,C6,E5,F12;F,D12,E17;E,C2,D5,F17;C,A9,D6,E2')
	print("===INFORMACI??N GRAFO CREADO===")
	mi_grafo.impriGrafo()
	mi_grafo.dijkstra('F')
	mi_grafo.impriGrafo()

aplicacion_Grafo()