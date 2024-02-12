def conteo_valles(recorrido):
    no_valles = 0
    nivel_del_mar = 0
    esta_en_valle = False

    for letra in recorrido:
        if letra == 'U':
            nivel_del_mar += 1
        else:
            nivel_del_mar -= 1

        if nivel_del_mar == 0 and letra == 'D':
            esta_en_valle = True

        elif nivel_del_mar == 0 and esta_en_valle == True:
            no_valles += 1
            esta_en_valle = False
            pasos_por_debajo = 0

    return no_valles




class Nodo:

    def __init__(self, valor=None):
        self.valor = valor
        self.hijoI = None
        self.hijoD = None

    def __str__(self):
        return str(f"({self.valor}, {self.hijoI}, {self.hijoD})")

class ArbolOrdenado:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self.agregar_nodo(self.raiz,valor)

    def agregar_nodo(self, nodo_a_insertar: Nodo, valor):
        if valor <= nodo_a_insertar.valor:
            if nodo_a_insertar.hijoI is None:
                nodo_a_insertar.hijoI = Nodo(valor)
            else:
                self.agregar_nodo(nodo_a_insertar.hijoI, valor)
        elif valor >= nodo_a_insertar.valor:
            if nodo_a_insertar.hijoD is None:
                nodo_a_insertar.hijoD = Nodo(valor)
            else:
                self.agregar_nodo(nodo_a_insertar.hijoD,   valor)

    def pre_orden(self):
        return self.pre_orden_auxiliar(self.raiz)

    def pre_orden_auxiliar(self, nodo_raiz):
        if nodo_raiz is None:
            return []
        resultado = [nodo_raiz.valor]

        # extend sirve para concatenar una lista(u objetos iterables) al final de otra
        resultado.extend(self.pre_orden_auxiliar(nodo_raiz.hijoI))
        resultado.extend(self.pre_orden_auxiliar(nodo_raiz.hijoD))
        return resultado

    def in_orden(self):
        return self.in_orden_auxiliar(self.raiz)

    def in_orden_auxiliar(self, nodo_raiz):
        if nodo_raiz is None:
            return []
        resultado = []
        resultado.extend(self.in_orden_auxiliar(nodo_raiz.hijoI))
        resultado.append(nodo_raiz.valor)
        resultado.extend(self.in_orden_auxiliar(nodo_raiz.hijoD))


        return resultado

    def post_orden(self):
        return self.post_orden_auxiliar(self.raiz)

    def post_orden_auxiliar(self, nodo_raiz):
        if nodo_raiz is None:
            return []
        resultado = []
        resultado.extend(self.post_orden_auxiliar(nodo_raiz.hijoI))
        resultado.extend(self.post_orden_auxiliar(nodo_raiz.hijoD))
        resultado.append(nodo_raiz.valor)
        return resultado






if __name__ == '__main__':
    print("RECORRIDO: \n")
    recorrido = "UUDDDDUU"
    print(conteo_valles(recorrido))

    print("Arbol Binario Ordenado:")
    arbol = ArbolOrdenado()
    arbol.agregar(5)
    arbol.agregar(3)
    arbol.agregar(8)
    arbol.agregar(1)
    arbol.agregar(4)

    print("Recorrido pre-orden:", arbol.pre_orden())
    print("Recorrido in-orden:", arbol.in_orden())
    print("Recorrido post-orden:", arbol.post_orden())


