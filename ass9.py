def first_duplicate(numbers):
    visited = set()
    for n in numbers:
        if n in visited:
            return n
        visited.add(n)
    return None