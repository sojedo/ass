def closest_number(numbers, target):
    closest_num = None
    min_diff = float('inf')
    
    for n in numbers:
        diff = abs(n - target)
        if diff < min_diff:
            min_diff = diff
            closest_num = n
            
    return closest_num