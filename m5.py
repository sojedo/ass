def most_frequent(numbers):
    frequency = {}
    max_count = 0
    most_freq_num = None
    
    for n in numbers:
        frequency[n] = frequency.get(n, 0) + 1
        if frequency[n] > max_count:
            max_count = frequency[n]
            most_freq_num = n
            
    return most_freq_num