from typing import List

def discretizar(valores, m:int):
    grilla = []
    for i in range(m):
        grilla.append(valores[0] + (i)*(valores[-1]-valores[0])/(m-1))
    return grilla

def pendiente(bp1, bp2, grilla_x, grilla_y):
    return (grilla_y[bp2[1]] - grilla_y[bp1[1]])/(grilla_x[bp2[0]] - grilla_x[bp1[0]])

def error_segmento(bp1, bp2, grilla_x, grilla_y, valores_x, valores_y):
    error = 0
    for i in range(len(valores_x)):
        if valores_x[i] >= grilla_x[bp1[0]] and valores_x[i] <= grilla_x[bp2[0]]:
            error += abs(valores_y[i] - (pendiente(bp1, bp2, grilla_x, grilla_y)*(valores_x[i] - grilla_x[bp1[0]]) + grilla_y[bp1[1]]))
        elif valores_x[i] > grilla_x[bp2[0]]: #solo funciona si la lista esta ordenada
            break
    return error

def suma_errores(B:List[List[int]], grilla_x, grilla_y, valores_x, valores_y):
    errores = 0
    for i in range(len(B)-2):
        errores += error_segmento(B[i], B[i+1], grilla_x, grilla_y, valores_x, valores_y)
    return errores

def fuerza_bruta(B:List[List[int]], k:int, m1:int, m2:int, grilla_x, grilla_y, valores_x, valores_y, minimo:List[List[int]], error_minimo):
    if len(B) == k and suma_errores(B, grilla_x, grilla_y, valores_x, valores_y) < error_minimo:
        error_minimo = suma_errores(B, grilla_x, grilla_y, valores_x, valores_y)
        minimo = B
    #elif len(B) == k and suma_errores(B, grilla_x, grilla_y, valores_x, valores_y) >= suma_errores(minimo, grilla_x, grilla_y, valores_x,valores_y):
        #B.pop()

    else:
        if len(B) == 0:
            for i in range(m2):
                B.append([0, i])
                fuerza_bruta(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y, minimo, error_minimo)
        
        elif len(B) == k:
            for i in range(m2):
                B.append([k-1, i])
                fuerza_bruta(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y, minimo, error_minimo)
        
        else:
            for i in range(int(B[-1][0]) + 1, m1):
                for j in range(1, m2):
                    B.append([i, j])
                    fuerza_bruta(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y, minimo, error_minimo)
                    B.pop()
                    fuerza_bruta(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y, minimo, error_minimo)