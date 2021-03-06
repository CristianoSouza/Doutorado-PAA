ano = {
    1957: ['Flow-matic' , 'Fortran I'],
    1958: ['Fortran II' , 'Algol 58'],
    1959: ['Lisp'],
    1960: ['COBOL' , 'Algol 60'],
    1961: ['CPL'],
    1962: ['Fortran IV'],
    1963: ['Simula I'],
    1964: ['PL/I' , 'Basic'],
    1966: ['Algol W'],
    1967: ['Simula 67'],
    1968: ['Algol 68'],
    1969: ['BCPL' , 'Smalltalk'],
    1970: ['B' , 'Prolog'],
    1971: ['Pascal' , 'C'],
    1972: ['Smalltalk 72'],
    1974: ['CLU' , 'Smalltalk 74'],
    1975: ['Scheme' , 'Modula'],
    1976: ['Smalltalk 76' , 'S'],
    1977: ['Modula-2' , 'ML' , 'Fortran 77'],
    1978: ['Smalltalk 78' , 'Scheme MIT' , 'CSP' , 'C (K&R)'],
    1979: ['Ada'],
    1980: ['ABC' , 'Smalltalk 80'],
    1983: ['Ada 83' , 'Pascal AFNOR'],
    1984: ['Lazy ML' , 'SML' , 'Scheme 84'],
    1985: ['Common Lisp' , 'Miranda' , 'C++' , 'CLIPS'],
    1986: ['Scheme R3RS' , 'Objective-C' , 'Eiffel'],
    1988: ['Scheme R4RS' , 'Erlang' , 'Life'],
    1989: ['CLOS' , 'Modula-3' , 'ANSI C' , 'Lambda Prolog'],
    1990: ['C++ (ARM)' , 'Haskell' , 'SML 90' , 'Fortran 90'],
    1991: ['Gofer' , 'Python' , 'Perl 4' , 'Oak'],
    1993: ['Mercury' , 'AppleScript' , 'R'],
    1994: ['Lua' , 'Common Lisp (ANSI)' , 'Perl 5'],
    1995: ['C 95' , 'Prolog ISO' , 'Ada 95' , 'PHP' , 'Java' , 'Ruby'],
    1996: ['Squeak' , 'OCaml'],
    1998: ['Scheme R5RS' , 'C++ (ISO)' , 'Java 2' , 'Haskell 98'],
    1999: ['.NET' , 'Python 1.5.2' , 'C 99'],
    2000: ['Lua 4.0' , 'Python 2.0' , 'C#'],
    2001: ['GHC 5.00'],
    2002: ['Python 2.2'],
    2003: ['Lua 5.0' , 'Io' , 'Fortran 2003' , 'GHC 6.0'],
    2004: ['Python 2.4' , 'Java 5' , 'Scala'],
    2005: ['C# 2.0'],
    2006: ['Python 2.5' , 'Java 6' , 'CAL (Open Quark)'],
    2007: ['D 1.0' , 'C# 3.0' , 'Fortress 1.0beta'],
    2008: ['Python 3.0'],
    2009: ['Go'],
    2010: ['Rust' , 'Haskell 2010'],
    2011: ['Java 7'],
    2014: ['Swift' , 'Java 8'],
    2016: ['Python 3.6']
}

