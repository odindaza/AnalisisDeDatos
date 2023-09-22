import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#Leyendo y mostrando los datos del archivo
data = pd.read_csv("framingham.csv", sep=",")
data
#Mostrando la grafica con los datos
data[["age","currentSmoker"]].plot.scatter(x="age",y="currentSmoker")
#Parametros
w = 0.1
b = -3.9
#Configurando la recta
x = np.linspace(0,data["age"].max(),100)
y = 1/(1+np.exp(-(w*x+b)))
#Configurando la grafica
data.plot.scatter(x="age",y="currentSmoker")
plt.plot(x,y,"-r")
plt.ylim(0,data["currentSmoker"].max()*1.1)
#Mostrando la grafica
plt.show()
