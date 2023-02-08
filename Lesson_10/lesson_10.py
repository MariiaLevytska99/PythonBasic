import pytest

class Triangle:
    def __init__(self, sides):
        self.sides = sides

    def is_triangle(self) -> bool:
        # if all(isinstance(side, (float, int)) for side in self.sides):
        if all(side > 0 for side in self.sides):
            sorted_sides = sorted(self.sides)
            if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                return True
        return False
        # return False

triangle = Triangle([2, 3, 4])
print(triangle.is_triangle())


@pytest.mark.parametrize("a", [([2, 3, 4]), ([3, 3, 3]), ([2, 3, 3])])
def test_is_triangle(a):
    triangle = Triangle(a)
    assert triangle.is_triangle()