pre = [
    ('GHC 6.0', 'Haskell 2010'),
    ('C++', 'Rust'),
    ('Erlang', 'Rust'),
    ('OCaml', 'Rust'),
    ('Haskell 98', 'Rust'),
    ('C# 2.0', 'Rust'),
    ('Lua 4.0', 'Lua 5.0'),
    ('Ada 83', 'Ada 95'),
    ('Scheme 84', 'Scheme R3RS'),
    ('PL/I', 'Pascal'),
    ('Algol W', 'Pascal'),
    ('Python 2.0', 'Python 2.2'),
    ('CPL', 'BCPL'),
    ('ML', 'SML'),
    ('Ada', 'Ada 83' ),
    ('C++ (ARM)', 'C++ (ISO)'),
    ('Fortran IV', 'Basic'),
    ('Java 5', 'Java 6'),
    ('Smalltalk 76', 'Smalltalk 78'),
    ('SML 90', 'Mercury'),
    ('Prolog', 'Mercury'),
    ('Haskell', 'Mercury'),
    ('Modula-3', 'Python'),
    ('ANSI C', 'Python'),
    ('ABC', 'Python'),
    ('Algol 60', 'Scheme'),
    ('Lisp', 'Scheme'),
    ('Modula', 'Modula-2'),
    ('Pascal', 'CLU'),
    ('Simula 67', 'CLU'),
    ('Common Lisp', 'CLOS'),
    ('ML', 'Miranda'),
    ('Smalltalk 80', 'AppleScript'),
    ('Java', 'Java 2'),
    ('Perl 4', 'Perl 5'),
    ('Python 2.2', 'Python 2.4'),
    ('Lua', 'Io'),
    ('Smalltalk 80', 'Io'),
    ('Scheme MIT', 'Common Lisp'),
    ('Lisp', 'Common Lisp'),
    ('Python', 'Python 1.5.2'),
    ('Fortran I', 'Fortran II'),
    ('C#', 'D 1.0'),
    ('Java', 'D 1.0'),
    ('C 99', 'D 1.0'),
    ('C++', 'D 1.0'),
    ('BCPL', 'B'),
    ('Python 2.4', 'Python 2.5'),
    ('Flow-matic', 'COBOL'),
    ('Smalltalk', 'Smalltalk 72'),
    ('Haskell 98', 'Swift'),
    ('CLU', 'Swift'),
    ('Objective-C', 'Swift'),
    ('C# 2.0', 'Swift'),
    ('D 1.0', 'Swift'),
    ('Ruby', 'Swift'),
    ('Python 2.0', 'Swift'),
    ('Rust', 'Swift'),
    ('Haskell', 'Gofer'),
    ('Algol 58', 'Algol 60' ),
    ('Smalltalk 80', 'Squeak'),
    ('Python 2.5', 'Python 3.0'),
    ('C++', 'C++ (ARM)'),
    ('Ada 83', 'C++ (ARM)'),
    ('CLU', 'C++ (ARM)'),
    ('Java 7', 'Java 8'),
    ('Scheme R4RS', 'Scheme R5RS'),
    ('C# 2.0', 'C# 3.0'),
    ('Common Lisp', 'Erlang'),
    ('Prolog', 'Erlang'),
    ('Scheme R3RS', 'Scheme R4RS'),
    ('Lazy ML', 'Haskell'),
    ('Miranda', 'Haskell'),
    ('Common Lisp', 'Common Lisp (ANSI)'),
    ('Smalltalk 74', 'Smalltalk 76'),
    ('COBOL', 'PL/I'),
    ('Algol 60', 'PL/I'),
    ('Fortran IV', 'PL/I'),
    ('Prolog', 'Prolog ISO'),
    ('ANSI C', 'C 95' ),
    ('Algol 60', 'Algol 68' ),
    ('Pascal AFNOR', 'Lua'),
    ('Perl 4', 'Lua'),
    ('Fortran I', 'Algol 58'),
    ('Algol 60', 'Algol W'),
    ('Algol 60', 'Simula I'),
    ('C++ (ARM)', 'Oak'),
    ('Fortran IV', 'Fortran 77' ),
    ('Fortran 2003', 'Fortress 1.0beta'),
    ('Scala', 'Fortress 1.0beta'),
    ('Gofer', 'Haskell 98'),
    ('Haskell', 'Haskell 98'),
    ('Smalltalk 72', 'Smalltalk 74'),
    ('Pascal', 'Modula'),
    ('Java 6', 'Java 7'),
    ('Python 3.0', 'Python 3.6'),
    ('OCaml', 'Scala'),
    ('.NET', 'Scala'),
    ('Java 2', 'Scala'),
    ('Prolog', 'Life'),
    ('Smalltalk 80', 'Ruby'),
    ('Perl 4', 'Ruby'),
    ('Python', 'Ruby'),
    ('Java 2', 'Java 5'),
    ('Java 2', 'CAL (Open Quark)'),
    ('Haskell 98', 'CAL (Open Quark)'),
    ('C 95', 'C 99' ),
    ('Simula 67', 'Eiffel'),
    ('Ada 83', 'Eiffel'),
    ('Python 1.5.2', 'Python 2.0' ),
    ('B', 'C' ),
    ('Algol 68', 'C'),
    ('Scheme', 'Scheme MIT' ),
    ('C++', 'ANSI C'),
    ('C (K&R)', 'ANSI C'),
    ('Modula-2', 'Modula-3' ),
    ('Haskell 98', 'GHC 5.00' ),
    ('Lua', 'Lua 4.0' ),
    ('S', 'R' ),
    ('Scheme', 'R'),
    ('Common Lisp', 'R'),
    ('Algol 60', 'CPL'),
    ('Smalltalk 80', 'Objective-C'),
    ('C (K&R)', 'Objective-C'),
    ('Perl 5', 'PHP'),
    ('Oak', 'Java' ),
    ('Simula 67', 'Smalltalk'),
    ('Fortran 90', 'Fortran 2003' ),
    ('Scheme MIT', 'Scheme 84' ),
    ('C#', 'C# 2.0' ),
    ('C', 'C (K&R)' ),
    ('Smalltalk 78', 'Smalltalk 80' ),
    ('C (K&R)', 'C++'),
    ('Algol 68', 'C++'),
    ('Simula 67', 'C++'),
    ('Simula I', 'Simula 67' ),
    ('GHC 5.00', 'GHC 6.0' ),
    ('Java 2', 'C#'),
    ('C++ (ISO)', 'C#'),
    ('Fortran 77', 'Fortran 90' ),
    ('CSP', 'Ada'),
    ('Pascal', 'Ada'),
    ('Prolog', 'CLIPS'),
    ('Prolog', 'Lambda Prolog'),
    ('SML', 'Lambda Prolog'),
    ('Fortran II', 'Fortran IV' ),
    ('Python 2.0', 'Go'),
    ('C', 'Go'),
    ('CSP', 'Go'),
    ('Smalltalk 80', 'Go'),
    ('Modula-3', 'Go'),
    ('Pascal', 'Go'),
    ('C (K&R)', 'ANSI C')
]

