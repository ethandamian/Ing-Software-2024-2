import matplotlib.pyplot as plt
import numpy as np


def funcion(x):
    return x * np.log(x)


def graficar():
    plt.figure(figsize=(10,6))
    x_valores = np.linspace(0.1,10000,1000)

    y_values = funcion(x_valores)
    plt.plot(x_valores, y_values, linestyle='-', color='r')

    plt.xlabel("Valores en x del 0 al 10000")
    plt.ylabel("Valores en y")
    plt.title("GRAFICA DE LA FUNCION x log(x)")

    plt.show()

if __name__ == '__main__':
    graficar()