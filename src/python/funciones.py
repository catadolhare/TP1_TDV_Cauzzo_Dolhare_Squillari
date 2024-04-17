from typing import List, Dict, Tuple
import time

#variables globales
minimo:List[List[int]] = []
error_total:int = 0
error_minimo:int = 1e10

estado:Dict[str, float] = {}

def pendiente(bp1, bp2, grilla_x, grilla_y):
    return (grilla_y[bp2[1]] - grilla_y[bp1[1]])/(grilla_x[bp2[0]] - grilla_x[bp1[0]])

def error_segmento(bp1:List[int], bp2:List[int],grilla_x, grilla_y, valores_x, valores_y):
    error_aux = 0
    for i in range(len(valores_x)):
        if valores_x[i] >= grilla_x[bp1[0]] and valores_x[i] <= grilla_x[bp2[0]]:
            error_aux += abs(valores_y[i] - ((pendiente(bp1, bp2, grilla_x, grilla_y)*(valores_x[i] - grilla_x[bp1[0]])) + grilla_y[bp1[1]]))
        elif valores_x[i] > grilla_x[bp2[0]]: #solo funciona si la lista esta ordenada
            break
    return error_aux

def llamada_fuerza_bruta(B:List[List[int]], k:int, m1:int, m2:int, grilla_x, grilla_y, valores_x, valores_y):
    global error_total
    global error_minimo
    global minimo

    fuerza_bruta(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y)

    return minimo, error_minimo


def fuerza_bruta(B:List[List[int]], k:int, m1:int, m2:int, grilla_x, grilla_y, valores_x, valores_y):
    global error_total
    global error_minimo
    global minimo
    
    error_segmento1 = 0
    if len(B) == k:
        if error_total < error_minimo and B[-1][0] == m1-1:
            error_minimo = error_total
            minimo[:] = B[:]
        return

    else:
        if len(B) == 0:
            for i in range(m2):
                B.append([0, i])
                fuerza_bruta(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y)
                B.pop()
        else:
            for l in range(int(B[-1][0]) + 1, m1):
                for j in range(m2):
                    B.append([l, j])
                    error_segmento1=error_segmento(B[-2], B[-1], grilla_x, grilla_y, valores_x, valores_y)
                    error_total+=error_segmento1
                    fuerza_bruta(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y)
                    B.pop()
                    error_total -= error_segmento1
        return
        
def llamada_backtracking(B:List[List[int]], k:int, m1:int, m2:int, grilla_x, grilla_y, valores_x, valores_y):
    global error_total
    global error_minimo
    global minimo

    backtracking(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y)

    return minimo, error_minimo

def backtracking(B:List[List[int]], k:int, m1:int, m2:int, grilla_x, grilla_y, valores_x, valores_y):
    global error_total
    global error_minimo
    global minimo
    
    error_segmento1 = 0
    if len(B) == k:
        if error_total < error_minimo and B[-1][0] == m1-1:
            error_minimo = error_total
            minimo[:] = B[:]
        return

    elif error_total < error_minimo:
        if len(B) == 0:
            for i in range(m2):
                B.append([0, i])
                fuerza_bruta(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y)
                B.pop()
        else:
            for l in range(int(B[-1][0]) + 1, m1):
                for j in range(m2):
                    B.append([l, j])
                    error_segmento1=error_segmento(B[-2], B[-1], grilla_x, grilla_y, valores_x, valores_y)
                    error_total+=error_segmento1
                    fuerza_bruta(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y)
                    B.pop()
                    error_total -= error_segmento1
        return

def llamada_programacion_dinamica(M:int, i:int, j:int, m1:int, m2:int, grilla_x, grilla_y, valores_x, valores_y):
    global estado

    error = programacion_dinamica(M, i, j, m1, m2, grilla_x, grilla_y, valores_x, valores_y)
    #breakpoints_pd = reconstruccion_pd(M, i, j, m1, m2, grilla_x, grilla_y, valores_x, valores_y)

    return error #, breakpoints_pd

def programacion_dinamica(M:int, i:int, j:int, m1:int, m2:int, grilla_x, grilla_y, valores_x, valores_y):
    global estado
    error_segmento_pd:float = 0
    error_minimo_local = 1e10
    
    clave = str(M) + "-" + str(i) + "-" + str(j)
    if clave in estado:
        return estado[clave]
    
    if M == 1 and i > 0:
        for z in range(m2):
            error_segmento_pd = error_segmento([0, z], [i, j], grilla_x, grilla_y, valores_x, valores_y)
            error_minimo_local = min(error_minimo_local, error_segmento_pd)
        estado[clave] = error_minimo_local
        return error_minimo_local

    else:
        for l in range(0, i):
            for n in range(m2):
                error_segmento_pd = error_segmento([l, n], [i, j], grilla_x, grilla_y, valores_x, valores_y)
                error_minimo_local = min(error_minimo_local, error_segmento_pd + programacion_dinamica(M-1, l, n, m1, m2, grilla_x, grilla_y, valores_x, valores_y))
        estado[clave] = error_minimo_local
        print(estado)
        return estado[clave]
    
def reconstruccion_pd(M:int, i:int, j:int, m1:int, m2:int, grilla_x, grilla_y, valores_x, valores_y):
    B = []
    for l in range(m2):
        error_reconstruccion = programacion_dinamica(M, m1-1, l, m1, m2, grilla_x, grilla_y, valores_x, valores_y)
        if error_reconstruccion < error_rec_minimo:
            error_rec_minimo = error_reconstruccion
            bp_y = l
    B.append([m1-1, bp_y])


    
