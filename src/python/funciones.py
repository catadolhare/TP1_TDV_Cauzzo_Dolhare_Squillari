from typing import List

def discretizar(valores, m:int):
    grilla = []
    for i in range(m):
        grilla.append(valores[0] + (i)*(valores[-1]-valores[0])/(m-1))
    return grilla

def pendiente(bp1, bp2, grilla_x, grilla_y):
    return (grilla_y[bp2[1]] - grilla_y[bp1[1]])/(grilla_x[bp2[0]] - grilla_x[bp1[0]])

def error_segmento(bp1:List[int], bp2:List[int], grilla_x, grilla_y, valores_x, valores_y):
    error_aux = 0
    if bp1[1] == -1:
       bp1[1] = 0
    for i in range(len(valores_x)):
        if valores_x[i] >= grilla_x[bp1[0]] and valores_x[i] <= grilla_x[bp2[0]]:
            error_aux += abs(valores_y[i] - (pendiente(bp1, bp2, grilla_x, grilla_y)*(valores_x[i] - grilla_x[bp1[0]]) + grilla_y[bp1[1]]))
        elif valores_x[i] > grilla_x[bp2[0]]: #solo funciona si la lista esta ordenada
            break
    return error_aux

def fuerza_bruta(B:List[List[int]], k:int, m1:int, m2:int, grilla_x, grilla_y, valores_x, valores_y, minimo:List[List[int]], error_total, error_minimo:List[int]):
    error_segmento1 = 0
    if k == 1 and error_total < error_minimo[0]: #ultimo se el ultimo de la grilla
        error_minimo = [error_total]
        minimo[:] = B[:]
        return minimo, error_minimo

    else:
        #for i in range(m2):
        #B = [[0, 0]]

        '''if len(B) == k-1:
            for j in range(m2):
                B.append([k-1, j])
                error_segmento1=error_segmento([k-2, j-1], [k-1, j], grilla_x, grilla_y, valores_x, valores_y)
                error+=error_segmento1
                fuerza_bruta(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y, minimo, error, error_minimo, error_segmento1)
                B.pop()
                error -= error_segmento1'''
        
            #else:
        for l in range(int(B[-1][0]) + 1, m1):
            for j in range(m2):
                    B.append([l, j])
                    error_segmento1=error_segmento([l-1, j-1], [l, j], grilla_x, grilla_y, valores_x, valores_y)
                    error_total+=error_segmento1
                    minimo, error_minimo = fuerza_bruta(B, k-1, m1, m2, grilla_x, grilla_y, valores_x, valores_y, minimo, error_total, error_minimo)
                    B.pop()
                    error_total -= error_segmento1
        return minimo, error_minimo