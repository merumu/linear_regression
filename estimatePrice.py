import pickle
import click

def checkInt(i):
    try:
        int(i)
    except:
        return False
    return True

def getTheta():
    try:
        with open('cache', 'rb') as fichier:
            my_unpickler = pickle.Unpickler(fichier)
            theta0 = my_unpickler.load()
            theta1 = my_unpickler.load()
            fichier.close()
    except:
        theta0 = 0
        theta1 = 0
    return (theta0, theta1)

def setTheta(theta0, theta1):
    with open('cache', 'wb') as fichier:
        my_pickler = pickle.Pickler(fichier)
        my_pickler.dump(theta0)
        my_pickler.dump(theta1)
        fichier.close()

def estimatePrice(mileage):
    theta0, theta1 = getTheta()
    return theta0 + theta1 * mileage

if __name__ == "__main__":
    theta0, theta1 = getTheta()
    if theta0 == 0 and theta1 == 0:
        setTheta(theta0, theta1)
    mileage = click.prompt("Please type Mileage value (int)", type=int)
    print("The estimate price is : " + str(estimatePrice(mileage)))