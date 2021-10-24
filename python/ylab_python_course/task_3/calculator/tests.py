import shapes
import unittest


class ErrorsTest(unittest.TestCase):
    def test_nonpositive_arguments(self):
        with self.assertRaises(ValueError, msg="Values must be positive."):
            shapes.Rectangle(3, 0)

    def test_wrong_side_length(self):
        with self.assertRaises(
            ValueError,
            msg="Each side should be shorter than the sum of others.",
        ):
            shapes.Trapezoid(100, 3, 5, 1)

class FormulasTest(unittest.TestCase):
    def test_pyramid_volume(self):
        pyramid = shapes.Pyramid(10)
        volume = 117.85113019775791
        self.assertEqual(pyramid.get_volume(), volume)


def main():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()
