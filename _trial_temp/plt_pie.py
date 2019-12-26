from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")
slices=[40, 30, 20, 10]
labels=["A", "b", "c", "d" ]
explode=[0, 0, 0.2, 0]

plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=90, autopct="%1.1f%%", wedgeprops={'edgecolor':'black'})

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()