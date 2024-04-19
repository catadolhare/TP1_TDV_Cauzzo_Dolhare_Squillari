#include "funciones.h"
#include <vector>
#include <cmath>
#include <utility>
#include <tuple>
#include <cstdlib>
#include <iostream>
#include <unordered_map>
#include<algorithm>

using namespace std;

float error_total=0;
float error_minimo=1e10;
vector<vector<int>> minimo_bp= {};
unordered_map<string,float> estado;
unordered_map<string,vector<int>> predecesor;

float maximo (vector<float> valores){
    float maximo_valores = 0;
    for(int i = 0; i<valores.size(); i++){
        if (valores[i] > maximo_valores){
            maximo_valores = valores[i];
        }
    }
    return maximo_valores;
}

float minimo (vector<float> valores){
    float minimo_valores = 100000000;
    for(int i = 0; i<valores.size(); i++){
        if (valores[i] < minimo_valores){
            minimo_valores = valores[i];
        }
    }
    return minimo_valores;
}

vector<float> discretizar(vector<float> valores, int m){
    vector<float> discretizado;
    float min_x=minimo(valores);
    float max_x=maximo(valores);
    for(int i=0; i<m; i++){
        double val_x= min_x + i*(max_x-min_x)/(m-1);
        discretizado.push_back(val_x);
    }
    return discretizado;
}



float pendiente(vector<int> bp1, vector<int> bp2, vector<float> grilla_x, vector<float> grilla_y){
    float pendiente = static_cast<float>(grilla_y[bp2[1]] - grilla_y[bp1[1]])/(grilla_x[bp2[0]] - grilla_x[bp1[0]]);
    return pendiente;
}

float error_segmento(vector<int> bp1, vector<int> bp2, vector<float>& grilla_x, vector<float>& grilla_y, vector<float>& valores_x, vector<float>& valores_y){
    float error_aux = 0;
    for (int i = 0; i < valores_x.size(); i++) {
        if (valores_x[i] >= grilla_x[bp1[0]] && valores_x[i] <= grilla_x[bp2[0]]) {
            float p=(pendiente(bp1, bp2, grilla_x, grilla_y)*(valores_x[i] - grilla_x[bp1[0]])) + grilla_y[bp1[1]];
            error_aux = error_aux + abs(valores_y[i] - p);
        } else if (valores_x[i] > grilla_x[bp2[0]]) {
            break;
        }
    }
    
    return error_aux;
}

tuple<vector<vector<int>>, float> llamada_fuerza_bruta(vector<vector<int>>& B, int k, int m1, int m2, vector<float>& grilla_x, vector<float>& grilla_y, vector<float>& valores_x, vector<float>& valores_y){
    fuerza_bruta(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y);
    tuple<vector<vector<int>>, float> solucion= make_tuple(minimo_bp, error_minimo);
    return solucion;
}

void fuerza_bruta(vector<vector<int>>& B, int k, int m1, int m2, vector<float>& grilla_x, vector<float>& grilla_y, vector<float>& valores_x, vector<float>& valores_y){
    float error_segmento1 = 0;
    if (B.size() == k) {
        if (error_total < error_minimo && B.back().front() == m1 - 1) {
            error_minimo = error_total;
            minimo_bp = B;
            for(int i = 0;  i < B.size(); i++){
                cout << "[";
                cout << B[i][0] << " ," << B[i][1];
                cout << "]" << endl;;
            }
        }
    
    } else {
        if (B.empty()) {
            for (int i = 0; i < m2; i++) {
                B.push_back({0, i});
                fuerza_bruta(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y);
                B.pop_back();
            }
        } else {
            for (int l = B.back().front()+ 1; l < m1; l++) {
                for (int j = 0; j < m2; j++) {
                    B.push_back({l, j});
                    error_segmento1 = error_segmento(B[B.size() - 2], B.back(), grilla_x, grilla_y, valores_x, valores_y);
                    error_total = error_total + error_segmento1;
                    fuerza_bruta(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y);
                    B.pop_back();
                    error_total = error_total - error_segmento1;
                }
            }
        }
    }
}

tuple<vector<vector<int>>, float> llamada_backtracking(vector<vector<int>>& B, int k, int m1, int m2, vector<float>& grilla_x, vector<float>& grilla_y, vector<float>& valores_x, vector<float> valores_y){
    backtracking(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y);
    tuple<vector<vector<int>>, float> sol= make_tuple(minimo_bp, error_minimo);
    return sol;

}

