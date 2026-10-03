import sys
import unittest
from pathlib import Path

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "traxis-1.0.2"))

from traxis.calc.circlefit import _distanceResiduals, fitCircle


class _Coordinate:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def x(self):
        return self._x

    def y(self):
        return self._y


class _Rectangle:
    def __init__(self, x, y):
        self._centre = _Coordinate(x, y)

    def center(self):
        return self._centre


class _Ellipse:
    def __init__(self, x, y):
        self._rectangle = _Rectangle(x, y)

    def rect(self):
        return self._rectangle


class _Marker:
    def __init__(self, x, y):
        self.ellipse = _Ellipse(x, y)


class _MarkerList:
    def __init__(self, points):
        self._markers = [_Marker(x, y) for x, y in points]

    def count(self):
        return len(self._markers)

    def item(self, index):
        return self._markers[index]


class CircleFitTests(unittest.TestCase):
    def test_distance_residuals_vanish_for_circle_points(self):
        angles = np.linspace(0.0, 2.0 * np.pi, 8, endpoint=False)
        x_values = 3.0 + 5.0 * np.cos(angles)
        y_values = -2.0 + 5.0 * np.sin(angles)
        residuals = _distanceResiduals((3.0, -2.0), x_values, y_values)
        np.testing.assert_allclose(residuals, 0.0, atol=1e-12)

    def test_fit_circle_recovers_known_geometry(self):
        angles = np.linspace(0.0, 2.0 * np.pi, 12, endpoint=False)
        points = [
            (3.0 + 5.0 * np.cos(angle), -2.0 + 5.0 * np.sin(angle))
            for angle in angles
        ]
        fitted = fitCircle(_MarkerList(points))
        self.assertAlmostEqual(fitted["centerX"], 3.0, places=10)
        self.assertAlmostEqual(fitted["centerY"], -2.0, places=10)
        self.assertAlmostEqual(fitted["radius"], 5.0, places=10)


if __name__ == "__main__":
    unittest.main()
