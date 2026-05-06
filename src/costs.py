"""Travel-time cost formulas."""


def bpr(
    t0: float,
    flow: float,
    capacity: float,
    alpha: float = 0.15,
    beta: float = 4,
) -> float:
    """BPR travel time for one edge."""
    if capacity <= 0:
        raise ValueError("capacity must be positive")
    return t0 * (1 + alpha * (flow / capacity) ** beta)


def beckmann_bpr_integral(
    t0: float,
    flow: float,
    capacity: float,
    alpha: float = 0.15,
    beta: float = 4,
) -> float:
    """Integral of the BPR cost from 0 to flow."""
    if capacity <= 0:
        raise ValueError("capacity must be positive")
    return t0 * flow + t0 * alpha * flow ** (beta + 1) / (
        (beta + 1) * capacity ** beta
    )


def total_system_cost_bpr(
    t0: float,
    flow: float,
    capacity: float,
    alpha: float = 0.15,
    beta: float = 4,
) -> float:
    """System cost x * t(x) for one edge."""
    return flow * bpr(t0, flow, capacity, alpha=alpha, beta=beta)


def marginal_cost_bpr(
    t0: float,
    flow: float,
    capacity: float,
    alpha: float = 0.15,
    beta: float = 4,
) -> float:
    """Marginal system cost d[x*t(x)]/dx for one edge."""
    if capacity <= 0:
        raise ValueError("capacity must be positive")
    return t0 * (1 + alpha * (beta + 1) * (flow / capacity) ** beta)


def pigou_toll_bpr(
    t0: float,
    flow: float,
    capacity: float,
    alpha: float = 0.15,
    beta: float = 4,
) -> float:
    """External cost x * t'(x) for one edge."""
    if capacity <= 0:
        raise ValueError("capacity must be positive")
    return t0 * alpha * beta * flow ** beta / capacity ** beta
