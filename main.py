import matplotlib.pyplot as plt
import csv
import random

def run():
    with open("./data.csv") as file:
        reader = csv.reader(file, delimiter=",")
        header = next(reader)
        countries = []
        labels = [1970,1980,1990,2000,2010,2015,2020,2022]
        values = []
        for row in reader:
            dict = {key:value for (key,value) in zip(header, row)}
            countries.append(dict)
        country = random.choice(countries)
        cPop = list(country.values())
        for i in range(-4, -12, -1):
            values.append(int(cPop[i]))
        fig, ax = plt.subplots()
        ax.bar(labels, values)
        ax.set_title(country["Country"])
        plt.show()
    
if __name__=="__main__":
    run()