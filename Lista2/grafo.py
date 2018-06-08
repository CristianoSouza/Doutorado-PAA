
from vertice import Vertice
from aresta import Aresta

class Grafo:

    def __init__(self, direcionado=True):
        self.lista_vertices = []
        self.lista_arestas = []
        self.direcionado = direcionado
        self.tempo = 0

    def novo_vertice(self, identificador):
        # string = input(str("Identificador do Vertice: "))
        self.lista_vertices.append(Vertice(identificador))

    def busca_aresta(self, u, v):  # Mtodo recebe dois objetos do tipo Vrtice
        for w in self.lista_arestas:
            origem = w.getOrigem()
            destino = w.getDestino()
            if origem.getId() == u.getId() and destino.getId() == v.getId():
                return w

    def busca_vertice(self, identificador):  # Mtodo recebe um int
        for i in self.lista_vertices:
            if identificador == i.getId():
                return i
        else:
            return None

    def nova_aresta(self, origem, destino, peso):  # Mtodo recebe dois identificadores
        origem_aux = self.busca_vertice(origem)
        destino_aux = self.busca_vertice(destino)
        if (origem_aux is not None) and (destino_aux is not None):
            self.lista_arestas.append(Aresta(origem_aux, destino_aux, peso))
        else:
            print("Um do Vertice ou ambos sao invalidos")

        if self.direcionado == False:
            self.lista_arestas.append(Aresta(destino_aux, origem_aux, peso))  # Aresta(u,v) e Aresta(v,u)

    def esta_vazio(self):
        if len(self.lista_vertices) == 0:
            return True
        else:
            return False

    def busca_adjacente(self, u):  # Mtodo recebe um vertice
        for i in range(len(self.lista_arestas)):
            origem = self.lista_arestas[i].getOrigem()
            destino = self.lista_arestas[i].getDestino()
            if (u.getId() == origem.getId()) and (destino.getVisitado() == False):
                destino.setVisitado(True)  # Para que n retorn o mesmo vertice seguidas veses
                return destino
        else:
            return None

    ####################################################################

    def Depth_first_search(self):
        self.tempo = 0
        for v in self.lista_vertices:
            v.setVisitado(False)
            v.input = 0
            v.output = 0
        for v in self.lista_vertices:
            if not v.getVisitado():
                self.visita(v)

    def visita(self, u):
        print("Visitando o vertice: %s" % u.getId())
        u.setVisitado(True)
        self.tempo += 1
        u.setImput(self.tempo)
        v = self.busca_Adjacente(u)  # retorna apenas no visitado ou nulo
        while v is not None:
            v.pai.append(u.getId())
            self.visita(v)
            v = self.busca_Adjacente(u)

        self.tempo += 1
        u.setOutput(self.tempo)
        print("Voltando para: ", u.pai)

    ####################################################################


    def busca_adjacentes(self, u):  # Mtodo recebe um vertice
        lista = []
        for i in range(len(self.lista_arestas)):
            origem = self.lista_arestas[i].getOrigem()
            destino = self.lista_arestas[i].getDestino()
            if (u.getId() == origem.getId()) and (destino.getCor() == "BRANCO"):
                lista.append(destino)
        return lista

    def breadth_first_search(self, identificador):
        fonte = self.busca_vertice(identificador)
        if fonte is None:
            return "Vertce Nulo"

        for i in range(0,len(self.lista_vertices)):
            self.lista_vertices[i].cor = "BRANCO"
            self.lista_vertices[i].pai = []
            self.lista_vertices[i].estimativa = 99999999    
        fonte.cor = "CINZA"
        fonte.pai = None
        lista = [fonte]

        while len(lista) != 0:
            u = lista.pop(0)
            print u
            lista_adjacentes = self.busca_adjacentes(u)  # retorna adjacente no visitado
            for adj in lista_adjacentes:
                adj.pai.append(u.getId())
                adj.cor = "CINZA"
                adj.estimativa += 1
                lista.append(adj)
            u.cor = "PRETO"



    ####################################################################


    def Breadth_first_search(self, identificador):
        fonte = self.busca_vertice(identificador)
        if fonte is None:
            return "Vertce Nulo"
        self.inicializa_Fonte(fonte)
        lista = [fonte]
        while 0 != len(lista):
            u = lista[0]
            v = self.busca_adjacente(u)  # retorna adjacente no visitado
            if v is None:
                lista.pop(0)  # retiro o vertice sem adjacentes

            else:
                self.tempo += 1
                v.setImput(self.tempo)
                v.pai.append(u.getId())
                v.setVisitado(True)
                lista.append(v)

            u.setVisitado(True)

    def imprime_Grafo_com_Destino(self, origem, destino):
        destino_Aux = self.busca_vertice(destino)
        if len(destino_Aux.pai) == 0:
            print("Nao ha caminho")
        else:
            print(destino)
            self.imprime_grafo(origem, destino)

    def imprime_grafo(self, origem, destino):
        if origem == destino:
            print("Fim")
        else:
            destino_Aux = self.busca_vertice(destino)
            if len(destino_Aux.pai) == 0:
                print("Nao ha caminho")
            else:
                print(destino_Aux.pai[0])
                self.imprime_grafo(origem, destino_Aux.pai[0])

    ####################################################################

    def relaxa_Vertice(self, u, v, w):
        if v.getEstimativa() > (u.getEstimativa() + w.getPeso()):
            v.setEstimativa(u.getEstimativa() + w.getPeso())
            v.pai.append(u.getId())  # guarda apenas o id

    def Dijkstra(self, origem):
        fonte = self.busca_Vertice(origem)
        if fonte is None:
            return "Vertce Nulo"

        self.inicializa_Fonte(fonte)
        lista = []
        resposta = []  # conjunto resposta
        for i in self.lista_vertices:
            lista.append(i)
        while len(lista) != 0:
            lista.sort()  # ordeno a lista baseado na estimativa
            u = lista[0]
            v = self.busca_Adjacente(u)
            if v is None:
                for i in self.lista_vertices:  # como o vetice u marcou seus adj como visitado nenhum outro vrtice visitara
                    i.setVisitado(
                        False)  # esse vertice entoa preciso marcar como nao visitado pra bucar os adj de outro vertice
                self.tempo += 1
                u.setImput(self.tempo)  # apenas mostra a ordem de visitacao do grafo
                resposta.append(lista[0])
                lista.pop(0)  # retiro vertice sem adjacente da lista

            else:
                w = self.busca_Aresta(u, v)
                if w is not None:
                    self.relaxa_Vertice(u, v, w)

        print("Estimativas: ")
        for i in resposta:
            print(i) # imprimo as respostas