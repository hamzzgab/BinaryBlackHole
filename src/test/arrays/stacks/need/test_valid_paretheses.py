from src.main.arrays.stacks.neet.valid_parentheses import is_valid


class TestValidParentheses:

    def test_case_1(self):
        s = "[]"

        assert is_valid(s) is True

    def test_case_2(self):
        s = "([{}])"

        assert is_valid(s) is True

    def test_case_3(self):
        s = "[(])"

        assert is_valid(s) is False

    def test_case_4(self):
        s = "]"

        assert is_valid(s) is False
