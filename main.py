# plt as alias for pyplot for ease of use
import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

# fig represents  'figure' (entire collection of plots), ax reps singular plots
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# set chart title and label axes
ax.set_title("Squared Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
