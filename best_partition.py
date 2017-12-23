def best_partition(array, d):
    """input is an array of numbers, and a number d.
    Output is a pair: the first element of the pair is the
    'best' partition of the array (an array of arrays of
    consecutive numbers in the input array), and the
    second element of the pair is the result number -
    the lowest maximum of sums obtainable, and the sum of
    one or more of the arrays in the partition."""
    max_guess = sum(array)
    min_guess = max(array)
    
    while True:
        guess = (min_guess + max_guess) // 2  # int division
        current_sum = 0
        current_group_count = 1
        current_partition = [[]]  # list of lists (or arrays)
        
        for item in array:
            if current_sum + item > guess \
                    and current_group_count < d:
                current_sum = 0
                current_partition.append([])
                current_group_count += 1
            current_sum += item
            current_partition[-1].append(item)
        
        # now current_sum is the sum of the last group
        # all other sums are definitely lower or equal to guess
        # but this last sum might be 'overflowing'
        if current_group_count == d and max_guess <= min_guess:
            break  # here you exit the 'while True' loop
        if current_sum <= guess:
            max_guess = guess
        else:
            min_guess = guess + 1
    
    return current_sum, current_partition


print(best_partition(array=range(2, 60, 3), d=3))