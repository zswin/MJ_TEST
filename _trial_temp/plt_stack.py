from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")
minutes=[1,2,3,4]
player1=[1,3,0,2]
player2=[5,3,7,1]
player3=[2,2,1,5]
labels=["player1", "player2", "player3"]
colors=["red", "green", "purple"]
plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)
plt.legend(loc=(0.05,0.04))
plt.title("My Awesome Stack Chart")
plt.tight_layout()
plt.show()
#comment