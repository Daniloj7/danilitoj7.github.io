import numpy as np
import pandas as pd
from pandas import Series
lista_enteros = np.random.randint(10, 101, size=10)
print(f"Lista de enteros aleatorios: {lista_enteros}")

indices = np.arange(1, 11) 
serie_original = Series(lista_enteros, index=indices)
print(f"\nSerie con índices personalizados:\n{serie_original}")
serie_cuadrados = serie_original ** 2
print(f"\nSerie con los cuadrados de los valores:\n{serie_cuadrados}")
print(f"\nLos 4 últimos elementos de la serie de cuadrados:\n{serie_cuadrados.tail(4)}")

numeros_mayores_500 = serie_cuadrados[serie_cuadrados > 500].tolist()
print(f"\nNúmeros mayores a 500 (como lista): {numeros_mayores_500}")