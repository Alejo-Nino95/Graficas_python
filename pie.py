import matplotlib.pyplot as plt
import csv

def run():
    with open("./data.csv") as file:
        reader = csv.reader(file, delimiter=",")
        header = next(reader)
        countries = []
        sizes = []
        labels = []
        for row in reader:
            dict = {key:value for (key,value) in zip(header, row)}
            countries.append(dict)
        for c in countries:
            labels.append(c["Country"])
            sizes.append(c["World Population Percentage"])
        fig, ax = plt.subplots()
        ax.set_title("World Population Percentage")
        ax.pie(sizes,labels=labels)
        plt.show()
    
if __name__=="__main__":
    run()