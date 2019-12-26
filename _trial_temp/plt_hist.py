import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")
ages=[18,19,21,25, 26, 26, 30, 32, 38, 45, 55 ]
bins=[10,20,30,40,50,60]
plt.hist(ages, bins=bins,edgecolor="black",log=True)
plt.title("Ages of responders")
#plt.ylabel("programming languages")
plt.axvline(29, color="green", label='age median', linewidth=2)
plt.legend()
plt.xlabel("ages")
plt.ylabel("total respondents")
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