import matplotlib.pyplot as plt
import json
import numpy as np

solution_name = "solution_fuerza_bruta_6_6_6_titanium.json"
filename = "././" + solution_name
with open(filename) as f:
	solution = json.load(f)
	
K = 5
m1 = 6
m2 = 6
N = 5

instance_name = "titanium.json"
filename = "././data/" + instance_name
with open(filename) as f:
	instance = json.load(f)
	
# Definir grilla de m x n.
grid_x = np.linspace(min(instance["x"]), max(instance["x"]), num=m1, endpoint=True)
grid_y = np.linspace(min(instance["y"]), max(instance["y"]), num=m2, endpoint=True)


x_sol = solution['x']
y_sol = solution['y']
k = solution['n']
tiempo = solution['tiempo']

x = instance["x"]
y = instance["y"]

plt.plot(x, y, 'k.')
plt.plot(x_sol, y_sol, 'r-')
titulo = "Solución para " + instance_name + " con " + str(k) + " breakpoints"
plt.title(titulo)
plt.legend(["Datos", "Aproximación PWL"])
plt.grid(True)
plt.xticks(grid_x)
plt.yticks(grid_y)
plt.show()