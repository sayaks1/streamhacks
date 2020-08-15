from find_flights import find_flight, possible_destinations

# print(possible_destinations("Rochester, NY"))
path = find_flight("Rochester, NY", "Greensboro/High Point, NC")
print(f"Flight from {path[0]} to {path[2]}")
print(f"Connection at: {path[1]}")