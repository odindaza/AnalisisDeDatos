import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#Leyendo y mostrando los datos del archivos
data = pd.read_csv("data.csv", sep=",")
data
#Graficando los datos del archivo
data.plot.scatter(x="metro", y="precio")
plt.show()
#Parámetros de la recta
w = 5
b = 350
#Configurando la recta
x = np.linspace(0,data['metro'].max(),100)
y = w*x+b
#Graficando la recta con los nuevos puntos
data.plot.scatter(x="metro", y="precio")
plt.plot(x, y, "-r")
plt.ylim(0,data["precio"].max()*1.1)
#Mostrando la grafica
plt.show()
