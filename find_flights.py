
import csv
from collections import defaultdict



flights = defaultdict(list)


origins = []
destinations = []
distances = {}



with open('airlines.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            origin = row[2]
            dest = row[4]
            distance = row[-2]
            if dest not in flights[origin]:
                flights[origin].append(dest)
            if origin not in origins:
                origins.append(origin)
            if dest not in destinations:
                destinations.append(dest)
            distances[(origin, dest)] = distance
            line_count += 1
    print(f'Processed {line_count} lines.')


print(distances)
print(origins)
print(destinations)


def possible_destinations(origin):
    return list(set(flights[origin]))


def find_flight(origin, dest):
    path = [origin]
    start = origin
    layer_destinations = list(set(flights[start]))
    if dest in layer_destinations:
        finish = dest
        path.append(finish)
        searching = False
    else:
        possible_dists = {}
        for possible in layer_destinations:
            if dest in list(set(flights[possible])):
#                 print(possible)
                total_dist = float(distances[(origin, possible)]) + float(distances[(possible, dest)])
                possible_dists[total_dist] = possible
        connection = possible_dists[min(possible_dists.keys())]
        path.append(connection)
        path.append(dest)
        
    return path


possible_destinations("Rochester, NY")


find_flight("Rochester, NY", "Las Vegas, NV")



# to check true value
float(distances[("Burlington, VT", "Chicago, IL")]) + float(distances[("Chicago, IL", 'Los Angeles, CA')])






