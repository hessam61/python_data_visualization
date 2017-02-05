import matplotlib.pyplot as plt
x_values = list(range(1, 20)) 
y_values = [x**2 for x in x_values]


plt.scatter(x_values, y_values, c='red', edgecolor='none', s=20)
# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set the range for each axis. 
plt.axis([0, 20, 0, 400])
plt.show()