from find_flights import find_flight, find_distance
from Emission_Calculator import calcEmission
from price import extra_cost

origin = input("Please enter your origin city, state: ")
dest = input("Please enter your destination city, state: ")
numPeople = int(input("Please enter the number of passengers: "))
path = find_flight(origin, dest)
print(f"Flight from {path[0]} to {path[-1]}")
if path[1] != path[-1]:
    connection = 1
    print(f"Connection at: {path[1]}")
else:
    connection = 0
carbon_emission = calcEmission(find_distance(path), numPeople, connection)
print(f"Total Carbon Emissions: {carbon_emission}")

# Price:
extra_cost = extra_cost(carbon_emission)
print(f"Extra Cost: {extra_cost}")