import matplotlib
import matplotlib.pyplot as plt

entriesLin = []
entriesPol = []
entriesSig = []

X_axis = []
with open('graphData.txt') as file:
	counter = 1
	for line in file:
		entries = line.split()
		if len(entries) == 1:
			X_axis.append(entries[0])
		elif str(entries[0]) == "Linear":
			entriesLin.append(entries[1])

		elif entries[0] == "Poly":
			entriesPol.append(entries[1])

		elif entries[0] == "Sigmoid":
			entriesSig.append(entries[1])
	
plt.ylim([0, 1])
plt.xlim([0,70])
plt.grid(color='r', linestyle='-', linewidth=0.12)


plt.plot(X_axis, entriesLin,'ro', color='blue')
plt.plot(X_axis, entriesPol,'ro',color='red')
plt.plot(X_axis, entriesSig,'ro', color='green')

plt.plot(X_axis, entriesLin, label = "linear", color='blue')
plt.plot(X_axis, entriesPol, label = "polynomial", color='red')
plt.plot(X_axis, entriesSig, label = "sigmoid", color='green')


plt.xlabel('Training Size')
plt.ylabel('Accuracy')
plt.title('Model Accuracy Comparision')

plt.legend(loc = 4)
plt.show()


