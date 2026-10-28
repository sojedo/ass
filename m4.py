def reverse_first(queue, k):
    if k > len(queue) or k <= 0:
        return queue

    stack = []
    for _ in range(k):
        stack.append(queue.pop(0))

    while stack:
        queue.append(stack.pop())

    for _ in range(len(queue) - k):
        queue.append(queue.pop(0))

    return queue
