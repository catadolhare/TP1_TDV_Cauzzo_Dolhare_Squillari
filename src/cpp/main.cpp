#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include "funciones.h"
using namespace std;
#include "include/json.hpp"
// Para libreria de JSON.
using namespace nlohmann;


int main(int argc, char** argv) {
    //std::string instance_name = "../../data/titanium.json";
    
    cout<< "Seleccione una instancia a aproximar:" << endl;
	cout<<"1. aspen_simulation.json"<<endl;
	cout<<"2. ethanol_water_vle.json"<<endl;
	cout<<"3. optimistic_instance.json"<<endl;
	cout<<"4. titanium.json"<<endl;
	cout<<"5. toy_instance.json"<<endl;
	string archivo_eleccion;
    cout << "Instancia: ";
    cin >> archivo_eleccion;

	string instance_name;
    if(archivo_eleccion == "1") {
        instance_name = "../../data/aspen_simulation.json";
    } else if(archivo_eleccion == "2") {
        instance_name = "../../data/ethanol_water_vle.json";
    } else if(archivo_eleccion == "3") {
        instance_name = "../../data/optimistic_instance.json";
    } else if(archivo_eleccion == "4") {
        instance_name = "../../data/titanium.json";
    } else if(archivo_eleccion == "5") {
        instance_name = "../../data/toy_instance.json";
    }
    std::cout << "Reading file " << instance_name << std::endl;
    std::ifstream input(instance_name);

    json instance;
    input >> instance;
    input.close();

    int K;
    cout << "Ingrese la cantidad de breakpoints: ";
    cin >> K;

    int m1;
    cout << "Ingrese el valor de m1: ";
    cin >> m1;

    int m2;
    cout << "Ingrese el valor de m2: ";
    cin >> m2;

    int N = 5;
    //std::cout << K << std::endl;

    // Aca empieza la magia.
    vector<float> grid_x = discretizar(instance["x"], m1);
    vector<float> grid_y = discretizar(instance["y"], m2);
    vector<float> valores_x=instance["x"];
    vector<float> valores_y=instance["y"];
    vector<vector<int>> B={};
    tuple<vector<vector<int>>, float> solucion;
    cout << "Ingrese el algoritmo a utilizar (1: Fuerza Bruta, 2: Backtracking, 3: ProgramaciÃ³n DinÃ¡mica): ";
    string algoritmo;
    cin >> algoritmo;

    if (algoritmo == "1") {
        clock_t inicio = clock();
        solucion=llamada_fuerza_bruta(B, K, m1, m2, grid_x, grid_y, valores_x, valores_y);
        clock_t fin = clock();
        double tiempo = double(fin - inicio) / CLOCKS_PER_SEC;
        cout << "tiempo = " << tiempo << endl;
        
    } else if (algoritmo == "2") {
        clock_t inicio = clock();
        solucion=llamada_backtracking(B, K, m1, m2, grid_x, grid_y, valores_x, valores_y);
        clock_t fin = clock();
        double tiempo = double(fin - inicio) / CLOCKS_PER_SEC;
        cout << "tiempo = " << tiempo << endl;
        
    } else if (algoritmo == "3") {
        clock_t inicio = clock();
        solucion = llamada_programacion_dinamica(K-1, m1, m2, grid_x, grid_y, valores_x, valores_y);
        clock_t fin = clock();
        double tiempo = double(fin - inicio) / CLOCKS_PER_SEC;
        cout << "tiempo = " << tiempo << endl;
        
    }

    cout << "Grid_x: " << endl;
    for(int i = 0;  i < grid_x.size(); i++){
        cout << grid_x[i] << " ";
    }
    cout << endl;
    cout << "Grid_y: " << endl;
    for(int i = 0;  i < grid_y.size(); i++){
        cout << grid_y[i] << " ";
    }
    cout << endl;

    vector<vector<int>> minimo_sol = get<0>(solucion);
    float error_minimo_sol = get<1>(solucion);
    cout << "Breakpoints:" << endl;
    for(int i = 0;  i < minimo_sol.size(); i++){
        cout << "[" << minimo_sol[i][0] << ", " << minimo_sol[i][1] << ']' << endl;
    }
    cout << "Error: " << error_minimo_sol << endl;

    // Ejemplo para guardar json.
    // Probamos guardando el mismo JSON de instance, pero en otro archivo.
    std::ofstream output("test_output.out");

    output << instance;
    output.close();

    return 0;
}