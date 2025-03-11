def is_valid(s: str) -> bool:
    brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}
    stack = []

    for curr_bracket in s:
        if curr_bracket in list(brackets.keys()):
            stack.append(curr_bracket)
        else:
            if len(stack) == 0:
                return False

            top = stack.pop()

            if brackets[top] != curr_bracket:
                return False

    if len(stack) != 0:
        return False

    return True
