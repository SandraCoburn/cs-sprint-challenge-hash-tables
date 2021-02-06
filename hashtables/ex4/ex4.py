'''
- which positive numbers have corresponding negative numbers in the list.
- Return value can be in any order.

- Solve this problem with a hash table.
'''
def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    for ele in a:
       
        if -ele in cache:
            cache[-ele] = ele
            cache[ele] = -ele
        else:
            cache[ele] = None

    for num in cache:
        if num > 0 and cache[num] is not None:
            result.append(num)

    
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
