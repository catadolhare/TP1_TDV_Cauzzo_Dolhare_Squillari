from typing import List

def discretizar(valores, m:int):
    grilla = []
    for i in range(m):
        grilla.append(valores[0] + (i)*(valores[-1]-valores[0])/(m-1))
    return grilla

def pendiente(bp1, bp2):
    return (bp2[1] - bp1[1])/(bp2[0] - bp1[0])

def error_segmento(bp1, bp2, grilla_x, grilla_y, valores_y):
    error = 0
    i = bp1[0]
    while valores_y[i]>=grilla_y[bp1[1]] and valores_y[i] <= grilla_y[bp2[1]]:
        error += abs(valores_y[i] - (pendiente(bp1, bp2)*(grilla_x[i] - bp1[1]) + bp1[1]))
        i += 1

    return error

def suma_errores(B:List[List[int]], grilla_x, grilla_y, valores_y):
    error = 0
    for i in range(len(B)-2):
        error += error_segmento(B[i], B[i+1], grilla_x, grilla_y, valores_y)
    return error

def fuerza_bruta(B:List[List[int]], k:int, m1:int, m2:int, grilla_x, grilla_y, valores_y):
    min = 0
    if len(B) == k and suma_errores(B, grilla_x, grilla_y, valores_y) < suma_errores(min, grilla_x, grilla_y, valores_y):
        min = B

    else:
        if len(B) == 0:
            for i in range(m2):
                B.append([0, i])
                fuerza_bruta(B, k, m1, m2, grilla_x, grilla_y, valores_y)
        
        if len(B) == k-2:
            for i in range(m2):
                B.append([k-1, i])
                fuerza_bruta(B, k, m1, m2, grilla_x, grilla_y, valores_y)

        for i in range(int(B[-1][0]) + 1, m1):
            for j in range(1, m2):
                B.append([i, j])
                fuerza_bruta(B, k, m1, m2, grilla_x, grilla_y, valores_y)
                