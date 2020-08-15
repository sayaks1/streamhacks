from find_flights import find_flight, find_distance
from Calculator import calcEmission, calcPrice, extra_cost
from flask import Flask

app = Flask(__main__)

@app.route("/")
def home():
    return "main page <h1>HELLO<h1>"

if __name__ == "__main__":
    app.run()

# origin = input("Please enter your origin city, state: ")
# dest = input("Please enter your destination city, state: ")
# numPeople = int(input("Please enter the number of passengers: "))
# path = find_flight(origin, dest)
# print(f"\nFlight from {path[0]} to {path[-1]}")
# if path[1] != path[-1]:
#     connection = 1
#     print(f"Connection at: {path[1]}")
# else:
#     connection = 0
# carbon_emission = calcEmission(find_distance(path), numPeople, connection)
# print(f"Total Carbon Emissions: {carbon_emission} kg")
#
# # Price:
# extra_cost = extra_cost(carbon_emission)
# print(f"\nCarbon Offset Cost: {extra_cost}")
# print(f"Total Cost: ${calcPrice(find_distance(path))+ extra_cost}")

