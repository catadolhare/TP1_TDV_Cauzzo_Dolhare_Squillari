import json
import numpy as np
import funciones

BIG_NUMBER = 1e10 # Revisar si es necesario.

def main():

	# Ejemplo para leer una instancia con json
	instance_name = "titanium.json"
	filename = "././data/" + instance_name
	with open(filename) as f:
		instance = json.load(f)
	
	K = instance["n"]
	m1 = 6
	m2 = 6
	N = 5

	# Definir grilla de m x n.
	grid_x = np.linspace(min(instance["x"]), max(instance["x"]), num=m1, endpoint=True)
	grid_y = np.linspace(min(instance["y"]), max(instance["y"]), num=m2, endpoint=True)
	print(grid_x)
	print(grid_y)

	# TODO: aca se deberia ejecutar el algoritmo.

	breakpoints = []
	global error_minimo 
	error_minimo = BIG_NUMBER
	global minimo 
	minimo = []
	global error_total 
	error_total = 0
	breakpoints, error_minimo = funciones.programacion_dinamica(breakpoints, K, K-1, m1, m2, 0, 0, {}, grid_x, grid_y, instance["x"], instance["y"])
	print(breakpoints)
	print(error_minimo)

	best = {}
	best['sol'] = [None]*(N+1)
	best['obj'] = BIG_NUMBER
	
	# Posible ejemplo (para la instancia titanium) de formato de solucion, y como exportarlo a JSON.
	# La solucion es una lista de tuplas (i,j), donde:
	# - i indica el indice del punto de la discretizacion de la abscisa
	# - j indica el indice del punto de la discretizacion de la ordenada.
	best['sol'] = breakpoints
	best['obj'] = error_minimo

	# Represetnamos la solucion con un diccionario que indica:
	# - n: cantidad de breakpoints
	# - x: lista con las coordenadas de la abscisa para cada breakpoint
	# - y: lista con las coordenadas de la ordenada para cada breakpoint
	solution = {}
	solution['n'] = len(best['sol'])
	solution['x'] = [grid_x[x[0]] for x in best['sol']]
	solution['y'] = [grid_y[x[1]] for x in best['sol']]
	solution['obj'] = best['obj']

	# Se guarda el archivo en formato JSON
	with open('solution_pd_6_6_5' + instance_name, 'w') as f:
		json.dump(solution, f)

	
if __name__ == "__main__":
	main()