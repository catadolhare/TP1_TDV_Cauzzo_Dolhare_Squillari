#include "funciones.h"
#include <vector>
#include <cmath>
#include <utility>

using namespace std;

vector<float> discretizar(vector<float> valores, int m){
    vector<float> discretizado;
    for(int i=0; i<valores.size(); i++){
        float valor = valores[i];
        int valor_discretizado = valores[0] + i*((valores[-1]-valores[0])/(m-1));
        discretizado.push_back(valor_discretizado);
    }

    return discretizado;
}

int pendiente(vector<int> bp1, vector<int> bp2, vector<float> grilla_x, vector<float> grilla_y){
    return (grilla_y[bp2[1]] - grilla_y[bp1[1]])/(grilla_x[bp2[0]] - grilla_x[bp1[0]]);
}

float error_segmento(vector<int> bp1, vector<int> bp2, vector<float>& grilla_x, vector<float>& grilla_y, vector<float>& valores_x, vector<float>& valores_y){
    float error_aux = 0;
    for (int i = 0; i < valores_x.size(); ++i) {
        if (valores_x[i] >= grilla_x[bp1[0]] && valores_x[i] <= grilla_x[bp2[0]]) {
            error_aux += abs(valores_y[i] - ((pendiente(bp1, bp2, grilla_x, grilla_y) * (valores_x[i] - grilla_x[bp1[0]])) + grilla_y[bp1[1]]));
        } else if (valores_x[i] > grilla_x[bp2[0]]) {
            break;
        }
    }
    return error_aux;
}

void fuerza_bruta(vector<vector<int>>& B, int k, int m1, int m2, vector<float>& grilla_x, vector<float>& grilla_y, vector<float>& valores_x, vector<float>& valores_y, vector<vector<int>>& minimo, float& error_total, float& error_minimo){
    float error_segmento1 = 0;
    if (B.size() == k) {
        if (error_total < error_minimo && B.back()[0] == m1 - 1) {
            error_minimo = error_total;
            minimo = B;
        }
    } else {
        if (B.empty()) {
            for (int i = 0; i < m2; ++i) {
                B.push_back({0, i});
                fuerza_bruta(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y, minimo, error_total, error_minimo);
                B.pop_back();
            }
        } else {
            for (int l = B.back()[0] + 1; l < m1; ++l) {
                for (int j = 0; j < m2; ++j) {
                    B.push_back({l, j});
                    error_segmento1 = error_segmento(B[B.size() - 2], B.back(), grilla_x, grilla_y, valores_x, valores_y);
                    error_total += error_segmento1;
                    fuerza_bruta(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y, minimo, error_total, error_minimo);
                    B.pop_back();
                    error_total -= error_segmento1;
                }
            }
        }
    }
}