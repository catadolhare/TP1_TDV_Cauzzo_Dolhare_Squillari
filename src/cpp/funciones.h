#ifndef FUNCIONES_H
#define FUNCIONES_H

#include <vector>
#include <tuple>
using namespace std;

float maximo (vector<float> valores);

float minimo (vector<float> valores);

vector<float> discretizar(vector<float> valores, int m);

float pendiente(vector<int> bp1, vector<int> bp2, vector<float> grilla_x, vector<float> grilla_y);

float error_segmento(vector<int> bp1, vector<int> bp2, vector<float>& grilla_x, vector<float>& grilla_y, vector<float>& valores_x, vector<float>& valores_y);

void fuerza_bruta(vector<vector<int>>& B, int k, int m1, int m2, vector<float>& grilla_x, vector<float>& grilla_y, vector<float>& valores_x, vector<float>& valores_y);

tuple<vector<vector<int>>, float> llamada_fuerza_bruta(vector<vector<int>>& B, int k, int m1, int m2, vector<float>& grilla_x, vector<float>& grilla_y, vector<float>& valores_x, vector<float>& valores_y);

tuple<vector<vector<int>>, float> llamada_backtracking(vector<vector<int>>& B, int k, int m1, int m2, vector<float>& grilla_x, vector<float>& grilla_y, vector<float>& valores_x, vector<float> valores_y);

void backtracking(vector<vector<int>>& B, int k, int m1, int m2, vector<float>& grilla_x, vector<float>& grilla_y, vector<float>& valores_x, vector<float>& valores_y);

float programacion_dinamica(int M, int i, int j, int m1, int m2, vector<float> grilla_x, vector<float> grilla_y, vector<float> valores_x, vector<float> valores_y);

tuple<vector<vector<int>>, float> reconstruccion_pd(int M, int m1, int m2, vector<float> grilla_x, vector<float> grilla_y, vector<float> valores_x, vector<float> valores_y);

tuple<vector<vector<int>>, float> llamada_programacion_dinamica(int M, int m1, int m2, vector<float> grilla_x, vector<float> grilla_y, vector<float> valores_x, vector<float> valores_y);
#endif