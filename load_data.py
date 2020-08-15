
import csv
from collections import defaultdict
import pickle



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
            destination = row[1]
            distance = row[2]
            if destination not in flights[origin]:
                flights[origin].append(destination)
            if origin not in origins:
                origins.append(origin)
            if destination not in destinations:
                destinations.append(destination)
            distances[(origin, destination)] = float(distance)
            line_count += 1
    print(f'Processed {line_count} lines.')

outfile = open('airline_data.pkl', 'wb')
pickle.dump(distances,outfile)
pickle.dump(flights,outfile)

outfile.close()