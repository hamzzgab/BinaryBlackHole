from src.main.calculator.calculator import add

class TestCalculator:
    def test_add(self):
        assert add(2, 3) == 5