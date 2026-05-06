"""Webster signal timing formulas."""


def _clip(value: float, lower: float, upper: float) -> float:
    return max(lower, min(value, upper))


def webster_cycle(Y: float, L: float,
                  C_min: float = 30, C_max: float = 180) -> float:
    """Return Webster cycle length in seconds, clipped to bounds."""
    if Y >= 1.0:
        return C_max
    if Y <= 0:
        return C_min
    return float(_clip((1.5 * L + 5) / (1 - Y), C_min, C_max))


def webster_greens(ys: list[float], cycle: float, L: float) -> list[float]:
    """Allocate effective green times by critical flow ratios."""
    if not ys:
        return []
    Y = sum(ys)
    eff = cycle - L
    if Y <= 0 or eff <= 0:
        return [eff / len(ys)] * len(ys)
    return [eff * y / Y for y in ys]


def webster_delay(q: float, s: float, g: float, C: float,
                  lost: float = 4.0) -> float:
    """Return average Webster delay in seconds per vehicle."""
    if q <= 0 or s <= 0 or g <= 0 or C <= 0:
        return 0.0
    q_s  = q / 3600
    s_s  = s / 3600
    lam  = g / C
    x    = min(q_s / (s_s * lam), 0.99) if s_s * lam > 0 else 0.99

    d1 = C * (1 - lam) ** 2 / (2 * (1 - lam * x))
    d2 = x ** 2 / (2 * q_s * (1 - x)) if (1 - x) > 0 else 0
    d3 = 0.65 * (C / (q_s ** 2 + 1e-9)) ** (1 / 3) * x ** (2 + 5 * lam)
    return max(d1 + d2 - d3, 0)
