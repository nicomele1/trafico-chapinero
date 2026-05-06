import unittest

from src.costs import (
    beckmann_bpr_integral,
    bpr,
    marginal_cost_bpr,
    pigou_toll_bpr,
    total_system_cost_bpr,
)


class CostTests(unittest.TestCase):
    def test_bpr_free_flow(self):
        self.assertEqual(bpr(t0=10, flow=0, capacity=1000), 10)

    def test_bpr_at_capacity(self):
        self.assertAlmostEqual(bpr(t0=10, flow=1000, capacity=1000), 11.5)

    def test_beckmann_integral(self):
        value = beckmann_bpr_integral(t0=10, flow=1000, capacity=1000)

        self.assertAlmostEqual(value, 10300)

    def test_system_and_marginal_cost(self):
        self.assertAlmostEqual(
            total_system_cost_bpr(t0=10, flow=1000, capacity=1000),
            11500,
        )
        self.assertAlmostEqual(
            marginal_cost_bpr(t0=10, flow=1000, capacity=1000),
            17.5,
        )

    def test_pigou_toll(self):
        self.assertAlmostEqual(pigou_toll_bpr(t0=10, flow=1000, capacity=1000), 6)


if __name__ == "__main__":
    unittest.main()
