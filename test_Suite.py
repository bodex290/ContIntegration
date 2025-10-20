import unittest
import numpy as np
import os
from my_function import add_numbers, generate_data, fit_line, plot_line

class TestMyFunction(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_generate_data(self):
        x, y = generate_data(m=1.0, b=0.0, n=10, seed=42, noise=0.0)
        self.assertEqual(len(x), 10)
        self.assertEqual(len(y), 10)
        # With noise=0, y should be exactly m*x + b
        np.testing.assert_allclose(y, x, atol=1e-8)

    def test_fit_line(self):
        x = np.array([0, 1, 2, 3])
        y = 2 * x + 1
        m, b = fit_line(x, y)
        self.assertAlmostEqual(m, 2.0, places=6)
        self.assertAlmostEqual(b, 1.0, places=6)

    def test_plot_line(self):
        x = np.linspace(0, 1, 5)
        y = 2 * x + 1
        m, b = fit_line(x, y)
        filename = "test_plot.png"
        plot_line(x, y, m, b, savepath=filename, show=False)
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()