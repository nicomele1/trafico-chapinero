"""Minimal route-assignment helpers."""

from itertools import islice


def _simple_weighted_digraph(graph, weight: str):
    import networkx as nx

    simple = nx.DiGraph()
    simple.add_nodes_from(graph.nodes(data=True))
    for u, v, data in graph.edges(data=True):
        edge_weight = data.get(weight, 1)
        if simple.has_edge(u, v) and simple[u][v].get(weight, 1) <= edge_weight:
            continue
        simple.add_edge(u, v, **data)
    return simple


def k_shortest_paths(graph, source, target, k: int, weight: str = "t0") -> list:
    """Return up to k simple shortest paths from source to target."""
    import networkx as nx

    graph_for_paths = (
        _simple_weighted_digraph(graph, weight)
        if graph.is_multigraph()
        else graph
    )
    try:
        paths = nx.shortest_simple_paths(graph_for_paths, source, target, weight=weight)
        return list(islice(paths, k))
    except (nx.NetworkXNoPath, nx.NodeNotFound):
        return []


def route_edges(path: list) -> list[tuple]:
    """Convert a node path into directed edge pairs."""
    return list(zip(path[:-1], path[1:]))


def edge_index(edges: list) -> dict:
    return {edge: idx for idx, edge in enumerate(edges)}


def build_route_edge_incidence(edges: list, routes: list[list]) -> list[list[int]]:
    """Build an edge x route incidence matrix as nested lists."""
    index = edge_index(edges)
    matrix = [[0 for _ in routes] for _ in edges]
    for route_idx, route in enumerate(routes):
        for edge in route_edges(route):
            if edge in index:
                matrix[index[edge]][route_idx] = 1
    return matrix


def edge_flows_from_route_flows(
    incidence: list[list[int]],
    route_flows: list[float],
) -> list[float]:
    return [
        sum(value * flow for value, flow in zip(row, route_flows))
        for row in incidence
    ]


def route_cost(path: list, edge_costs: dict) -> float:
    return sum(edge_costs[edge] for edge in route_edges(path))
