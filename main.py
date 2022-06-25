import os
import pandas as pd
import matplotlib.pyplot as plt

# Getting terminal size and adding divider for any screen.
sp = "-" * os.get_terminal_size().columns

# Reading CSV file.
df = pd.read_csv("gravity.csv")

# Printing divider and Data Frame.
print("\nData Of Gravity Of Stars", sp)
print(df.head())
print(sp, "\n")

# Collecting the Data.
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()
gravity = df["Gravity"].to_list()

# Slotting the Data.
mass.sort()
radius.sort()
gravity.sort()

print("\n1st Plot -> 'Mass and Radius of Stars' -> Plotted !\n")

# Plotting 1st plot.
plt.title("Mass and Radius of Stars")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.plot(radius, mass)
plt.show()

print("\n2nd Plot -> 'Mass and Gravity of Stars' -> Plotted !\n")

# Plotting 2nd plot.
plt.title("Mass and Gravity of Stars")
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.plot(mass, gravity)
plt.show()

# Printing the result .
print("1st and 2nd Plot -> Plotted !\n")
