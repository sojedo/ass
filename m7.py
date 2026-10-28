def first_position(numbers):
    visited = set()
    for i, n in enumerate(numbers):
        if n in visited:
            return i
        visited.add(n)
    return -1