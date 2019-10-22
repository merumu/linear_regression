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
    learningRate = 0.05
    tmpT0 = 0
    tmpT1 = 0
    theta0, theta1 = getTheta()
    maxKm = max(data)
    minKm = min(data)
    cost = 0
    for km, price in data.items():
        km = km / (maxKm - minKm)
        tmpT0 += estimatePrice(km) - price
        tmpT1 += (estimatePrice(km) - price) * km
        cost += (estimatePrice(km**2) - price**2)**2
        m += 1
    cost = cost / (2*m)
    tmpT0 = theta0 - tmpT0 * learningRate / m
    tmpT1 = theta1 - tmpT1 * learningRate / m
    tmpT1 = tmpT1 / (maxKm - minKm)
    print("new theta :", tmpT0, tmpT1, cost, sep="\t|\t")
    setTheta(tmpT0, tmpT1)
    return cost

if __name__ == "__main__":
    theta0, theta1 = getTheta()
    if theta0 == 0 and theta1 == 0:
        setTheta(theta0, theta1)
    data = readData()
    if data:
        fig, axs = plt.subplots(1, 2, figsize=(15, 5))
        axs[0].set_title('Linear Regression')
        axs[1].set_title('Cost function')
        n = 1
        for i in range(0, 1000):
            cost = linearRegression(data)
            axs[1].scatter(n, cost/1000000)
            n += 1
        mileage = list(data.keys())
        price = list(data.values())
        axs[0].scatter(mileage, price)
        theta0, theta1 = getTheta()
        axs[0].plot([0,max(mileage)], [theta0 , theta0 + theta1 * max(mileage)], color='red', linewidth=3)
        plt.show()