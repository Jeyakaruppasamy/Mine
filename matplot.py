import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a plot
plt.plot(x, y, label='Line 1', color='blue', marker='o')

# Add titles and labels
plt.title("Simple Line Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Show legend
plt.legend()

# Show the plot
plt.show()
