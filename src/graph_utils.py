"""
Utilidades para carga y enriquecimiento del grafo vial.
"""

from pathlib import Path
import osmnx as ox
import networkx as nx

CAPACITY_MAP = {
    'motorway':       2200,
    'motorway_link':  1500,
    'trunk':          2000,
    'trunk_link':     1200,
    'primary':        1800,
    'primary_link':   1200,
    'secondary':      1500,
    'secondary_link': 1000,
    'tertiary':       1200,
    'tertiary_link':   800,
    'residential':     600,
    'living_street':   300,
    'unclassified':    600,
    'service':         300,
}


def get_capacity(highway_val) -> int:
    if isinstance(highway_val, list):
        highway_val = highway_val[0]
    return CAPACITY_MAP.get(str(highway_val), 600)


def load_graph(path) -> nx.MultiDiGraph:
    """Carga un grafo desde GraphML."""
    return ox.load_graphml(str(path))


def enrich_graph(G: nx.MultiDiGraph) -> nx.MultiDiGraph:
    """Añade velocidades, tiempos de viaje libre y capacidades."""
    G = ox.add_edge_speeds(G)
    G = ox.add_edge_travel_times(G)
    for u, v, k, data in G.edges(keys=True, data=True):
        data['capacity'] = get_capacity(data.get('highway', 'unclassified'))
        data['t0'] = data.get('travel_time', data['length'] / 8.33)
    return G


def bpr(t0: float, flow: float, capacity: float,
         alpha: float = 0.15, beta: float = 4) -> float:
    """Función BPR: t(x) = t0 * (1 + alpha * (x/cap)^beta)."""
    return t0 * (1 + alpha * (flow / capacity) ** beta)
