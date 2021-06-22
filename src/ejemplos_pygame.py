import datetime
x = datetime.datetime.now()
print(x)
#******************************************************************************
nodo_raiz=7
print('nodo_raiz: ',nodo_raiz)
#******************************************************************************
from grafoMalla import grafoMalla
from grafoGeografico import grafoGeografico
from grafoErdosRenyi import grafoErdosRenyi
from grafoGilbert import grafoGilbert
from grafoBarabasiAlbert import grafoBarabasiAlbert
from grafoDorogovtsevMendes import grafoDorogovtsevMendes
#******************************************************************************
'''
#gfGeografico - 100 nodos
gfGeografico = grafoGeografico(n=100, r=0.3, dirigido=False, auto=False)
gfGeografico.display()
gfGeografico.playSpringAnimation("grafoGeografico 100 nodos")
'''

gfGeografico = grafoGeografico(n=500, r=0.12, dirigido=False, auto=False)
gfGeografico.display()
gfGeografico.playSpringAnimation("grafoGeografico 500 nodos")

'''
#gfMalla - 100 nodos
gfMalla = grafoMalla(10,10,dirigido=False)
gfMalla.display()
gfMalla.playSpringAnimation("grafo Malla 100 nodos")
'''
'''
gfMalla = grafoMalla(15,12,dirigido=False)
gfMalla.display()
gfMalla.playSpringAnimation("grafo Malla 100 nodos")
'''
'''
gfMalla = grafoMalla(17,17,dirigido=False)
gfMalla.display()
gfMalla.playSpringAnimation("grafo Malla 289 nodos")
'''
'''
#gfErdosReny - 100 nodos
gfErdosReny = grafoErdosRenyi(n=100, m=100, dirigido=False, auto=False)
gfErdosReny.display()
gfErdosReny.playSpringAnimation("grafo Erdos Renyi 100 nodos")
'''
'''
#gfErdosReny - 500 nodos
gfErdosReny = grafoErdosRenyi(n=400, m=200, dirigido=False, auto=False)
gfErdosReny.display()
gfErdosReny.playSpringAnimation("grafo Erdos Renyi 400 nodos")
'''

'''
#grafoGilbert - 100 nodos
gfGilbert = grafoGilbert(n=100, p=0.1, dirigido=False, auto=False)
gfGilbert.display()
gfGilbert.playSpringAnimation("grafo Gilbert 100 nodos")
'''
'''
#grafoGilbert - 100 nodos
gfGilbert = grafoGilbert(n=500, p=0.1, dirigido=False, auto=False)
gfGilbert.display()
gfGilbert.playSpringAnimation("grafo Gilbert 500 nodos")
'''

'''
#grafoBarabasiAlbert - 100 nodos
gfBarabasiAlbert = grafoBarabasiAlbert(n=100, d=4, dirigido=False, auto=False)
gfBarabasiAlbert.display()
gfBarabasiAlbert.playSpringAnimation("grafo Barabási-Albert 100 nodos")
'''
'''
#grafoBarabasiAlbert - 100 nodos
gfDorogovtsevMendes = grafoDorogovtsevMendes(100,dirigido=False)
gfDorogovtsevMendes.display()
gfDorogovtsevMendes.playSpringAnimation("grafo Dorogovtsev-Mendes 100 nodos")
'''
#******************************************************************************
