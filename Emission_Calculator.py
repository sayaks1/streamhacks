# For every kWH of energy supplied by gas or fuel, the CO2 emissions are 0.206 to 0.281kg CO2s.
# For fuel, 2.317kg CO2/litre of fuel.
# Freight factor is 22%.
# 66.3, 81.2 and 78.1% for passenger emission, domestic, short or long haul.
# Emission per passenger: (50/(x+300))+(1/20).


# Add the utilizing of the this method, include connecting points.
# Returns total CO2 emission on the flight, KG.
def calcEmission(distance, numPass, numCon):
    passEmission = ePerPassengerKG(distance)*numPass
    passEmission *= distance
    if distance < 4000:
        percentPassE = 0.663
    elif distance < 4800:
        percentPassE = 0.812
    else:
        percentPassE = 0.781
    totalEmission = passEmission/percentPassE
    fTime = distance/900
    totalEmission = ((1.7*numPass*90*fTime) + 1.8*totalEmission)/2
    totalEmission += numCon*totalEmission*(2.8/100)
    return totalEmission

def ePerPassengerKG(distance):
    distance += 300
    distance = 50 / float(distance)
    distance += (1 / 17)
    return distance


# Test.
print(calcEmission(892, 1, 1))
