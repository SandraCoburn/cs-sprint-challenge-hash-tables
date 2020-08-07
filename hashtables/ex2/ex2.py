'''
 Each ticket is represented as a class
 - the `source` string represents the starting airport
 - `destination` string represents the next airport
 - The ticket for your first flight has a destination with a `source` of `NONE`
 - the ticket for your final flight has a `source` with a `destination` of `NONE`
tickets = [
    Ticket{ source: "PIT", destination: "ORD" },
    Ticket{ source: "XNA", destination: "CID" },
    Ticket{ source: "SFO", destination: "BHM" },
    Ticket{ source: "FLG", destination: "XNA" },
    Ticket{ source: "NONE", destination: "LAX" },
    Ticket{ source: "LAX", destination: "SFO" },
    Ticket{ source: "CID", destination: "SLC" },
    Ticket{ source: "ORD", destination: "NONE" },
    Ticket{ source: "SLC", destination: "PIT" },
    Ticket{ source: "BHM", destination: "FLG" }
]
'''
#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}
    route = [None] * length

    for i in range(length):
        if tickets[i].source is "NONE":
            route[0] = tickets[i].destination
        if tickets[i].source not in cache:
            cache[tickets[i].source] = tickets[i].destination
    for j in range(length):
        if route[j-1] is not None:
            route[j] = cache[route[j-1]]

    return route
