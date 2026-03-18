"""
Fórmula de Webster para optimización de semáforos.
"""
import numpy as np


def webster_cycle(Y: float, L: float,
                  C_min: float = 30, C_max: float = 180) -> float:
    """
    Ciclo óptimo: C0 = (1.5*L + 5) / (1 - Y)
    Y  = suma de razones de flujo crítico por fase
    L  = tiempo perdido total por ciclo (s)
    """
    if Y >= 1.0:
        return C_max
    if Y <= 0:
        return C_min
    return float(np.clip((1.5 * L + 5) / (1 - Y), C_min, C_max))


def webster_greens(ys: list[float], cycle: float, L: float) -> list[float]:
    """
    Verde efectivo por fase: g_i = (C - L) * y_i / Y
    """
    Y = sum(ys)
    eff = cycle - L
    if Y <= 0 or eff <= 0:
        return [eff / len(ys)] * len(ys)
    return [eff * y / Y for y in ys]


def webster_delay(q: float, s: float, g: float, C: float,
                  lost: float = 4.0) -> float:
    """
    Demora promedio por vehículo (Webster 1958, s/veh).
    q, s en veh/h; g, C, lost en segundos.
    """
    q_s  = q / 3600
    s_s  = s / 3600
    lam  = g / C
    x    = min(q_s / (s_s * lam), 0.99) if s_s * lam > 0 else 0.99

    d1 = C * (1 - lam) ** 2 / (2 * (1 - lam * x))
    d2 = x ** 2 / (2 * q_s * (1 - x)) if (1 - x) > 0 else 0
    d3 = 0.65 * (C / (q_s ** 2 + 1e-9)) ** (1 / 3) * x ** (2 + 5 * lam)
    return max(d1 + d2 - d3, 0)