void backtracking(vector<vector<int>>& B, int k, int m1, int m2, vector<float>& grilla_x, vector<float>& grilla_y, vector<float>& valores_x, vector<float>& valores_y){
    float error_segmento1 = 0;
    if (B.size() == k) {
        if (error_total < error_minimo && B.back()[0] == m1 - 1) {
            error_minimo = error_total;
            minimo_bp = B;
        }
    } else {
        if (B.empty()) {
            for (int i = 0; i < m2; ++i) {
                B.push_back({0, i});
                backtracking(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y);
                B.pop_back();
            }
        } else if (error_total < error_minimo) {
            for (int l = B.back()[0] + 1; l < m1; ++l) {
                for (int j = 0; j < m2; ++j) {
                    B.push_back({l, j});
                    error_segmento1 = error_segmento(B[B.size() - 2], B.back(), grilla_x, grilla_y, valores_x, valores_y);
                    error_total += error_segmento1;
                    backtracking(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y);
                    B.pop_back();
                    error_total -= error_segmento1;
                }
            }
        }
    }
}

float programacion_dinamica(int M, int i, int j, int m1, int m2, vector<float> grilla_x, vector<float> grilla_y, vector<float> valores_x, vector<float> valores_y){
    float error_segmento_pd = 0;
    float error_minimo_local = 1e10;
    
    string clave = to_string(M) + "-" + to_string(i) + "-" + to_string(j);
    if (estado.find(clave) != estado.end()){
        return estado[clave];
    }
    if (M == 1 && i > 0){
        for(int z=0; z<m2; z++){
            error_segmento_pd = error_segmento({0, z}, {i, j}, grilla_x, grilla_y, valores_x, valores_y);
            if (error_segmento_pd < error_minimo_local){
                error_minimo_local = error_segmento_pd;
                int bp_y = z;
                predecesor[clave] = {0, bp_y};
            }
        }
        estado[clave] = error_minimo_local;
        return error_minimo_local;

    }else{
        for(int l=0; l<i; l++){
            for(int n=0; n<m2; n++){
                error_segmento_pd = error_segmento({l, n}, {i, j}, grilla_x, grilla_y, valores_x, valores_y);
                float error_aux = error_segmento_pd + programacion_dinamica(M-1, l, n, m1, m2, grilla_x, grilla_y, valores_x, valores_y);
                if (error_aux < error_minimo_local){
                    error_minimo_local = error_aux;
                    predecesor[clave] = {l, n};
                }
            }
        }        
        estado[clave] = error_minimo_local;
        return estado[clave];
    }
}

tuple<vector<vector<int>>, float> reconstruccion_pd(int M, int m1, int m2, vector<float> grilla_x, vector<float> grilla_y, vector<float> valores_x, vector<float> valores_y){

    float error_rec_minimo = 1e10;
    vector<vector<int>> B;
    int bp_y;
    for(int l=0; l<m2; l++){
        float error_reconstruccion = programacion_dinamica(M, m1-1, l, m1, m2, grilla_x, grilla_y, valores_x, valores_y);
        if (error_reconstruccion < error_rec_minimo){
            error_rec_minimo = error_reconstruccion;
            bp_y = l;
        }
    }
    error_rec_minimo = programacion_dinamica(M, m1-1, bp_y, m1, m2, grilla_x, grilla_y, valores_x, valores_y); //lo corremos una vez mÃ¡s con los puntos que hacen el minimo para tener bien el diccionario
    B.push_back({m1-1, bp_y});
    string clave = to_string(M) + "-" + to_string(m1-1) + "-" + to_string(bp_y);
    while(M > 0){
        B.push_back(predecesor[clave]);
        clave = to_string(M-1) + "-" + to_string(predecesor[clave][0]) + "-" + to_string(predecesor[clave][1]);
        M -= 1;
    }
    vector<vector<int>> copia;
    for(int i=B.size()-1; i>=0; i--){
        copia.push_back(B[i]);
    }
    tuple <vector<vector<int>>, float> solucion = make_tuple(copia, error_rec_minimo);
    return solucion;
}

tuple<vector<vector<int>>, float> llamada_programacion_dinamica(int M, int m1, int m2, vector<float> grilla_x, vector<float> grilla_y, vector<float> valores_x, vector<float> valores_y){

    tuple <vector<vector<int>>, float> solucion = reconstruccion_pd(M, m1, m2, grilla_x, grilla_y, valores_x, valores_y);

    return solucion;
}
