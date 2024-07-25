import numpy as np
import matplotlib.pyplot as plt

colors = [
    "Blue",
    "Blue",
    "Blue",
    "pink",
    "Blue",
    "pink",
    "blue",
    "green",
    "blue",
    "PINK",
    "Baby blue",
    "Red",
    "Green",
    "green",
    "Purple",
    "Blue",
    "Pink",
    "Pink",
]

numbers = np.array([
    11,
    33,
    3,
    20,
    7,
    2,
    3,
    8,
    21,
    10,
    2,
    7,
    5,
    11,
    15,
    5,
    7,
    1,
])

sibs = np.array([
    6,
    1,
    2,
    2,
    1,
    4,
    1,
    1,
    1,
    2,
    5,
    2,
    0,
    1,
    1,
    2,
    2,
    3,
])

heights = [
    60,
    62,
    63,
    68,
    71,
    62,
    61,
    64,
    60,
    68,
    65.5,
    65,
    66,
    61,
    73,
    67,
    66,
    66,
]

shoe = [
    7,
    8,
    8,
    9,
    10.5,
    8,
    6,
    9,
    5,
    8.5,
    7.5,
    9,
    10.5,
    7,
    10.5,
    9,
    9,
    9,
]



new_colors = []
for color in colors:
    new_colors.append(color.lower())

plt.hist(new_colors)
plt.title("CSS Favorite Colors!")
plt.show() 

# Create a scatterplot
plt.scatter(sibs, numbers)

# Add titles and labels
plt.title("Siblings vs Fav Nums")
plt.xlabel("sibs")
plt.ylabel("fav nums")

# Show the plot
plt.show()

# Line of best fit:
slope, intercept = np.polyfit(sibs, numbers, 1)
print(slope, intercept)

# Predict y values
numbers_pred = slope * sibs + intercept

# Calculate R² value
ss_res = np.sum((numbers - numbers_pred) ** 2)
ss_tot = np.sum((numbers - np.mean(numbers)) ** 2)
r2 = 1 - (ss_res / ss_tot)

print(f"R² value: {r2:.2f}")