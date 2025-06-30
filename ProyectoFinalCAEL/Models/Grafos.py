class Grafo:
    def __init__(self):
        # Diccionario de adyacencia: {id: {vecino_id: peso, ...}}
        self.adyacencia = {}

    def agregar_nodo(self, id):
        if id not in self.adyacencia:
            self.adyacencia[id] = {}

    def agregar_arista(self, id1, id2, peso=1):
        self.agregar_nodo(id1)
        self.agregar_nodo(id2)
        self.adyacencia[id1][id2] = peso
        self.adyacencia[id2][id1] = peso  # Grafo no dirigido

    def obtener_vecinos(self, id):
        return self.adyacencia.get(id, {})

    def obtener_aristas(self):
        aristas = set()
        for id1 in self.adyacencia:
            for id2, peso in self.adyacencia[id1].items():
                if (id2, id1) not in aristas:
                    aristas.add((id1, id2, peso))
        return list(aristas)

    def existe_arista(self, id1, id2):
        return id2 in self.adyacencia.get(id1, {})
