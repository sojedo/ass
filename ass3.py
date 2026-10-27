def list_sum(numbers):
    if not numbers:
        return 0
    total = 0
    for number in numbers:
        total += number
    return total