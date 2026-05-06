import unittest

from src.webster import webster_cycle, webster_delay, webster_greens


class WebsterTests(unittest.TestCase):
    def test_cycle_bounds(self):
        self.assertEqual(webster_cycle(Y=0, L=8), 30)
        self.assertEqual(webster_cycle(Y=1.2, L=8), 180)

    def test_green_allocation(self):
        self.assertEqual(webster_greens([], cycle=60, L=8), [])
        self.assertEqual(webster_greens([1, 1], cycle=60, L=10), [25, 25])

    def test_delay_non_negative(self):
        self.assertGreaterEqual(webster_delay(q=600, s=1800, g=30, C=90), 0)
        self.assertEqual(webster_delay(q=0, s=1800, g=30, C=90), 0)


if __name__ == "__main__":
    unittest.main()
