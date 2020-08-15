
import csv
from collections import defaultdict



flights = defaultdict(list)


origins = []
destinations = []
distances = {}



with open('airlines.csv') as csv_file:
    """
    Opens flight data: check off ORIGIN_CITY_NAME, DEST_CITY_NAME, DISTANCE

    Returns
    -------
    origins: List
    destinations: List
    distances: Dictionary
        Maps Tuple of (Origin, Destination) to number of miles
    """
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            origin = row[0]
            dest = row[1]
            distance = row[2]
            if dest not in flights[origin]:
                flights[origin].append(dest)
            if origin not in origins:
                origins.append(origin)
            if dest not in destinations:
                destinations.append(dest)
            distances[(origin, dest)] = float(distance)
            line_count += 1
    print(f'Processed {line_count} lines.')



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
    start = origin
    layer_destinations = possible_destinations(start)
    if dest in layer_destinations:
        finish = dest
        path.append(finish)
    else:
        possible_dists = {} # maps total distance for a path to the connecting city
        for possible in layer_destinations:
            if dest in possible_destinations(possible):
                total_dist = distances[(origin, possible)] + distances[(possible, dest)]
                possible_dists[total_dist] = possible
            else:
                return "Bad luck today. Too many connections, too bad for the environment, too bad for you."
        connection = possible_dists[min(possible_dists.keys())]
        path.append(connection)
        path.append(dest)
        
    return path

#example: returns all direct flights out of Rochester
possible_destinations("Rochester, NY")

#example: Finds shortest path from Rochester to Las Vegas
find_flight("Rochester, NY", "Las Vegas, NV")








