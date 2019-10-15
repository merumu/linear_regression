import sys
import pickle

if __name__ == "__main__":
    try:
        with open('cache', 'rb') as fichier:
            my_unpickler = pickle.Unpickler(fichier)
            tetha0 = my_unpickler.load()
            tetha1 = my_unpickler.load()
            print(tetha0, tetha1, sep="-")
            fichier.close()
    except:
        pass
    tetha0 = 0
    tetha1 = 1
    with open('cache', 'wb') as fichier:
        my_pickler = pickle.Pickler(fichier)
        my_pickler.dump(tetha0)
        my_pickler.dump(tetha1)
        fichier.close()