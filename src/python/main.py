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
	m = 6
	n = 6
	N = 5

	# Definir grilla de m x n.
	grid_x = np.linspace(min(instance["x"]), max(instance["x"]), num=m, endpoint=True)
	grid_y = np.linspace(min(instance["y"]), max(instance["y"]), num=n, endpoint=True)
	print(grid_x)
	print(grid_y)

	# TODO: aca se deberia ejecutar el algoritmo.

	breakpoints = []
	error_minimo = BIG_NUMBER
	minimo = []
	error_total = 0
	breakpoints, error_minimo = funciones.fuerza_bruta(breakpoints, 5, m, n, grid_x, grid_y, instance['x'], instance['y'], minimo, error_total, error_minimo)
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
	with open('solution_' + instance_name, 'w') as f:
		json.dump(solution, f)

	
if __name__ == "__main__":
	main()