# Proyecto 5 - Disposición de grafos - parte I

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

**INSTITUTO POLITÉCNICO NACIONAL**

**Centro de Investigación en Computación**

**PRESENTA** Victor Christian Jaime Tamayo

**BOLETA** A210232

**ASIGNATURA** Diseño y Análisis de Algoritmos

**PROFESOR** Dr. Rolando Quintero Téllez

**SEMESTRE** A21

**FECHA** 21 de Junio de 2021

---

## Instrucciones

Dado un grafo, y utilizando pygame, generar una visualización del mismo. Mediante dos métodos:
- Spring: calcula la disposición de un grafo mediante el algoritmo de resortes presentado por P. Eades (1984). O(m+n)

Entregables:
- Repositorio GIT
- Capturas de pantalla (links a videos) con la ejecución del proyecto. Dos por cada modelo de generación, uno con 100 nodos y otro con 500.


---

## Modelo Gm,n de malla
- m: número de columnas
- n: número de filas
- dirigido: el grafo es dirigido

##

### 100 nodos (Modelo Gm,n de malla)
**m = 10, n = 10, dirigido = False**

[![GRAFO_MALLA_100](/img/GRAFO_MALLA_100.PNG)](https://www.youtube.com/watch?v=3XNFgLX7PIo)

>[Ver en YouTube](https://www.youtube.com/watch?v=3XNFgLX7PIo)

##

### 289 nodos (Modelo Gm,n de malla)
**m = 17, n = 17, dirigido = False**

[![GRAFO_MALLA_289](/img/GRAFO_MALLA_289.PNG)](https://www.youtube.com/watch?v=uncQHZ-XuJA)

>[Ver en YouTube](https://www.youtube.com/watch?v=uncQHZ-XuJA)


##


---

## Modelo Gn,m de Erdös y Rényi
- n: número de nodos (> 0)
- m: número de aristas (>= n-1)
- dirigido: el grafo es dirigido?
- auto: permitir auto-ciclos?

##

### 100 nodos (Modelo Gn,m de Erdös y Rényi)
**n = 100, m = 100, dirigido = False, auto=False**

[![ERDOS_100](/img/ERDOS_100.PNG)](https://www.youtube.com/watch?v=pok46h8rKUo)

>[Ver en YouTube](https://www.youtube.com/watch?v=pok46h8rKUo)

##

### 180 nodos (Modelo Gn,m de Erdös y Rényi)
**n = 180, m = 150, dirigido = False, auto=False**

[![ERDOS_180](/img/ERDOS_180.PNG)](https://www.youtube.com/watch?v=hwCnme5mw6s)

>[Ver en YouTube](https://www.youtube.com/watch?v=hwCnme5mw6s)

##

### 400 nodos (Modelo Gn,m de Erdös y Rényi)
**n = 400, m = 200, dirigido = False, auto=False**

[![ERDOS_400](/img/ERDOS_400.PNG)](https://www.youtube.com/watch?v=pSEIADjMB2g)

>[Ver en YouTube](https://www.youtube.com/watch?v=pSEIADjMB2g)

##

---

## Modelo Gn,p de **Gilbert**
- n: número de nodos (> 0)
- p: probabilidad de crear una arista (0, 1)
- dirigido: el grafo es dirigido?
- auto: permitir auto-ciclos?

##

### 100 nodos (Modelo Gn,p de Gilbert)
**n = 100, p = 0.1, dirigido = False, auto=False**

[![GILBERT_100](/img/GILBERT_100.PNG)](https://www.youtube.com/watch?v=8ASXGPjfktg)

>[Ver en YouTube](https://www.youtube.com/watch?v=8ASXGPjfktg)


##

### 500 nodos (Modelo Gn,p de Gilbert)
**n = 500, p = 0.1, dirigido = False, auto=False**

[![GILBERT_500](/img/GILBERT_500.PNG)](https://www.youtube.com/watch?v=_pP7ClPGpsM)

>[Ver en YouTube](https://www.youtube.com/watch?v=_pP7ClPGpsM)


##

---

## Modelo Gn,r **geográfico simple**
- n: número de nodos (> 0)
- r: distancia máxima para crear un nodo (0, 1)
- dirigido: el grafo es dirigido?
- auto: permitir auto-ciclos?

##

### 100 nodos (Modelo Gn,r Geográfico simple)
**n = 100, r = 0.3, dirigido = False, auto=False**


[![GEOGRAFICO_100](/img/GEOGRAFICO_100.PNG)](https://www.youtube.com/watch?v=OGbUKRpw1xY)

>[Ver en YouTube](https://www.youtube.com/watch?v=OGbUKRpw1xY)

##

---

## Variante del modelo Gn,d **Barabási-Albert**
- n: número de nodos (> 0)
- d: grado máximo esperado por cada nodo (> 1)
- dirigido: el grafo es dirigido?
- auto: permitir auto-ciclos?

##

### 100 nodos (Variante del modelo Gn,d Barabási-Albert)
**n = 30, d = 4, dirigido = False, auto=False**

[![BARABASI_100](/img/BARABASI_100.PNG)](https://www.youtube.com/watch?v=CJa8EBXT3bs)

>[Ver en YouTube](https://www.youtube.com/watch?v=CJa8EBXT3bs)

##

---

## Modelo Gn **Dorogovtsev-Mendes**
- n: número de nodos (≥ 3)
- dirigido: el grafo es dirigido?

##

### 100 nodos (Modelo Gn Dorogovtsev-Mendes)
**n = 30, dirigido = False**

[![DOROGVTSEV_100](/img/DOROGVTSEV_100.PNG)](https://www.youtube.com/watch?v=V8WMTf-rH1Y)

>[Ver en YouTube](https://www.youtube.com/watch?v=V8WMTf-rH1Y)

##


---
