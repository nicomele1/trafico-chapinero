# Theory Outline

These notes summarize the mathematical objects used by the notebooks. The purpose is to fix notation, not to present a complete treatment of traffic assignment.

## Road graph

We model the road network as a directed graph `G=(V,E)`. The set `V` contains nodes and the set `E` contains directed edges. A route is a directed path from an origin node to a destination node.

For a route `p`, let `f_p >= 0` denote the route flow. Edge flows are induced by route flows through the incidence coefficients

```text
delta[e,p] = 1 if edge e is in route p, and 0 otherwise.
```

Thus

```text
x_e = sum_p delta[e,p] * f_p.
```

## BPR cost function

For each edge `e`, let `t_e^0 > 0` denote free-flow travel time and let `c_e > 0` denote capacity. The BPR cost function is

```text
t_e(x_e) = t_e^0 * (1 + alpha * (x_e / c_e)^beta).
```

In this repository, the default parameters are `alpha = 0.15` and `beta = 4`. The function is used as a simple congestion model, not as a locally calibrated empirical law.

The Beckmann integral for BPR costs is

```text
integral_0^x t_e(u) du = t_e^0*x + alpha*t_e^0*x^(beta+1)/((beta+1)*c_e^beta).
```

## Wardrop equilibrium

Wardrop user equilibrium means that, for each origin-destination pair, all used routes have minimal route cost among the available routes. In the finite-route formulation used here, this condition is imposed over the enumerated candidate routes.

For separable increasing edge costs, the Wardrop equilibrium can be computed through the Beckmann objective

```text
sum_e integral_0^{x_e} t_e(u) du.
```

## Social optimum

The system-optimum assignment minimizes total system cost,

```text
TC(x) = sum_e x_e * t_e(x_e),
```

over the same feasible route-flow set. This objective is not the same as the Beckmann objective unless costs are constant.

The marginal social cost on edge `e` is

```text
MC_e(x_e) = d[x_e*t_e(x_e)]/dx_e = t_e(x_e) + x_e*t_e'(x_e).
```

## Webster signal timing

For a signalized intersection with total lost time `L` and critical flow ratios `y_i = q_i/s_i`, Webster's cycle formula is

```text
C_0 = (1.5*L + 5) / (1 - Y),  where Y = sum_i y_i.
```

The effective green time for phase `i` is

```text
g_i = (C_0 - L) * y_i / Y.
```

The notebooks apply these formulas to simplified phase groups inferred from the graph and modeled flows. The calculation is not calibrated against observed signal timing data.
