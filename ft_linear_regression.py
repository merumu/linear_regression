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
                    print(f'Column mileage are {", ".join(row)}')
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
    learningRate = 0.1
    tmpT0 = 0
    tmpT1 = 0
    theta0, theta1 = getTheta()
    maxKm = max(data)
    minKm = min(data)
    for km, price in data.items():
        km = (km - minKm) / (maxKm - minKm)
        tmpT0 += estimatePrice(km) - price
        tmpT1 += (estimatePrice(km) - price) * km
        m += 1
    tmpT0 = theta0 - tmpT0 * learningRate / m
    tmpT1 = theta1 - tmpT1 * learningRate / m
    tmpT1 = tmpT1 / (maxKm - minKm)
    print("new theta :", tmpT0, tmpT1, sep="\t")
    setTheta(tmpT0, tmpT1)

if __name__ == "__main__":
    theta0, theta1 = getTheta()
    if theta0 == 0 and theta1 == 0:
        setTheta(theta0, theta1)
    data = readData()
    if data:
        for i in range(0,80):
            linearRegression(data)
    mileage = list(data.keys())
    price = list(data.values())
    plt.scatter(mileage, price)
    theta0, theta1 = getTheta()
    plt.plot([0,max(mileage)], [theta0 , theta0 + theta1 * max(mileage)], color='red', linewidth=3)
    plt.show()