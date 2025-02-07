class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)

    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izquierda)
            print(nodo.valor, end=" ")
            self.inorden(nodo.derecha)

    def postorden(self, nodo):
        if nodo:
            self.postorden(nodo.izquierda)
            self.postorden(nodo.derecha)
            print(nodo.valor, end=" ")


def evaluar_arbol(nodo):
    if nodo is None:
        return 0
    if isinstance(nodo.valor, int):  
        return nodo.valor

    izquierda = evaluar_arbol(nodo.izquierda)
    derecha = evaluar_arbol(nodo.derecha)
    
   
    if nodo.valor == '+':
        return izquierda + derecha
    elif nodo.valor == '-':
        return izquierda - derecha
    elif nodo.valor == '*':
        return izquierda * derecha
    elif nodo.valor == '/':
        return izquierda / derecha if derecha != 0 else None


nodo_raiz = Nodo('*')
nodo_raiz.izquierda = Nodo('+')
nodo_raiz.izquierda.izquierda = Nodo(3)
nodo_raiz.izquierda.derecha = Nodo(5)
nodo_raiz.derecha = Nodo(2)


resultado = evaluar_arbol(nodo_raiz)

arbol = ArbolBinario()
valores = [10, 5, 15, 3, 7, 12, 18]
for valor in valores:
    arbol.insertar(valor)

print("Recorrido Preorden:")
arbol.preorden(arbol.raiz)
print("\nRecorrido Inorden:")
arbol.inorden(arbol.raiz)
print("\nRecorrido Postorden:")
arbol.postorden(arbol.raiz)
print("\nResultado de la expresion (3 + 5) * 2:", resultado)
