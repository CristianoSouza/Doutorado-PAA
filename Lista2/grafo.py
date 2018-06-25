
from vertice import Vertice
from aresta import Aresta
import networkx as nx
import numpy as n
import Queue as q
from subset import Subset

class Grafo:
    lista_vertices = []
    lista_arestas = []
    tempo = 0

    def __init__(self):
        self.lista_vertices = []
        self.lista_arestas = []
        self.tempo = 0

    def novo_vertice(self, identificador):
        self.lista_vertices.append(Vertice(identificador))

    def nova_aresta(self, origem, destino, peso): 
        origem_aux = self.busca_vertice(origem)
        destino_aux = self.busca_vertice(destino)
        if (origem_aux is not None) and (destino_aux is not None):
            self.lista_arestas.append(Aresta(origem_aux, destino_aux, peso))
        else:
            print("Um dos Vertices ou ambos sao invalidos")

    def busca_vertice(self, identificador):
        for i in self.lista_vertices:
            if identificador == i.getId():
                return i
        else:
            return None

    def esta_vazio(self):
        if len(self.lista_vertices) == 0:
            return True
        else:
            return False

    ######## Breadth First Search - Largura ##########

    def busca_adjacentes(self, u):  
        lista = []
        pesos = []
        for i in range(0,len(self.lista_arestas)):
            origem = self.lista_arestas[i].getOrigem()
            destino = self.lista_arestas[i].getDestino()
            peso = self.lista_arestas[i].getPeso()
            if (u.getId() == origem.getId()) and (destino.getCor() == "BRANCO"):
                lista.append(destino)
                pesos.append(peso)
        return lista, pesos

    def breadth_first_search(self, identificador):
        fonte = self.busca_vertice(identificador)
        if fonte is None:
            return "Vertce Nulo"

        for i in range(0,len(self.lista_vertices)):
            self.lista_vertices[i].setCor("BRANCO")
            self.lista_vertices[i].pai = []
            self.lista_vertices[i].setDistancia(99999999)    
        fonte.setCor("CINZA")
        fonte.pai = None
        lista = [fonte]

        while len(lista) != 0:
            u = lista.pop(0)
            print u
            lista_adjacentes = self.busca_adjacentes(u)[0]  # retorna adjacente no visitado
            for adj in lista_adjacentes:
                adj.pai.append(u.getId())
                adj.setCor("CINZA")
                adj.distancia += 1
                lista.append(adj)
            u.setCor("PRETO")

    ########## Depth First Search - Profundidade ##########

    def depth_first_search(self):
        self.tempo = 0
        for v in self.lista_vertices:
            v.setCor("BRANCO")
            v.setImput(0)
            v.setOutput(0)
            v.pai = []

        for v in self.lista_vertices:
            if (v.getCor() == "BRANCO"):
                self.visita(v)

    def visita(self, u):
        print("Visitando o vertice: %s" % u.getId())
        u.setCor("CINZA")
        self.tempo += 1
        u.setImput(self.tempo)
        lista_adjacentes = self.busca_adjacentes(u)[0]  # retorna adjacente no visitado
        for adj in lista_adjacentes:
            adj.pai.append(u.getId())
            self.visita(adj)

        self.tempo += 1
        u.setOutput(self.tempo)
        u.setCor("PRETO")
        print("Voltando para: ", u.pai)

    ########## Ordenacao Topologica ##########
    def ordenacaoTopologica(self):
        self.tempo = 0
        lista_ordenacao = []
        for v in self.lista_vertices:
            v.setCor("BRANCO")
            v.setImput(0)
            v.setOutput(0)
            v.pai = []
        for v in self.lista_vertices:
            if (v.getCor() == "BRANCO"):
                self.visitaOrdTop(v,lista_ordenacao)

        return lista_ordenacao

    def visitaOrdTop(self, u, lista_final):
        print("Visitando o vertice: %s" % u.getId())
        u.setCor("CINZA")
        self.tempo += 1
        u.setImput(self.tempo)
        lista_adjacentes = self.busca_adjacentes(u)[0] 
        for adj in lista_adjacentes:
            adj.pai.append(u.getId())
            self.visitaOrdTop(adj,lista_final)

        self.tempo += 1
        u.setOutput(self.tempo)
        u.setCor("PRETO")
        lista_final.insert(0,u)

        print("Voltando para: ", u.pai)


    ########## PRIM ##########    
    def PRIM(self, vertice_inicio):
        fila_boolean = {}
        AGM = []
        for v in self.lista_vertices:
            v.setDistancia(99999)
            v.pai = None
        r = self.busca_vertice(vertice_inicio)
        r.setDistancia(0)
        fila = q.PriorityQueue()
        for item in self.lista_vertices:
            fila.put([item.getDistancia(), item])
            fila_boolean[item.getId()] = 1
        
        while ( not fila.empty()):
            u = fila.get(False)[1]
            fila_boolean[u.getId()] = 0
            print ("u: " + u.getId())

            print fila_boolean
            lista_adjacentes, pesos = self.busca_adjacentes(u)  # retorna adjacente no visitado
            for i in range(0,len(lista_adjacentes)):  
                #print(u.getId(),lista_adjacentes[i].getId())
                #print(i)  
                #print (pesos[i],lista_adjacentes[i].getDistancia() )
                if (fila_boolean[lista_adjacentes[i].getId()] == 1) and (pesos[i] < lista_adjacentes[i].getDistancia()):

                    print (" Fila booleana:" + str(fila_boolean[lista_adjacentes[i].getId()]))
                    print("""ATUALIZANDO DISTANCIA VERTICES ("""+ str(u.getId()) +""","""+ str(lista_adjacentes[i].getId()) +""") COM PESO = """ + str(pesos[i]))
                    lista_adjacentes[i].setPai(u.getId())
                    lista_adjacentes[i].setDistancia(pesos[i])
                    
                    AGM.append(lista_adjacentes[i])
        return AGM

    def verifica_key(self, AGM, nome_item):
        for item in AGM.keys():
            if (nome_item == item ):
                    print ("origem e destinos iguais")
                    return 1

        return 0

    ########## ARVORE MTI ##########
    def find(self, subsets, i):
        #find root and make root as parent of i (path compression)
        if (subsets[i].pai != i):
            subsets[i].pai = self.find(subsets, subsets[i].pai)
     
        return subsets[i].pai
    
    def union(self, subsets, x, y):
        xroot = self.find(subsets, x)
        yroot = self.find(subsets, y)
 
        #Attach smaller rank tree under root of high rank tree
        # (Union by Rank)
        if (subsets[xroot].rank < subsets[yroot].rank):
            subsets[xroot].pai = yroot
        elif (subsets[xroot].rank > subsets[yroot].rank):
            subsets[yroot].pai = xroot
            #If ranks are same, then make one as root and increment
            # its rank by one
        else:
            subsets[yroot].pai = xroot
            subsets[xroot].rank+= 1
    
    def makeSet(self,subsets, vetor):
        #make set
        for i in range(0,len(vetor)): 
            subsets.append(Subset())
            subsets[i].pai = vetor[i]
            subsets[i].rank = 0
            subsets[i].numero = vetor[i]

    def generate_mti(self, vetor):
        subsets = []
        self.makeSet(subsets, vetor)

        j = 0
        while j < len(vetor)-1:
            x = self.find(subsets, vetor[j])
            y = self.find(subsets, vetor[j+1])
     
            if (x == y):
                print("x e y iguais")
            self.union(subsets, x, y)
            j+=1
        return subsets

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
            lista.sort()  # ordeno a lista baseado na distancia
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


    def Prim(G = nx.Graph(), R = None):
        # Q e a lista de vertices que nao estao na arvore
        Q    = {}
        # pred armazenara o predecessor de cada vertice
        pred = {}

        # Inicializamos Q com todos os vertices com valor infinito, pois neste
        # ponto ainda nao ha ligacao entre nenhum vertice. Igualmente, nenhum
        # vertice tem predecessor, portanto utilizamos o valor 'null'.
        for v,data in G.nodes(data=True):
            Q[v]    = n.inf
            pred[v] = 'null'

        # Caso nao haja pesos definidos para os vertices, atribuimos o valor 1.0.
        # Esta e uma abordagem alternativa a que usamos em Kruskal, de utilizar uma
        # variavel para verificar se estamos levando em conta o peso ou nao.
        for e,x in G.edges():
            if ('weight' not in G[e][x]):
                G[e][x]['weight'] = 1.0

        # Inicializamos a raiz da arvore com valor 0, e criamos uma arvore chamada
        # MST apenas com os vertices de G.
        Q[R] = 0.0
        MST  = nx.create_empty_copy(G)

        while Q:
            # u := indice do menor elemento de Q
            # pois queremos o vertice de menor peso
            u = min(Q,key=Q.get)

            # removemos de Q, pois ele sera adicionado na arvore
            del Q[u]

            # guardamos os pesos minimos de cada vizinho de u em Q, se forem
            # menores do que os ja armazenados
            for vizinho in G[u]:
                if vizinho in Q:
                    if G[u][vizinho]['weight'] < Q[vizinho]:
                        pred[vizinho] = u
                        Q[vizinho]    = G[u][vizinho]['weight']

            # Se existirem predecessores para u, entao adicionaremos as arestas
            # conectando o vertice u a seus predecessores
            if pred[u] is not 'null':
                for v1,v2,data in G.edges(data=True):
                    # para preservar os dados da aresta, foi necessario esse loop
                    # que verifica todas as arestas do grafo e procura a aresta
                    # (pred(u),u), porem, como um grafo nao direcionado da
                    # biblioteca nao duplica a existencia de suas arestas no
                    # conjunto de arestas, isto e, se tem (u,v) nao tem (v,u), ha a
                    # necessidade de verificar, no caso de grafos nao direcionados,
                    # se haa existencia da aresta (u,pred(u)) ao inves de
                    # (pred(u),u)
                    if ( v1 is pred[u] and v2 is u ):
                        MST.add_edge(pred[u],u,data)
                    elif (  ( v1 is u and v2 is pred[u] ) and
                            ( not nx.is_directed(G) )  ):
                        MST.add_edge(pred[u],u,data)

        return MST

    # Funcao auxiliar para encontrar oindice do conjunto em que o veertice se
    # encontra
    def encontrar_conjunto(lista, vertice):
        i = 0
        for conjunto in lista:
            if (vertice in conjunto):
                return i
            i = i+1

    def Kruskal(G):
        if 'weight' in G.edges(data=True)[0][2]:
            grafo_com_peso = True
        else:
            grafo_com_peso = False

        MST = nx.create_empty_copy(G)

        if grafo_com_peso:
            E = sorted(G.edges(data=True), key=lambda k: k[2]['weight'])
        else:
            E = G.edges(data=True)

        vertices_conexos = []

        # criamos uma lista de conjuntos disjuntos com apenas um vertice cada um, a
        # principio, para depois fazermos as unioes
        for v in G.nodes():
            vertices_conexos.append({v})

        for aresta in E:
            indexConj1 = encontrar_conjunto(vertices_conexos, aresta[0])
            indexConj2 = encontrar_conjunto(vertices_conexos, aresta[1])

            # Se o conjunto encontrado para o vertice 0 e o mesmo do vertice 1,
            # entao nao podemos uni-los, ja que isto fecharia um ciclo.
            if indexConj1 != indexConj2:

                # Se o grafo contem o peso, entao adicionamos as tres informacoes
                # da aresta (2 vertices e dados)
                if grafo_com_peso:
                    MST.add_edge(aresta[0], aresta[1], aresta[2])
                else:
                    MST.add_edge(aresta[0], aresta[1])

                # removemos os dois conjuntos de vertices do vetor vertices_conexos
                if indexConj1 > indexConj2:
                    conj1 = vertices_conexos.pop(indexConj1)
                    conj2 = vertices_conexos.pop(indexConj2)
                else:
                    conj2 = vertices_conexos.pop(indexConj2)
                    conj1 = vertices_conexos.pop(indexConj1)

                # e inserimos um novo conjunto a partir da uniao dos dois
                vertices_conexos.append(conj1.union(conj2))

        return MST