from grafo import Grafo
from subcadeia import SubCadeia
from MT1 import MTI
import time
import random

grafo = Grafo()
'''
for item_ano in ano.values():
    for vertice in item_ano:
        grafo.novo_vertice(vertice)
        print("Criado novo vertice: ")
        print grafo.busca_vertice(vertice) 


for item_pre in pre:
    grafo.nova_aresta(item_pre[0], item_pre[1], 0)
    print("Criada nova aresta E(", item_pre[0], ",", item_pre[1], ")!")

#grafo.Breadth_first_search('Python')
#grafo.imprime_Grafo_com_Destino('Python', 'Go')

#grafo.breadth_first_search('SML')
#grafo.depth_first_search()
lista = grafo.ordenacaoTopologica()

for item in lista:
    print item
'''

grafo2 = Grafo()
grafo2.novo_vertice('a')
grafo2.novo_vertice('b')
grafo2.novo_vertice('c')
grafo2.novo_vertice('d')
grafo2.novo_vertice('e')
grafo2.novo_vertice('f')
grafo2.novo_vertice('g')
grafo2.novo_vertice('h')
grafo2.novo_vertice('i')

'''
grafo2.nova_aresta('a','b', 15)
grafo2.nova_aresta('b','a', 15)
grafo2.nova_aresta('a','c', 5)
grafo2.nova_aresta('c','a', 5)
#grafo2.nova_aresta('b','d', 6)
grafo2.nova_aresta('c','d', 2)
grafo2.nova_aresta('d','c', 2)
grafo2.nova_aresta('d','a', 11)
grafo2.nova_aresta('a','d', 11)
grafo2.nova_aresta('d','b', 1)
grafo2.nova_aresta('b','d', 1)
'''

