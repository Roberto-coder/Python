import numpy as np
import matplotlib.pyplot as plt

X = np.array([2019, 2020, 2021, 2022, 2023, 2024])
yd = np.array([4.0, 5.0 ,6.5 ,7.0 ,8.5 ,12.0])

X_norm = normalizacion(X)

def normalizacion(X):
    X_max = max(X)
    X_min = min(X)
    return (X-X_min)/(X_max-X_min)

X_test = float(input("Introdusca el año a predecir"))
X_norm= normalizacion(X_test)
Y_test = b0 + b1*X_norm
print("Para el año {X_test} se estiman {Y_test} millones de ventas")

X = X_norm

## Definicion de los hiperparametros
lr = 0.01
epocas = 5000
b0 = 0.1 ## Se recomienda inicializar entre 0 y 1 de forma random
b1 = 0.2
##
## B = np.array(dimension = m)

lamda = 0.001

m = len(X)
grafica = []

for epoch in range(epocas):
    Yobt = b0 + b1*X
    
    ## Calculo de la funcion de costo ECM
    J = (1/(2*m))*np.sum((Yobt-yd)**2) + (lamda/2)*np.sum(b1**2)
    grafica += [J]
    
    ## Calculo de B0 y B
    b0 = b0 - lr*(1/m)*np.sum(Yobt-yd)
    b1 = b1 - lr*(1/m)*np.sum((Yobt-yd)*X) + (lamda/m)*b1
    
print("Parametro b0: ",b0)
print("Parametro b1: ",b1)

##Graficar J
plt.figure(figsize=(8,6))
plt.plot(range(len(grafica)) ,grafica, label = "Funcion de costo")
plt.xlabel("Epocas")
plt.ylabel("Funcion de costo")
plt.title("Funcion de costo vs Epocas")
plt.legend()
plt.show()


##Graficar los datos

plt.figure(figsize=(8,6))
for i in range(m):
    plt.scatter(X[i],yd[i], color = "blue")
    
x_val = [min(X),max(X)]
y_val = [b0 + b1*X for X in x_val]
plt.plot(x_val,y_val, color = "red")   
plt.show() 

