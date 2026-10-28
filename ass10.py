def move_zeros(numbers):
    non_zero_numbers = []
    for number in numbers:
        if number != 0:
            non_zero_numbers.append(number)
    zero_count = numbers.count(0)
    return non_zero_numbers + [0] * zero_count
print(move_zeros([0, 3, 0, 5, 8]))