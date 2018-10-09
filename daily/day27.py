"""
Given a string of round, curly, and square open and closing brackets, 
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

def balanced(string:str) -> bool:
    # assuming well-formed input
    pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    stack = []
    for ch in string:
        if ch in ["(", "[", "{"]:
            stack.append(ch)
        else:
            popped = stack.pop()
            if pairs[popped] != ch:
                return False
    if not stack:
        return True
    return False

def test_it():
    assert balanced("([])[]({})") == True
    assert balanced("([)]") == False
    assert balanced("((()") == False
