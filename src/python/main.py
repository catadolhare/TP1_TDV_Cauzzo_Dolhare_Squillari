import json
import numpy as np
import funciones
import time

BIG_NUMBER = 1e10 # Revisar si es necesario.

def main():

	# Ejemplo para leer una instancia con json
	instance_name = "titanium.json"
	filename = "././data/" + instance_name
	with open(filename) as f:
		instance = json.load(f)
	
	K = 6
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
	inicio = time.time()
	breakpoints, error_minimo = funciones.backtracking(breakpoints, K, m1, m2, grid_x, grid_y, instance["x"], instance["y"])
	fin = time.time()
	tiempo = fin - inicio
	print(tiempo)
	print(breakpoints)
	print(error_minimo)

	best = {}
	best['sol'] = [None]*(N+1)
	best['obj'] = BIG_NUMBER
	best['tiempo'] = 0
	
	# Posible ejemplo (para la instancia titanium) de formato de solucion, y como exportarlo a JSON.
	# La solucion es una lista de tuplas (i,j), donde:
	# - i indica el indice del punto de la discretizacion de la abscisa
	# - j indica el indice del punto de la discretizacion de la ordenada.
	best['sol'] = breakpoints
	best['obj'] = error_minimo
	best['tiempo'] = tiempo

	# Represetnamos la solucion con un diccionario que indica:
	# - n: cantidad de breakpoints
	# - x: lista con las coordenadas de la abscisa para cada breakpoint
	# - y: lista con las coordenadas de la ordenada para cada breakpoint
	solution = {}
	solution['n'] = len(best['sol'])
	solution['x'] = [grid_x[x[0]] for x in best['sol']]
	solution['y'] = [grid_y[x[1]] for x in best['sol']]
	solution['obj'] = best['obj']
	solution['tiempo'] = best['tiempo']

	# Se guarda el archivo en formato JSON
	with open('solution_backtracking_' + str(m1) +'_' + str(m2) + '_' + str(K) + '_' + instance_name, 'w') as f:
		json.dump(solution, f)

	
if __name__ == "__main__":
	main()