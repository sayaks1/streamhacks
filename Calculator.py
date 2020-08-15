# For every kWH of energy supplied by gas or fuel, the CO2 emissions are 0.206 to 0.281kg CO2s.
# For fuel, 2.317kg CO2/litre of fuel.
# Freight factor is 22%.
# 66.3, 81.2 and 78.1% for passenger emission, domestic, short or long haul.
# Emission per passenger: (50/(x+300))+(1/20).


# Returns total CO2 emission on the flight, KG.
def calcEmission(distance, numPass, numCon):
    passEmission = ePerPassengerKG(distance)*numPass
    passEmission *= distance
    if distance < 4000:
        percentPassE = 0.663
        rate = 6
    elif distance < 4800:
        percentPassE = 0.812
        rate = 4
    else:
        percentPassE = 0.781
        rate = 2.8
    totalEmission = passEmission/percentPassE
    fTime = distance/900
    totalEmission = ((1.7*numPass*90*fTime) + 1.8*totalEmission)/2
    totalEmission += numCon*totalEmission*(rate/100)
    return int(totalEmission)

# Calculates the average passenger CO2 emission per km
def ePerPassengerKG(distance):
    distance += 300
    distance = 50 / float(distance)
    distance += (1 / 17)
    return distance

def calcPrice(distance):
    price = 0.129*distance
    price += 200
    return int(price)


# Test.
print(str(calcEmission(892, 1, 2)) + "kg of CO2 emitted!")
print("The flight's price is $" + str(calcPrice(892)))
