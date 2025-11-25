import math

# Lista de puntos
puntos = [
    (2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2),
    (12, 5), (14, 3), (3, 10), (6, 8), (11, 11), (13, 9),
    (15, 6), (18, 2), (17, 7), (19, 4), (21, 3), (20, 8),
    (23, 5), (25, 7), (24, 1), (26, 4), (30, 2), (28, 9),
    (31, 7), (34, 6), (33, 3), (36, 8), (38, 5)
]

# -------------------------------------------------------------
# Función de distancia Euclidiana
# -------------------------------------------------------------
def distancia(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# -------------------------------------------------------------
# Fuerza Bruta O(n^2)
# -------------------------------------------------------------
def distancia_minima_bruta(puntos):
    min_dist = float("inf")
    n = len(puntos)
    for i in range(n):
        for j in range(i+1, n):
            d = distancia(puntos[i], puntos[j])
            if d < min_dist:
                min_dist = d
    return min_dist

# -------------------------------------------------------------
# Divide y Vencerás O(n log n)
# -------------------------------------------------------------
def distancia_min_strip(strip, d):
    min_dist = d
    strip.sort(key=lambda p: p[1])  # ordenar por Y

    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_dist:
            min_dist = min(min_dist, distancia(strip[i], strip[j]))
            j += 1
    return min_dist

def distancia_min_divide_y_venceras(puntos):
    if len(puntos) <= 3:
        return distancia_minima_bruta(puntos)

    mid = len(puntos) // 2
    mitad_izq = puntos[:mid]
    mitad_der = puntos[mid:]

    d_izq = distancia_min_divide_y_venceras(mitad_izq)
    d_der = distancia_min_divide_y_venceras(mitad_der)
    d = min(d_izq, d_der)

    # Construir franja (strip)
    mid_x = puntos[mid][0]
    strip = [p for p in puntos if abs(p[0] - mid_x) < d]

    return min(d, distancia_min_strip(strip, d))

def closest_pair(puntos):
    puntos_ordenados = sorted(puntos, key=lambda p: p[0])
    return distancia_min_divide_y_venceras(puntos_ordenados)

# -------------------------------------------------------------
# Ejecución
# -------------------------------------------------------------
print("Distancia mínima (Fuerza bruta):", distancia_minima_bruta(puntos))
print("Distancia mínima (Divide y vencerás):", closest_pair(puntos))
