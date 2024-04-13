from typing import List, Dict

def pendiente(bp1, bp2, grilla_x, grilla_y):
    return (grilla_y[bp2[1]] - grilla_y[bp1[1]])/(grilla_x[bp2[0]] - grilla_x[bp1[0]])

def error_segmento(bp1:List[int], bp2:List[int], grilla_x, grilla_y, valores_x, valores_y):
    error_aux = 0
    for i in range(len(valores_x)):
        if valores_x[i] >= grilla_x[bp1[0]] and valores_x[i] <= grilla_x[bp2[0]]:
            error_aux += abs(valores_y[i] - ((pendiente(bp1, bp2, grilla_x, grilla_y)*(valores_x[i] - grilla_x[bp1[0]])) + grilla_y[bp1[1]]))
        elif valores_x[i] > grilla_x[bp2[0]]: #solo funciona si la lista esta ordenada
            break
    return error_aux

def fuerza_bruta(B:List[List[int]], k:int, m1:int, m2:int, grilla_x, grilla_y, valores_x, valores_y, minimo, error_total, error_minimo):
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
                    minimo, error_minimo = fuerza_bruta(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y, minimo, error_total, error_minimo)
                    B.pop()
            else:
                for l in range(int(B[-1][0]) + 1, m1):
                    for j in range(m2):
                        B.append([l, j])
                        error_segmento1=error_segmento(B[-2], B[-1], grilla_x, grilla_y, valores_x, valores_y)
                        error_total+=error_segmento1
                        minimo, error_minimo = fuerza_bruta(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y, minimo, error_total, error_minimo)
                        B.pop()
                        error_total -= error_segmento1
            return minimo, error_minimo
        

def backtracking(B:List[List[int]], k:int, m1:int, m2:int, grilla_x, grilla_y, valores_x, valores_y, minimo:List[List[int]], error_total, error_minimo):
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
                    minimo, error_minimo = backtracking(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y, minimo, error_total, error_minimo)
                    B.pop()
            else:
                for l in range(int(B[-1][0]) + 1, m1):
                    for j in range(m2):
                        B.append([l, j])
                        error_segmento1=error_segmento(B[-2], B[-1], grilla_x, grilla_y, valores_x, valores_y)
                        error_total+=error_segmento1
                        minimo, error_minimo = backtracking(B, k, m1, m2, grilla_x, grilla_y, valores_x, valores_y, minimo, error_total, error_minimo)
                        B.pop()
                        error_total -= error_segmento1

        return minimo, error_minimo
        
def programacion_dinamica(B:List[List[int]], k:int, M:int, i:int, estado:Dict[List[List[int]], int]):
    if M == 1:
        estado[B] = error_caso_base()
        return error_caso_base()
    
    else:
        if B in estado.keys():
            return B, estado[B]
        
        else:
            minimo = 1e10
            for j in range(i, M):
                B.append([j, M])
                minimo = min(minimo, programacion_dinamica(B, k, m-1, j, estado))
                B.pop()
                estado[B] = minimo
            return minimo
