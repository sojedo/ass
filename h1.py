def two_sum(numbers, target):
    seen = {}

    for index, value in enumerate(numbers):
        need = target - value
        if need in seen:
            return [seen[need], index]
        seen[value] = index

    return None