grafo2.nova_aresta('a','b', 4)
grafo2.nova_aresta('b','a', 4)

grafo2.nova_aresta('a','h', 8)
grafo2.nova_aresta('h','a', 8)

grafo2.nova_aresta('c','b', 8)
grafo2.nova_aresta('b','c', 8)

grafo2.nova_aresta('b','h', 11)
grafo2.nova_aresta('h','b', 11)

grafo2.nova_aresta('c','i', 2)
grafo2.nova_aresta('i','c', 2)

grafo2.nova_aresta('c','d', 7)
grafo2.nova_aresta('d','c', 7)

grafo2.nova_aresta('c','f', 4)
grafo2.nova_aresta('f','c', 4)

grafo2.nova_aresta('i','h', 7)
grafo2.nova_aresta('h','i', 7)

grafo2.nova_aresta('i','g', 6)
grafo2.nova_aresta('g','i', 6)

grafo2.nova_aresta('g','h', 1)
grafo2.nova_aresta('h','g', 1)

grafo2.nova_aresta('g','f', 2)
grafo2.nova_aresta('f','g', 2)

grafo2.nova_aresta('d','f', 14)
grafo2.nova_aresta('f','d', 14)

grafo2.nova_aresta('d','e', 9)
grafo2.nova_aresta('e','d', 9)

grafo2.nova_aresta('e','f', 10)
grafo2.nova_aresta('f','e', 10)
#grafo2.breadth_first_search('d')
#grafo2.depth_first_search()

'''
grafo2.novo_vertice('A')
grafo2.novo_vertice('B')
grafo2.novo_vertice('C')
grafo2.novo_vertice('D')
grafo2.novo_vertice('E')
grafo2.novo_vertice('F')
grafo2.novo_vertice('G')
grafo2.novo_vertice('H')

grafo2.nova_aresta('B','A', 42)
grafo2.nova_aresta('B', 'A', 42)
grafo2.nova_aresta('A', 'B', 42)
grafo2.nova_aresta('C', 'A', 61)
grafo2.nova_aresta('A', 'C', 61)
grafo2.nova_aresta('C', 'B', 14)
grafo2.nova_aresta('B', 'C', 14)
grafo2.nova_aresta('D', 'A', 30)
grafo2.nova_aresta('A', 'D', 30)
grafo2.nova_aresta('D', 'B', 87)
grafo2.nova_aresta('B', 'D', 87)
grafo2.nova_aresta('D', 'C', 20)
grafo2.nova_aresta('C', 'D', 20)
grafo2.nova_aresta('E', 'A', 17)
grafo2.nova_aresta('A', 'E', 17)
grafo2.nova_aresta('E', 'B', 28)
grafo2.nova_aresta('B', 'E', 28)
grafo2.nova_aresta('E', 'C', 81)
grafo2.nova_aresta('C', 'E', 81)
grafo2.nova_aresta('E', 'D', 34)
grafo2.nova_aresta('D', 'E', 34)
grafo2.nova_aresta('F', 'A', 82)
grafo2.nova_aresta('A', 'F', 82)
grafo2.nova_aresta('F', 'B', 70)
grafo2.nova_aresta('B', 'F', 70)
grafo2.nova_aresta('F', 'C', 21)
grafo2.nova_aresta('C', 'F', 21)
grafo2.nova_aresta('F', 'D', 33)
grafo2.nova_aresta('D', 'F', 33)
grafo2.nova_aresta('F', 'E', 41)
grafo2.nova_aresta('E', 'F', 41)
grafo2.nova_aresta('G', 'A', 31)
grafo2.nova_aresta('A', 'G', 31)
grafo2.nova_aresta('G', 'B', 19)
grafo2.nova_aresta('B', 'G', 19)
grafo2.nova_aresta('G', 'C', 8)
grafo2.nova_aresta('C', 'G', 8)
grafo2.nova_aresta('G', 'D', 91)
grafo2.nova_aresta('D', 'G', 91)
grafo2.nova_aresta('G', 'E', 34)
grafo2.nova_aresta('E', 'G', 34)
grafo2.nova_aresta('G', 'F', 19)
grafo2.nova_aresta('F', 'G', 19)
grafo2.nova_aresta('H', 'A', 11)
grafo2.nova_aresta('A', 'H', 11)
grafo2.nova_aresta('H', 'B', 33)
grafo2.nova_aresta('B', 'H', 33)
grafo2.nova_aresta('H', 'C', 29)
grafo2.nova_aresta('C', 'H', 29)
grafo2.nova_aresta('H', 'D', 10)
grafo2.nova_aresta('D', 'H', 10)
grafo2.nova_aresta('H', 'E', 82)
grafo2.nova_aresta('E', 'H', 82)
grafo2.nova_aresta('H', 'F', 32)
grafo2.nova_aresta('F', 'H', 32)
grafo2.nova_aresta('H', 'G', 59)
grafo2.nova_aresta('G', 'H', 59)
'''
'''
ini = time.time()
pai, key = grafo2.PRIM('a')
fin = time.time()
tempo_execucao = fin-ini
#for item in AGM:
    #print item
    #print( "Vertice: " + str(item.getId()) +") = " + str(item.getDistancia()))
for item in key:
    print key[item]
    #print( item + "Aresta("+ str(AGM[item].getPai()) +","+ str(AGM[item].getId()) +") = " + str(AGM[item].getDistancia()))
print ("TEMPO DE EXECUCAO: " + str(tempo_execucao))
'''
#grafo.imprime_grafo('a', 'd')

