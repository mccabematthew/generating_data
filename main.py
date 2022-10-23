# plt as alias for pyplot for ease of use
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# fig represents  'figure' (entire collection of plots), ax reps singular plots
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# set chart title and label axes
ax.set_title("Squared Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', labelsize=14)

plt.show()


