from collections import Counter
import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")
data = pd.read_csv("data.csv")
ids = data["Responder_id"]
langs = data["LanguagesWorkedWith"]
lan_counter = Counter()

for response in langs:
    lan_counter.update(response.split(";"))
#with open('data.csv') as csv_file:
#    csv_reader = csv.DictReader(csv_file)
#    lan_counter = Counter()
#    for row in csv_reader:
#       lan_counter.update(row["LanguagesWorkedWith"].split(";"))
langs=[]
pops=[]
for item in lan_counter.most_common(15):
    langs.append(item[0])
    pops.append(item[1])
langs.reverse()
pops.reverse()

plt.barh(langs, pops)
plt.title("Most poplular languages")
#plt.ylabel("programming languages")
plt.xlabel("number of ppl who use")
plt.tight_layout()
plt.show()

'''ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
x_indexes = np.arange(len(ages_x))
width = 0.25
dev_y=[38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 68748, 73752, 66666]
py_dev_y=[33444, 34567, 23456, 54667, 87764, 22323, 23455, 23233, 44444, 54345, 98798]
plt.bar(x_indexes - width, dev_y, width=width, color="#444444", label="All Devs")
plt.bar(x_indexes , py_dev_y, width= width, color="#008fd5", label="python devs")
plt.legend()
plt.xticks(ticks=x_indexes, labels=ages_x)
plt.title("Median salary (USD) by age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.tight_layout()
plt.show()
'''