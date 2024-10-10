from time import sleep

import numpy as np

array = np.array([1, 2, 3, 4])
print(array)

soma = np.sum(array)
print(f"Soma: {soma}")

sleep(2)

import pandas as pd

data = {
    'Nome': ['Felipe', 'Patricia', 'Thor'],
    'Idade': [24, 30, 10],
    'Estado': ['SP', 'PR', 'SP']
}

df = pd.DataFrame(data)

print(df)
print(df.describe())

sleep(2)

import matplotlib.pyplot as plt

x = [0, 50, 100, 150, 200]
y = [0, 20, 40, 60, 80]

plt.plot(x, y)
plt.title('Gráfico')
plt.xlabel('Distância(m)')
plt.ylabel('Velocidade(km/h')
plt.show()

print(15*"-=")
print("       Fim do Programa!")
print(15*"-=")
