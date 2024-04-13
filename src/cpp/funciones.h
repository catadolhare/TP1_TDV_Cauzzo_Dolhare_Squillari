#ifndef FUNCIONES_H
#define FUNCIONES_H

#include <vector>
using namespace std;

vector<float> discretizar(vector<float> valores, int m);

int pendiente(vector<int> bp1, vector<int> bp2, vector<float> grilla_x, vector<float> grilla_y);

float error_segmento(vector<int> bp1, vector<int> bp2, vector<float>& grilla_x, vector<float>& grilla_y, vector<float>& valores_x, vector<float>& valores_y);

void fuerza_bruta(vector<vector<int>>& B, int k, int m1, int m2, vector<float>& grilla_x, vector<float>& grilla_y, vector<float>& valores_x, vector<float>& valores_y, vector<vector<int>>& minimo, float& error_total, float& error_minimo);


#endif