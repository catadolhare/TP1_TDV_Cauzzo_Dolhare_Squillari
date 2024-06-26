from typing import List, Dict, Tuple
import time

#variables globales
minimo:List[List[int]] = []
error_total:int = 0
error_minimo:int = 1e10

estado:Dict[str, float] = {}
predecesor:Dict[str, List[int]] = {}

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

def llamada_programacion_dinamica(M:int, m1:int, m2:int, grilla_x, grilla_y, valores_x, valores_y):
    global estado
    global predecesor

    breakpoints_pd, error_pd = reconstruccion_pd(M, m1, m2, grilla_x, grilla_y, valores_x, valores_y)

    return breakpoints_pd, error_pd

def programacion_dinamica(M:int, i:int, j:int, m1:int, m2:int, grilla_x, grilla_y, valores_x, valores_y):
    global estado
    global predecesor

    error_segmento_pd:float = 0
    error_minimo_local = 1e10
    
    clave = str(M) + "-" + str(i) + "-" + str(j)
    if clave in estado:
        return estado[clave]
    
    if M == 1 and i > 0:
        for z in range(m2):
            error_segmento_pd = error_segmento([0, z], [i, j], grilla_x, grilla_y, valores_x, valores_y)
            if error_segmento_pd < error_minimo_local:
                error_minimo_local = error_segmento_pd
                bp_y = z
                predecesor[clave] = [0, bp_y]
        estado[clave] = error_minimo_local
        
        return error_minimo_local

    else:
        for l in range(0, i):
            for n in range(m2):
                error_segmento_pd = error_segmento([l, n], [i, j], grilla_x, grilla_y, valores_x, valores_y)
                error_aux = error_segmento_pd + programacion_dinamica(M-1, l, n, m1, m2, grilla_x, grilla_y, valores_x, valores_y)
                if error_aux < error_minimo_local:
                    error_minimo_local = error_aux
                    predecesor[clave] = [l, n]

                
        estado[clave] = error_minimo_local
        return estado[clave]
    
def reconstruccion_pd(M:int, m1:int, m2:int, grilla_x, grilla_y, valores_x, valores_y):
    global estado
    global predecesor
    
    error_rec_minimo = 1e10
    B = []
    for l in range(m2):
        error_reconstruccion = programacion_dinamica(M, m1-1, l, m1, m2, grilla_x, grilla_y, valores_x, valores_y)
        if error_reconstruccion < error_rec_minimo:
            error_rec_minimo = error_reconstruccion
            bp_y = l
    error_rec_minimo = programacion_dinamica(M, m1-1, bp_y, m1, m2, grilla_x, grilla_y, valores_x, valores_y) #lo corremos una vez más con los puntos que hacen el minimo para tener bien el diccionario
    B.append([m1-1, bp_y])
    clave = str(M) + "-" + str(m1-1) + "-" + str(bp_y)
    while M > 0:
        B.append(predecesor[clave])
        clave = str(M-1) + "-" + str(predecesor[clave][0]) + "-" + str(predecesor[clave][1])
        M -= 1
    B = B[::-1]
    return B, error_rec_minimo