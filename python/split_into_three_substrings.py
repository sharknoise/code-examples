"""https://www.geeksforgeeks.org/count-ways-to-split-a-binary-string-into-three-substrings-having-equal-count-of-zeros/"""

def count_ways(binary_string):
    """Count the total number of ways to split a binary string into three
    non-overlapping substrings having the same number of 0s"""

    # Store total count of 0s
    zero_total = 0
 
    # Count total no. of 0s
    # character in given string
    for char in binary_string:
        if char == '0':
            zero_total += 1
 
    # If total count of 0
    # character is not
    # divisible by 3
    if (zero_total % 3 != 0):
        return 0
 
    way_count = 0
    zero_req = zero_total // 3  # number of 0 required in each partition
    current_zero_count = 0
 
    # Initialize map to store
    # frequency of zero_req
    mp = {}
 
    # Traverse string to find
    # ways to split string
    for i in range(len(binary_string)):
 
        # Increment count if 0 appears
        if binary_string[i] == '0':
            current_zero_count += 1
 
        # Increment result if sum equal to
        # 2*zero_req and zero_req exists in map
        if (current_zero_count == 2 * zero_req and zero_req in mp and
            i < len(binary_string) - 1 and i > 0):
            way_count += mp[zero_req]
 
        # Update the frequency of sum
        if current_zero_count in mp:
            mp[current_zero_count] += 1
        else:
            mp[current_zero_count] = 1
             
    return way_count
 
# test
print(count_ways('000'))