import matplotlib.pyplot as plt

input_values = [1,2,3,4,5,6]
numbers = [1,5,3,7,10,2]
plt.plot(input_values, numbers, linewidth=3)

#set title and label 
plt.title("Simple Line", fontsize=16)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Number", fontsize=12)
#set size of tick labels
plt.tick_params(axis='both', labelsize=8)

plt.show()	