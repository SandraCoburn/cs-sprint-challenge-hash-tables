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
    for file in range(len(files)):
        cache[files[file]] = file
       
        for char in queries:
            if file.endswith(char):
                # cache[files[file]] = file 
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