vetor = []
#vetor = [1, 5, 2, 2, 7, 4, 1, 3]
vetor = [10, 76, 95, 193, 181, 56, 183, 105, 141, 137]
#for i in range(0,10):
#    vetor.append(random.randrange(255))
print vetor
#subsets = grafo.generate_mti(vetor)
subsets = grafo.generate_mti_rank_path_compression(vetor)
print vetor
for item in subsets:
    print("Pai: " + str(subsets[item].pai) + "  Item: " + str(subsets[item].numero)) 


subcadeia = SubCadeia()


'''
#Exemplo 1
X = "ABCB"
Y = "BDCAB"
print len(X)
print len(Y)
#tamanho_sub_cadeia = subcadeia.SCM(X,len(X),Y,len(Y))[0]
print ("Cadeia 1: " + X)
print ("Tamanho Cadeia 1: " + str(len(X)))
print ("Cadeia 2: " + Y)
print ("Tamanho Cadeia 2: " + str(len(Y)))

tamanho_sub_cadeia = subcadeia.SCM_memoizado(X,len(X),Y,len(Y))
print ("Tamanho da subcadeia: " + str(tamanho_sub_cadeia))
subcadeia.imprimir_matriz_c(len(X),len(Y))
subcadeia.imprimir_matriz_b(len(X),len(Y))
subcadeia.recupera_SCM(X,len(X),len(Y))
print("Maior Subcadeia encontrada: ")
print(subcadeia.getSubcadeia())

#Exemplo 2
X = "AABCBB"
Y = "FABABDCKBJB"
print len(X)
print len(Y)
print ("Cadeia 1: " + X)
print ("Tamanho Cadeia 1: " + str(len(X)))
print ("Cadeia 2: " + Y)
print ("Tamanho Cadeia 2: " + str(len(Y)))
tamanho_sub_cadeia = subcadeia.SCM_memoizado(X,len(X),Y,len(Y))
print ("Tamanho da subcadeia: " + str(tamanho_sub_cadeia))
subcadeia.imprimir_matriz_c(len(X),len(Y))
subcadeia.imprimir_matriz_b(len(X),len(Y))
subcadeia.recupera_SCM(X,len(X),len(Y))
print("Maior Subcadeia encontrada: ")
print(subcadeia.getSubcadeia())'''