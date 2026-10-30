def has_cycle(graph):
    visited = set()
    rec_stack = set()

    def visit(node):
        if node in rec_stack:
            return True
        if node in visited:
            return False
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph.get(node, []):
            if visit(neighbor):
                return True
        rec_stack.remove(node)
        return False

    return any(visit(node) for node in graph)
