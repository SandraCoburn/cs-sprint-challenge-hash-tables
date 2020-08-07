'''
list of lists that contain integers:
- we need to compute the _intersection_, that is, numbers that exist
in all lists
- the return value will be: [1, 2]
- Output can be in any order
Limits:

* There can be up to 10 lists in the list of lists.
* The lists can contain up to roughly 1,000,000 elements each.

'''

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    for arr in arrays:
        for num in arr:
            if num in cache:
                cache[num] += 1
            else:
                cache[num] = 1
    for num in cache:
        if cache[num] == len(arrays):
            result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

   # print(intersection(arrays))
arr = [[1,2,3], [1,2,4], [1,2,5,8,7]]
print(intersection(arr))
