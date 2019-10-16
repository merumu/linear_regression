import csv
import collections
from estimatePrice import getTheta, setTheta, estimatePrice, checkInt

def readData():
    line = -1
    try:
        with open('data.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            data = collections.OrderedDict()
            for row in csv_reader:
                if line == -1:
                    print(f'Column names are {", ".join(row)}')
                    line += 1
                else:
                    if len(row) == 2 and checkInt(row[0]) and checkInt(row[1]):
                        data[row[0]] = row[1]
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
    for km, price in data.items():
        tmpT0 += estimatePrice(int(km)) - int(price)
        tmpT1 += (estimatePrice(int(km)) - int(price)) * int(km)
        m += 1
    tmpT0 = tmpT0 * learningRate * (1/m)
    tmpT1 = tmpT1 * learningRate * (1/m)
    print("new theta :", tmpT0, tmpT1, sep="  ")
    setTheta(tmpT0, tmpT1)

if __name__ == "__main__":
    theta0, theta1 = getTheta()
    if theta0 == 0 and theta1 == 0:
        setTheta(theta0, theta1)
    data = readData()
    if data:
        linearRegression(data)