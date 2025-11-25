# Problema del Par de Puntos Más Cercanos

## Comparación de Complejidades: O(n²) vs O(n log n)

### Algoritmo de Fuerza Bruta - O(n²)

El algoritmo de fuerza bruta compara **todos los pares de puntos** posibles:

```
Para cada punto i:
    Para cada punto j > i:
        Calcular distancia entre i y j
```

- Número total de pares: C(n,2) = n·(n-1)/2 = **O(n²)**
- Cada comparación: O(1)
- Complejidad total: **O(n²)**

**Problema:** Con 29 puntos hace ~420 comparaciones. Con 1 millón de puntos haría ~500 mil millones de comparaciones.

---

### Algoritmo Divide y Vencerás - O(n log n)

**¿Por qué mejora a O(n log n)?**

El algoritmo divide el problema en subproblemas más pequeños:

#### 1. **Divide (log n niveles)**

- Divide el conjunto de puntos ordenados por coordenada X en dos mitades
- Esto crea un árbol de recursión con altura **log n**
- En cada nivel: 1 → 2 → 4 → 8 → ... → n subproblemas

#### 2. **Conquista**

- Base: Si ≤ 3 puntos → O(1) (fuerza bruta directa)
- Recursión: T(n) = 2·T(n/2) + O(n log n)

#### 3. **Combina (O(n log n) por nivel)**

El paso crítico es la **franja de combinación**:

```
- Distancia mínima actual: d
- Crear "franja" alrededor de la línea divisoria
- Solo incluir puntos con |x - x_medio| < d
- Estos puntos: máximo ~7-8 puntos (propiedad geométrica)
```

**Clave geométrica:** En cualquier región de tamaño d×d,
solo caben ~7 puntos máximo manteniendo distancia ≥ d entre ellos.

Esto significa que en la franja:

- Aunque haya n puntos totales, solo ~O(1) están en la franja
- Ordenar por Y: O(n log n) **una sola vez** al inicio
- Búsqueda en franja: O(n) (no O(n²)) porque el bucle interno itera ≤ 7 veces

#### 4. **Análisis Total**

```
T(n) = 2·T(n/2) + O(n)    [la franja se procesa en O(n)]
     = O(n log n)          [por el Teorema Maestro]
```

---

## Comparativa

| Aspecto          | Fuerza Bruta          | Divide y Vencerás            |
| ---------------- | --------------------- | ---------------------------- |
| **Complejidad**  | O(n²)                 | O(n log n)                   |
| **100 puntos**   | ~5,000 ops            | ~665 ops                     |
| **1,000 puntos** | ~500,000 ops          | ~10,000 ops                  |
| **1M puntos**    | ~500 mil millones ops | ~20 millones ops             |
| **Estrategia**   | Comparar todo         | Descartar zonas innecesarias |

**Conclusión:** El algoritmo D&C es **exponencialmente más eficiente** porque explota propiedades geométricas del plano para descartar puntos que no pueden ser la solución, evitando las comparaciones innecesarias que obliga la fuerza bruta.
