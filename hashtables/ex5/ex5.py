# Your code here
'''
Given a list of full paths to files, and a list of filenames to query,
report all the full paths that match that filename.
'''


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    cache = {}
    query_c = {}
    result = []
    for file in files:
        cache[file] = None
        #print(file)
    for i in queries:
        query_c[i] = None
    for file in cache:

        for char in query_c:
            if file.endswith(char):
                #cache[file] = file
                result.append(file)
    return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
