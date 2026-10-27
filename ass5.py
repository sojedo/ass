def count_occurrences(numbers, target):
    count = 0
    for number in numbers:
        if number == target:
            count += 1
    return count
    