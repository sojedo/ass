def move_zeros(numbers):
    non_zero_numbers = [num for num in numbers if num != 0]
    zero_count = numbers.count(0)
    return non_zero_numbers + [0] * zero_count