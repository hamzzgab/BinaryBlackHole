from src.main.recursion.neet.factorial import fact


class TestFactorial:
    def test_factorial(self):
        assert fact(0) == 1
        assert fact(1) == 1
        assert fact(2) == 2
        assert fact(3) == 6
        assert fact(4) == 24
        assert fact(5) == 120
