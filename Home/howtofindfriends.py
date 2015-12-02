"""
Sophia's drones are not soulless and stupid drones; they can make and have
friends. In fact, they already are working for the their own social network
just for drones! Sophia has received the data about the connections between
drones and she wants to know more about relations between them.

We have an array of straight connections between drones. Each connection is
represented as a string with two names of friends separated by hyphen. For
example: "dr101-mr99" means what the dr101 and mr99 are friends. Your should
write a function that allow determine more complex connection between drones.
You are given two names also. Try to determine if they are related through
common bonds by any depth. For example: if two drones have a common friends or
friends who have common friends and so on.

network

Let's look at examples: scout2 and scout3 have the common friend scout1 so they
are related. super and scout2 are related through sscout, scout4 and scout1. But
dr101 and sscout are not related.

Input: Three arguments: Information about friends as a tuple of strings; first
name as a string; second name as a string.

Output: Are these drones related or not as a boolean.

Precondition:
len(network) ≤ 45
if "name1-name2" in network, then "name2-name1" not in network
3 ≤ len(drone_name) ≤ 6
first_name and second_name in network.
"""

def buildGraph(connectionlist):
    """Build a nondirectional graph using '-' separated names

    Represented by a dict in which each key is the name of a node and
    each value is the list of all other nodes it directs to."""
    graph = {}
    for connection in connectionlist:
        k = connection.split("-")[0] # our names are dash-separated
        v = connection.split("-")[1]
        if k in graph:
            graph[k].append(v)
        else:
            graph[k] = [v]
        # graph is nondirectional, so connect both directions
        if v in graph:
            graph[v].append(k)
        else:
            graph[v] = [k]
    return graph

def findPath(graph, start, end, path):
    """From https://www.python.org/doc/essays/graphs/"""
    path.append(start)
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = findPath(graph, node, end, path)
            if newpath: return newpath
    return None

def check_connection(network, first, second):
    graph = buildGraph(network)
    path = findPath(graph, first, second, [])
    if path == None:
        return False
    else:
        return True

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
