from matplotlib import pyplot as plt
import pandas as pd

plt.style.use("seaborn")
data = pd.read_csv("data2.csv")
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']
plt.scatter(view_count, likes, c=ratio, cmap='summer',edgecolors='black', linewidth=1, alpha=0.75)
cbar=plt.colorbar()
cbar.set_label("like/dislike ratio")
plt.xscale("log")
plt.yscale("log")
'''x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]
colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]
sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
          538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]
plt.scatter(x,y, s=sizes, c=colors, edgecolor='black',cmap='Greens', linewidth=1, alpha=0.75)
'''
plt.tight_layout()
plt.show()