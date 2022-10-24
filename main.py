#plt as alias for pyplot for ease of use
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# fig represents  'figure' (entire collection of plots), ax reps singular plots
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# set chart title and label axes
ax.set_title("Squared Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set range for each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()
