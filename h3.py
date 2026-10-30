def valid_parentheses(text):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in text:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack == [] or mapping[char] != stack.pop():
                return False
    return stack == []
print(valid_parentheses("{[}"))