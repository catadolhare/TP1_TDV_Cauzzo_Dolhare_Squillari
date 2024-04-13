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

    int K = instance["n"];
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
    cout << "Grid_y: " << endl;
    for(int i = 0;  i < grid_y.size(); i++){
        cout << grid_y[i] << " ";
    }

    // Ejemplo para guardar json.
    // Probamos guardando el mismo JSON de instance, pero en otro archivo.
    std::ofstream output("test_output.out");

    output << instance;
    output.close();

    return 0;
}