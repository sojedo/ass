def find_smallest(numbers):
    if not numbers:
        return None

    smallest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
    return smallest