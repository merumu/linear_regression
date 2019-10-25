import csv
import matplotlib.pyplot as plt
from estimatePrice import *

def readData():
    line = -1
    try:
        with open('data.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            data = {}
            for row in csv_reader:
                if line == -1:
                    print(f'Column are {", ".join(row)}')
                    line += 1
                else:
                    if len(row) == 2 and checkInt(row[0]) and checkInt(row[1]):
                        data[int(row[0])] = int(row[1])
                        line += 1
            print(f'Processed {line} lines')
            csv_file.close()
    except:
        pass
    if line > 0:
        return data
    return None

def linearRegression(data):
    m = 0
    learningRate = 0.5
    tmpT0 = 0
    tmpT1 = 0
    theta0, theta1 = getTheta()
    maxKm = max(data)
    minKm = min(data)
    if maxKm == minKm:
        printError('only one x value in data, can\'t process')
    cost = 0
    for km, price in data.items():
        kmNormalized = (km - minKm) / (maxKm - minKm)
        try:
            tmpT0 += (estimatePrice(km) - price)
            tmpT1 += (estimatePrice(km) - price) * kmNormalized
            cost += (estimatePrice(km) - price)**2
            m += 1
        except:
            printError('Linear Regression had an overflow. Try to modify the learningRate or the data')
    cost = cost / (2*m)
    tmpT1 = tmpT1 / (maxKm - minKm)
    theta0 = theta0 - tmpT0 * learningRate / m
    theta1 = theta1 - tmpT1 * learningRate / m
    setTheta(theta0, theta1)
    print("theta0 : ", theta0, "\ttheta1 : ", theta1, "\tcost : ", cost, sep=" ")
    return cost

def printRegression(data):
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))
    axs[0].set_title('Linear Regression')
    axs[0].set_xlabel('Mileage')
    axs[0].set_ylabel('Price')
    axs[1].set_title('Cost function')
    axs[1].set_xlabel('Number of iterations')
    axs[1].set_ylabel('Cost')
    n = 1
    cost = 0
    preCost = 999999
    while (abs(cost - preCost) > 0.1):
        preCost = cost
        cost = linearRegression(data)
        axs[1].scatter(n, cost)
        n += 1
    mileage = list(data.keys())
    price = list(data.values())
    axs[0].scatter(mileage, price)
    theta0, theta1 = getTheta()
    axs[0].plot([0,max(mileage)], [theta0 , theta0 + theta1 * max(mileage)], color='red', linewidth=3)
    plt.show()

if __name__ == "__main__":
    theta0, theta1 = getTheta()
    if theta0 == 0 and theta1 == 0:
        setTheta(theta0, theta1)
    data = readData()
    if data:
        printRegression(data)
    else:
        printError("no data found")