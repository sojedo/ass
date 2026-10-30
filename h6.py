def missing_number(numbers):
    if not numbers:
        return []

    min_num = min(numbers)
    max_num = max(numbers)
    full_set = set(range(min_num, max_num + 1))
    missing = full_set - set(numbers)

    return sorted(list(missing))
print(missing_number([3, 0, 1]))  