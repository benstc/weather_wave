import csv
import math
import random

from datavisualization import visualizedata

# holds frequency variable for sin function
W = (2*math.pi)/365 # set so that there is one cycle per year

class weatherwave():
    def __init__(self, avgtemps):
        self.avgtemps = avgtemps

    def cost(self, equation):
        """
        this function will find the total difference between a given sin function
        specified with the input parameters and the average temperature throughout the year
        returning the float value that is the difference
        """
        cost = 0.0
        # for each day in the temperature data, find the difference between sin function and temp
        for i in range(len(self.avgtemps)):
            sinval = equation[0]*math.sin(W*i + equation[1]) + equation[2]
            diff = abs(sinval-self.avgtemps[i])
            cost += diff
        
        return cost



    def neighbors(self, equation):
        """
        This function will find all of the neighbors of a given sin function,
        of which there will be (3^3 - 1), since each parameter will have 3 neighbors and there are 3 parameter (but we dont want
        to include the neighbor that is itself).

        This function will return a 2-dimensional array with 8 rows, each row corresponding to a neighbor,
        and 3 columns, each column corresponding to a changing parameter to the sin equation.
        """
        a = equation[0]
        o = equation[1]
        h = equation[2]

        adiff = 0.1
        odiff = 0.025
        hdiff = 0.1

        # return all neighbors of a given equation
        neighbors = [[a, o, h+hdiff],
                     [a, o, h-hdiff],
                     [a, o+odiff, h],
                     [a, o+odiff, h+hdiff],
                     [a, o+odiff, h-hdiff],
                     [a, o-odiff, h],
                     [a, o-odiff, h+hdiff],
                     [a, o-odiff, h+hdiff],
                     [a+adiff, o, h],
                     [a+adiff, o, h+hdiff],
                     [a+adiff, o, h-hdiff],
                     [a+adiff, o+odiff, h],
                     [a+adiff, o+odiff, h+hdiff],
                     [a+adiff, o+odiff, h-hdiff],
                     [a+adiff, o-odiff, h],
                     [a+adiff, o-odiff, h+hdiff],
                     [a+adiff, o-odiff, h+hdiff],
                     [a-adiff, o, h],
                     [a-adiff, o, h+hdiff],
                     [a-adiff, o, h-hdiff],
                     [a-adiff, o+odiff, h],
                     [a-adiff, o+odiff, h+hdiff],
                     [a-adiff, o+odiff, h-hdiff],
                     [a-adiff, o-odiff, h],
                     [a-adiff, o-odiff, h+hdiff],
                     [a-adiff, o-odiff, h+hdiff]]
        return neighbors

    def randomequation(self):
        """
        this function will be used to generate a random sin equation to begin the local search algorithm
        """
        a_upperbound = 40
        a_lowerbound = 20
        o_upperbound = -0.75
        o_lowerbound = -math.pi/2
        h_upperbound = 60
        h_lowerbound = 40
        
        a = random.uniform(a_lowerbound, a_upperbound)
        o = random.uniform(o_upperbound, o_lowerbound)
        h = random.uniform(h_upperbound, h_lowerbound)

        return [a, o, h]


    def minimum(self, equation):
        """
        this function will contain the while loop and funciton calls to cost and neighbors
        """
        current_equation = equation
        current_cost = self.cost(current_equation)

        while True:
            neighbors = self.neighbors(current_equation)
            best_neighbor = current_equation
            best_neighbor_cost = current_cost
            for i in range(len(neighbors)):
                temp_cost = self.cost(neighbors[i])
                if temp_cost < best_neighbor_cost:
                    best_neighbor = neighbors[i]
                    best_neighbor_cost = temp_cost
            if best_neighbor_cost < current_cost:
                current_equation = best_neighbor
                current_cost = best_neighbor_cost
            else:
                return current_equation

def parsetemps():
    """
    this function will parse the csv file and return the array of 730 days of avg temps
    """
    avgtemps = []
    with open('data/newCSV.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row in reader:
            avgtemps.append(float(row[4]))
    
    return avgtemps



def main():
    avgtemps = parsetemps()
    findsin = weatherwave(avgtemps=avgtemps)
    randomstart = findsin.randomequation()
    minimumequation = findsin.minimum(randomstart)
    print(f'optimal amplitude: {minimumequation[0]}')
    print(f'optimal phase angle: {minimumequation[1]}')
    print(f'optimum vertical shift: {minimumequation[2]}')
    visualizedata(minimumequation)
    return


if __name__ == "__main__":
    main()