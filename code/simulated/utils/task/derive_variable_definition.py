
def remove_repeated_subpatterns(sequence):
    """
    Remove repeated subpatterns from the sequence using iteration.

    Args:
        sequence (list): A list of elements in the sequence.

    Returns:
        list: The sequence with repeated subpatterns removed.
    """
    n = len(sequence)
    for i in range(1, n):
        is_repeated = True
        # Check if the sequence is a repetition of sequence[:i]
        for j in range(i, n):
            if sequence[j] != sequence[j % i]:
                is_repeated = False
                break
        if is_repeated:
            return sequence[:i]
    return sequence

def reorder_sequence(sequence):
    """
    Reorders a sequence by detecting breaks in the trend and combining them in order.

    Args:
        sequence (list): A list of integers with a circular order.

    Returns:
        list: The reordered sequence in increasing order.
    """
    n = len(sequence)
    breaks = []
    
    # Find points where the sequence suddenly reverses (decreases)
    for i in range(1, n):
        if sequence[i] < sequence[i - 1]:
            breaks.append(i)
    
    # Split the sequence into pieces at the breaks
    pieces = []
    start = 0
    for b in breaks:
        pieces.append(sequence[start:b])
        start = b
    pieces.append(sequence[start:])  # Add the last piece
    
    # Sort and concatenate the pieces
    ordered_sequence = sorted(sum(pieces, []))
    return ordered_sequence

def get_previous_item(lst, item):
    """
    Returns the previous item in the list with wrap-around behavior.
    
    Args:
        lst (list): The list of items.
        item: The item whose previous item is to be found.

    Returns:
        The previous item in the list, or None if the list is empty.
    """
    if not lst:  # Check if the list is empty
        return None
    
    try:
        index = lst.index(item)  # Get the index of the item
        previous_index = (index - 1) % len(lst)  # Calculate the previous index with wrap-around
        return lst[previous_index]
    except ValueError:
        return None  # Return None if the item is not found in the list

def analyze_continuous_sequence(sequence, being_affected_by_actions = False, revert_back_later = True):
    """
    Analyzes a sequence to determine value ranges, step values, and the current value.

    Args:
        sequence (list): A list of integers representing the sequence.

    Returns:
        tuple: A tuple containing:
            - list of lists: Each sublist contains [start, end, step] for a value range.
            - int: The current value (first element of the sequence).
    """

    has_repeated_value = (len(sequence) != len(set(sequence)))
    if revert_back_later:
        current_value = sequence[0]
    else:
        current_value = sequence[-1]
    
    ###
    """
    if not has_repeated_value:
        if being_affected_by_actions:
            return "the same as previously defined", f"the value before {current_value} in the value range"
        else:
            return "the same as previously defined", current_value
    """
    unique_sequence = remove_repeated_subpatterns(sequence)
    reordered_sequence = reorder_sequence(unique_sequence)
    
    
    ranges = []
   
    n = len(reordered_sequence)
    
    start = reordered_sequence[0]
    step = None

    for i in range(1, n):
        # Calculate step
        diff = reordered_sequence[i] - reordered_sequence[i - 1]
        if step is None:
            step = diff

        # Check if step changes
        if diff != step:
            # Add the current range to the list
            ranges.append([start, reordered_sequence[i - 1], step])
            # Update start and step for the next range
            start = reordered_sequence[i - 1]
            step = diff

    # Add the final range
    ranges.append([start, reordered_sequence[-1], step])

    if revert_back_later and being_affected_by_actions:
        current_value = get_previous_item(reordered_sequence, current_value)
    return ranges, current_value

def analyze_discrete_sequence(sequence, being_affected_by_actions = False, revert_back_later = True):
    """
    Analyzes a sequence to determine value ranges, and the current value.

    Args:
        sequence (list): A list of strings representing the sequence.

    Returns:
        tuple: A tuple containing:
            - list of strings: a value range.
            - string: The current value (first element of the sequence).
    """

    unique_sequence = remove_repeated_subpatterns(sequence)
    if revert_back_later:
    
        current_value = sequence[0]
        
        if being_affected_by_actions:
            current_value = get_previous_item(unique_sequence, current_value)
    else:
        current_value = sequence[-1]
    return unique_sequence, current_value



if __name__ == "__main__":
    # Example Usage
    print(analyze_continuous_sequence([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3, 4]))
    # Output: ([0, 10, 1], 0)

    print(analyze_continuous_sequence([0, 2, 4, 6, 8, 10, 0, 2, 4]))
    # Output: ([0, 10, 2], 0)

    print(analyze_continuous_sequence([3, 4, 5, 6, 7, 8, 9, 3, 4, 5]))
    # Output: ([3, 9, 1], 3)

    print(analyze_continuous_sequence([3, 4, 5, 6, 7, 8, 9, 0, 3, 4, 5, 6]))
    # Output: ([[0, 3, 3], [3, 9, 1]], 3)

    print(analyze_continuous_sequence([9, 8, 7, 6, 5, 0, 9, 8, 7, 6, 5]))
    # Output: ([[0, 3, 3], [3, 9, 1]], 3)

    print(analyze_discrete_sequence(["4H", "6H", "8H", "10H", "Off", "4H", "6H", "8H", "10H", "Off", "4H"]))
    # output: (['4H', '6H', '8H', '10H', 'Off'], '4H')

