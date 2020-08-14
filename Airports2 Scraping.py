# A file that scrapes the Airports2.csv file and turn lines into objects.
# https://www.kaggle.com/flashgordon/usa-airport-dataset
import csv


class Flights(object):
    # Each object has six parameters.
    # Includes: (string) start location, (string) end location, (int) passenger number, (int) seats, (int) distance, (date) date.
    def __init__(self, sL, eL, numPass, numSeat, distance, date):
        self.sL = sL
        self.eL = eL
        self.numPass = numPass
        self.numSeat = numSeat
        self.distance = distance
        self.date = date

    def returnData(self):
        return self.sL, self.eL, self.numPass, self.numSeat, self.distance, self.date


with open('Airports2.csv', 'r') as csvFile:
    csvReader = csv.reader(csvFile)
    i = 0
    for line in csvReader:
        flight = Flights(line[2], line[3], line[4], line[5], line[7], line[8])
        print(flight.returnData())
        # Input the numbers.
        if i == 100:
            break
        i += 1
