
"""
    - Given a package with a weight limit `limit` and a list `weights` of item
weights
    - find two items whose sum of weights equals the weight limit `limit`.
    - return a tuple of integers that has the following form: (zero, one)
    - each element represents the item weights of the two packages
    - The higher valued index should be placed in the `zeroth` index and
the smaller index should be placed in the `first` index.
    - Function should return None if that condition doesn't exist
    ex: input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
 """
    # Your code here
def get_indices_of_item_weights(weights, length, limit):
    cache = {}
    for index, num in enumerate(weights):
        for index2, num2 in enumerate(weights):
            if num + num2 == limit:
                if num > num2:
                    if index not in cache:
                        cache[index] = index2
                        match = index, index2
                        return match
                else: 
                    cache[index2] = index
                    match = index2, index
                    return match
    

    return None

weights = [ 4, 6, 10, 15, 16 ]
length = 5 
limit = 21
get_indices_of_item_weights(weights, length, limit)