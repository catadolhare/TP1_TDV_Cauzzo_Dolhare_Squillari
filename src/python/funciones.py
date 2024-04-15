from typing import List, Dict

#variables globales
minimo:List[List[int]] = []
error_total:int = 0
error_minimo:int = 1e10

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

def fuerza_bruta(B:List[List[int]], k:int, m1:int, m2:int, grilla_x, grilla_y, valores_x, valores_y):
    global error_total
    global error_minimo
    global minimo
    
    
    error_segmento1 = 0
    if len(B) == k:
        if error_total < error_minimo and B[-1][0] == m1-1:
            error_minimo = error_total
            minimo[:] = B[:]
        return minimo, error_minimo

    else:
        if len(B) == 0:
            for i in range(m2):
                B.append([0, i])
                minimo, error_minimo = fuerza_bruta(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y)
                B.pop()
        else:
            for l in range(int(B[-1][0]) + 1, m1):
                for j in range(m2):
                    B.append([l, j])
                    error_segmento1=error_segmento(B[-2], B[-1], grilla_x, grilla_y, valores_x, valores_y)
                    error_total+=error_segmento1
                    minimo, error_minimo = fuerza_bruta(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y)
                    B.pop()
                    error_total -= error_segmento1
        return minimo, error_minimo
        

def backtracking(B:List[List[int]], k:int, m1:int, m2:int, grilla_x, grilla_y, valores_x, valores_y):
        error_segmento1 = 0
        if len(B) == k:
            if error_total < error_minimo and B[-1][0] == m1-1:
                error_minimo = error_total
                minimo[:] = B[:]
            return minimo, error_minimo

        elif error_total < error_minimo:
            if len(B) == 0:
                for i in range(m2):
                    B.append([0, i])
                    minimo, error_minimo = backtracking(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y)
                    B.pop()
            else:
                for l in range(int(B[-1][0]) + 1, m1):
                    for j in range(m2):
                        B.append([l, j])
                        error_segmento1=error_segmento(B[-2], B[-1])
                        error_total+=error_segmento1
                        minimo, error_minimo = backtracking(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y)
                        B.pop()
                        error_total -= error_segmento1

        return minimo, error_minimo
        
def programacion_dinamica(B:List[List[int]], k:int, M:int, m1:int, m2:int, i:int, j:int, estado:Dict[List[List[int]], float], grilla_x, grilla_y, valores_x, valores_y):
    minimo_cb = 1e10
    minimo_pd = 1e10
    minimo_bp = []
    if M == 1:
        for l in range(m2):
            B.append([0, l])
            error_segmento_cb = error_segmento([0, l], [i, j], grilla_x, grilla_y, valores_x, valores_y)
            estado[B] = minimo_cb
            if error_segmento_cb < minimo_cb:
                minimo_cb = error_segmento_cb
                minimo_bp[:] = B[:]
            B.pop()
        return minimo
    
    else:
        if B in estado.keys():
            return estado[B]
        
        else:
            if len(estado) == 0:
                for l in range(m2):
                    B.append([0, l])



            for n in range(m2):
                B.append([B[-1][0], n])
                error_segmento_pd = error_segmento(B[-1], [i,j], grilla_x, grilla_y, valores_x, valores_y)
                minimo_pd = min(minimo_pd, error_segmento_pd + programacion_dinamica(B, k, M-1, B[-1][0], B[-1][1], estado))
                estado[B] = minimo_pd
                B.pop()


