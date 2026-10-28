def second_largest(numbers):
    if len(numbers) < 2:
        return None
    largest = None
    second_largest = None
    
    for num in numbers:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif num != largest and (second_largest is None or num > second_largest):
            second_largest = num

    return second_largest

