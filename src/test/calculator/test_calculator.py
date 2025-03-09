from src.main.calculator.calculator import add, sub


class TestCalculator:
    def test_add(self):
        assert add(2, 3) == 5

    def test_sub(self):
        assert sub(5, 2) == 3
