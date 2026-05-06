import unittest

from src.assignment import (
    build_route_edge_incidence,
    edge_flows_from_route_flows,
    route_cost,
    route_edges,
)


class AssignmentTests(unittest.TestCase):
    def test_route_edges(self):
        self.assertEqual(route_edges(["a", "b", "c"]), [("a", "b"), ("b", "c")])

    def test_incidence_and_edge_flows(self):
        edges = [("a", "b"), ("b", "c"), ("a", "c")]
        routes = [["a", "b", "c"], ["a", "c"]]

        incidence = build_route_edge_incidence(edges, routes)

        self.assertEqual(incidence, [[1, 0], [1, 0], [0, 1]])
        self.assertEqual(edge_flows_from_route_flows(incidence, [10, 5]), [10, 10, 5])

    def test_route_cost(self):
        costs = {("a", "b"): 2.5, ("b", "c"): 3.0}

        self.assertEqual(route_cost(["a", "b", "c"], costs), 5.5)


if __name__ == "__main__":
    unittest.main()
