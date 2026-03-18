# Optimización de Tráfico — Chapinero, Bogotá

Proyecto de optimización de la red vial de Chapinero usando teoría de juegos de tráfico y control de semáforos.

## Contenido

### Notebooks de Jupyter (`notebooks/`)
Implementación computacional del pipeline completo. **Nota: los notebooks tienen algunas correcciones pendientes** (en particular, los solvers de CVXPY requieren ajuste de parámetros para redes de mayor tamaño).

| Notebook | Contenido |
|---|---|
| `01_download_graph.ipynb` | Descarga del grafo OSM de Chapinero |
| `02_wardrop_equilibrium.ipynb` | Equilibrio de Wardrop (User Equilibrium) |
| `03_social_optimum.ipynb` | Óptimo Social (System Optimum) |
| `04_price_of_anarchy.ipynb` | Price of Anarchy |
| `05_webster_optimization.ipynb` | Optimización de semáforos con Webster |

### Documento teórico (`latex/`)
Notas matemáticas sobre la teoría de asignación de tráfico: equilibrio de Wardrop, teorema de Beckmann, óptimo social, externalidades de congestión y Precio de la Anarquía. **En construcción en Overleaf.**

## Referencias
- Wardrop (1952), Beckmann et al. (1956), Roughgarden y Tardos (2002), Sheffi (1985)
