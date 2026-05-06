import unittest

from src.graph_utils import get_capacity


class GraphUtilsTests(unittest.TestCase):
    def test_capacity_from_string(self):
        self.assertEqual(get_capacity("primary"), 1800)

    def test_capacity_from_list(self):
        self.assertEqual(get_capacity(["residential", "service"]), 600)

    def test_capacity_default(self):
        self.assertEqual(get_capacity("unknown"), 600)


if __name__ == "__main__":
    unittest.main()
