import matplotlib.pyplot as plt
import numpy as np
# Generate x values from 0 to 10
x = np.linspace(0, 10, 100)
# Define y as a function of x (say y = 2x + 1)
y = 2 * x + 1
# Plot the line
plt.plot(x, y, label="y = 2x + 1", color='blue')
# Add labels and title
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Line Plot Example sidhartha")
# Show legend
plt.legend()
# Display the plot
plt.show()
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y1 = x          # Line 1: y = x
y2 = x**2       # Line 2: y = x^2
y3 = np.sqrt(x) # Line 3: y = √x
plt.plot(x, y1, label="y = x", color='blue')
plt.plot(x, y2, label="y = x²", color='red')
plt.plot(x, y3, label="y = √x", color='green')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Multiple Lines on Same Plot sidhartha")
plt.legend()
plt.show()
import matplotlib.pyplot as plt
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.bar(languages, popularity, color=['blue', 'green', 'red', 'purple', 'orange', 'cyan'])
plt.xlabel("Programming Languages")
plt.ylabel("Popularity (%)")
plt.title("Popularity of Programming Languages sidhartha")
plt.show()
