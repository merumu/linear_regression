import sys
import pickle
import csv

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
    tetha0 = 41
    tetha1 = 42
    with open('cache', 'wb') as fichier:
        my_pickler = pickle.Pickler(fichier)
        my_pickler.dump(tetha0)
        my_pickler.dump(tetha1)
        fichier.close()
    try:
        with open('data.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line = 0
            for row in csv_reader:
                if line == 0:
                    print(f'Column names are {", ".join(row)}')
                    line += 1
                else:
                    print(f'\t{row[0]}km = {row[1]}$')
                    line += 1
    except:
        line = 0
    print(f'Processed {line} lines.')