from recursion.neet.fibonacci_series import fib

class TestFibonacciSeries:
    def test_fibonacci_series(self):
        assert fib(0) == 0
        assert fib(1) == 1
        assert fib(2) == 1
        assert fib(3) == 2
        assert fib(4) == 3
        assert fib(5) == 5
        assert fib(6) == 8
