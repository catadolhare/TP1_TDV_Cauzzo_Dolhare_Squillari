import json
import numpy as np
import funciones
import time
import matplotlib.pyplot as plt

BIG_NUMBER = 1e10 # Revisar si es necesario.

def main():
	print("Seleccione una instancia a aproximar:")
	print("1. aspen_simulation.json")
	print("2. ethanol_water_vle.json")
	print("3. optimistic_instance.json")
	print("4. titanium.json")
	print("5. toy_instance.json")
	archivo_eleccion = input("Instancia: ")

	if(archivo_eleccion == "1"):
		instance_name = "aspen_simulation.json"
	elif(archivo_eleccion == "2"):
		instance_name = "ethanol_water_vle.json"
	elif(archivo_eleccion == "3"):
		instance_name = "optimistic_instance.json"
	elif(archivo_eleccion == "4"):
		instance_name = "titanium.json"
	elif(archivo_eleccion == "5"):
		instance_name = "toy_instance.json"

	filename = "././data/" + instance_name
	with open(filename) as f:
		instance = json.load(f)
	
	cant_bp = input("Ingrese la cantidad de breakpoints: ")
	K = int(cant_bp)

	valor_m1 = input("Ingrese el valor de m1: ")
	m1 = int(valor_m1)

	valor_m2 = input("Ingrese el valor de m2: ")
	m2 = int(valor_m2)

	N=5

	# Definir grilla de m1 x m2.
	grid_x = np.linspace(min(instance["x"]), max(instance["x"]), num=m1, endpoint=True)
	grid_y = np.linspace(min(instance["y"]), max(instance["y"]), num=m2, endpoint=True)
	print("Valores del eje x de la grilla:")
	print(grid_x)
	print("Valores del eje y de la grilla:")
	print(grid_y)

	# TODO: aca se deberia ejecutar el algoritmo.

	algoritmo = input("Ingrese el algoritmo a utilizar (1: Fuerza Bruta, 2: Backtracking, 3: Programación Dinamica): ")

	if algoritmo == "1":
		inicio = time.time()
		minimo_main, error_minimo_main = funciones.llamada_fuerza_bruta([], K, m1, m2, grid_x, grid_y, instance["x"], instance["y"])
		fin = time.time()
	elif algoritmo == "2":
		inicio = time.time()
		minimo_main, error_minimo_main = funciones.llamada_backtracking([], K, m1, m2, grid_x, grid_y, instance["x"], instance["y"])
		fin = time.time()
	elif algoritmo == "3":
		inicio = time.time()
		minimo_main, error_minimo_main = funciones.llamada_programacion_dinamica(K-1, m1, m2, grid_x, grid_y, instance["x"], instance["y"],)
		fin = time.time()
	
	tiempo = fin - inicio
	print('tiempo = ', tiempo)
	print('breakpoints = ', minimo_main)
	print('error = ', error_minimo_main)

	best = {}
	best['sol'] = [None]*(N+1)
	best['obj'] = BIG_NUMBER
	best['tiempo'] = 0
	
	# Posible ejemplo (para la instancia titanium) de formato de solucion, y como exportarlo a JSON.
	# La solucion es una lista de tuplas (i,j), donde:
	# - i indica el indice del punto de la discretizacion de la abscisa
	# - j indica el indice del punto de la discretizacion de la ordenada.
	best['sol'] = minimo_main
	best['obj'] = error_minimo_main
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

	plt.plot(instance['x'], instance['y'], 'k.')
	plt.plot(solution['x'], solution['y'], 'r-')
	titulo = "Solución para " + instance_name + " con " + str(K) + " breakpoints"
	plt.title(titulo)
	plt.legend(["Datos", "Aproximación PWL"])
	plt.grid(True)
	plt.xticks(grid_x)
	plt.yticks(grid_y)
	plt.show()

	# Se guarda el archivo en formato JSON
	with open('solution_' + algoritmo + 'py' + str(m1) +'' + str(m2) + '' + str(K) + '_' + instance_name, 'w') as f:
		json.dump(solution, f)

if __name__ == "__main__":
	main()