import numpy as np
import matplotlib.pyplot as plt
 
# data to plot
n_groups = 8
Linear = (.90, .55, .40, .65, .90, .55, .40, .65)
Sigmoid = (.90, .55, .40, .65, .90, .55, .40, .65)
Poly = (.90, .55, .40, .65, .90, .55, .40, .65)
 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
 
rects1 = plt.bar(index, Linear, 0.2, alpha=0.5, color='b', label='Linear')
rects2 = plt.bar(index + 0.2, Sigmoid, 0.2, alpha=0.5, color='g', label='Sigmoid')
rects3 = plt.bar(index + 0.4, Sigmoid, 0.2, alpha=0.5, color='r', label='Polynomial')
 
plt.xlabel('Training Replays')
plt.ylabel('Accuracy')
plt.xticks(index + 0.2, ['5', '10','15', '20','25', '30','35', '40',])
plt.legend()
 
plt.show()