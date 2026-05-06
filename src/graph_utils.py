"""Graph loading and enrichment helpers."""

from typing import TYPE_CHECKING

from .costs import bpr

if TYPE_CHECKING:
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


def load_graph(path) -> "nx.MultiDiGraph":
    """Load a GraphML road graph with OSMnx."""
    import osmnx as ox

    return ox.load_graphml(str(path))


def enrich_graph(G: "nx.MultiDiGraph") -> "nx.MultiDiGraph":
    """Add free-flow travel time and capacity attributes in place."""
    import osmnx as ox

    G = ox.add_edge_speeds(G)
    G = ox.add_edge_travel_times(G)
    for u, v, k, data in G.edges(keys=True, data=True):
        data['capacity'] = get_capacity(data.get('highway', 'unclassified'))
        data['t0'] = data.get('travel_time', data['length'] / 8.33)
    return G
