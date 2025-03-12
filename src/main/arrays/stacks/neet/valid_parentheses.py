from src.main.arrays.stacks.Stack import Stack


def is_valid(s: str) -> bool:
    brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}
    stack = Stack(_empty_val=None, _max=len(s))

    for curr_bracket in s:
        if curr_bracket in list(brackets.keys()):
            stack.push(curr_bracket)
        else:
            if len(stack) == 0:
                return False

            top = stack.pop()

            if brackets[top] != curr_bracket:
                return False

    if len(stack) != 0:
        return False

    return True


is_valid(s='([{}])')