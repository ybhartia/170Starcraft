import matplotlib
import matplotlib.pyplot as plt

entries = []
X_axis = []
with open('graphData.txt') as file:
    counter = 1
    for line in file:
        entries.append(float(line.split()[1]))
        X_axis.append(int(counter))
        counter = counter + 1

print entries, X_axis

plt.plot(X_axis, entries, label = "linear")
plt.legend()
plt.show()


