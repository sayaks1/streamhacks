import pickle

infile = open('airline_data.pkl','rb')
distances, flights = pickle.load(infile)
infile.close()

def possible_destinations(origin):
    """
    Returns all direct flights from origin
    """
    return list(set(flights[origin]))


def find_flight(origin, dest):
    """
    Finds the minimum distance path between origin and dest.

    Parameters
    ----------
    origin: str
        Starting city, state
    dest: str
        Ending city, state

    Returns
    ------
    path: List[str]
        Names of airports traveled through
    """
    path = [origin]
    layer_destinations = possible_destinations(origin)
    if dest in layer_destinations:
        path.append(dest)
    else:
        possible_dists = {} # maps total distance for a path to the connecting city
        for possible in layer_destinations:
            if dest in possible_destinations(possible):
                total_dist = distances[(origin, possible)] + distances[(possible, dest)]
                possible_dists[total_dist] = possible
        if len(possible_dists) == 0:
            return "Bad luck today. Too many connections, too bad for the environment, too bad for you."
        connection = possible_dists[min(possible_dists.keys())]
        path.append(connection)
        path.append(dest)
        
    return path

def find_distance(path):
    total_dist = 0
    for i in range(len(path)-1):
        first, second = path[i:i+2]
        total_dist += distances[(first, second)]
    return total_dist
#example: returns all direct flights out of Rochester
# possible_destinations("Rochester, NY")

#example: Finds shortest path from Rochester to Las Vegas
# path = find_flight("Rochester, NY", "Las Vegas, NV")
# print(find_distance(path))







