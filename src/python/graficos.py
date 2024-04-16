import matplotlib.pyplot as plt
import json

solution_name = "solution_fuerza_bruta_6_6_6_titanium.json"
filename = "././" + solution_name
with open(filename) as f:
	solution = json.load(f)
	
instance_name = "titanium.json"
filename = "././data/" + instance_name
with open(filename) as f:
	instance = json.load(f)
	
x_sol = solution['x']
y_sol = solution['y']
k = solution['n']
tiempo = solution['tiempo']

x = instance["x"]
y = instance["y"]

plt.plot(x, y, 'k.')
plt.plot(x_sol, y_sol, 'red')
plt.show()