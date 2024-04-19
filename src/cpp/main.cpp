#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include "funciones.h"
using namespace std;
//#include "funciones.h"
#include "include/json.hpp"
// Para libreria de JSON.
using namespace nlohmann;


int main(int argc, char** argv) {
    std::string instance_name = "../../data/titanium.json";
    std::cout << "Reading file " << instance_name << std::endl;
    std::ifstream input(instance_name);

    json instance;
    input >> instance;
    input.close();

    int K = 5; //instance["n"];
    int m = 6;
    int n = 6;
    int N = 5;

    std::cout << K << std::endl;

    // Aca empieza la magia.
    vector<float> grid_x = discretizar(instance["x"], m);
    vector<float> grid_y = discretizar(instance["y"], n);
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


    vector<vector<int>> breakpoints = {};
    vector<float> valores_x = instance["x"];
    vector<float> valores_y = instance["y"];

    tuple<vector<vector<int>>, float> solucion = llamada_programacion_dinamica(K-1, m, n, grid_x, grid_y, valores_x, valores_y);
    vector<vector<int>> minimo_sol = get<0>(solucion);
    float error_minimo_sol = get<1>(solucion);

    cout << "Breakpoints:" << endl;
    for(int i = 0;  i < minimo_sol.size(); i++){
        cout << "[" << minimo_sol[i][0] << ", " << minimo_sol[i][1] << ']' << endl;
    }
    cout << "Error: " << error_minimo_sol << endl;
    

   // tuple<vector<vector<int>>, float> solu=llamada_backtracking(breakpoints, 5, m, n, grid_x, grid_y, valores_x, valores_y);
    //cout<< solucion << endl;
    // Ejemplo para guardar json.
    // Probamos guardando el mismo JSON de instance, pero en otro archivo.
    std::ofstream output("test_output.out");

    output << instance;
    output.close();

    return 0;
}