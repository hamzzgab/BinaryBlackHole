from src.main.arrays.stacks.stack import Stack


class TestValidParentheses:

    def test_should_return_default_on_empty_top(self):
        stack = Stack()
        assert stack.top() == -1

    def test_should_return_top_when_stack_not_empty(self):
        stack = Stack()

        top_value = 10
        stack.push(top_value)

        assert stack.top() == top_value

    def test_should_not_push_to_stack_when_full(self):
        stack = Stack(_max=3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.push(4) is None

    def test_should_not_pop_stack_when_empty(self):
        stack = Stack()
        assert stack.pop() == -1
