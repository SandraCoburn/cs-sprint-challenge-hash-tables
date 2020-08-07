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
    result = []
    for file in files:
        if file not in cache:
            cache[file] = file
        for char in queries:
            if file.endswith(char):
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
