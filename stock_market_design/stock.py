import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



class Company:
    def __init__(self, array):
        self.name = array[1]
        self.members = array[2]
        self.product = array[3]
        self.costs = int(array[4])
        self.incomes = int(array[5])
        self.worth = self.incomes - self.costs

    def add_costs(self, cost):
        self.costs += cost
        self.worth -= cost
        return self.worth

    def add_incomes(self, income):
        self.incomes += income
        self.worth += income
        return self.worth

    def rank(self, list):
        for x in list:
            print(x)






# call
class_1 = []
class_2 = []

f = open('example.csv')
csv_f = csv.reader(f)

for row in csv_f:
  class_1.append(row)

objs = []
for x in range(1, len(class_1)):
    objs.append(Company(class_1[x]))

print(objs[0].name)
