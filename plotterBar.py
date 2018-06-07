import numpy as np
import matplotlib.pyplot as plt
 
# data to plot
n_groups = 14
More = ( 3,9,10,18,16,17,24,26,32,27,28,32,35,40)
Less = ( 5-3,10-9,15-10,20-18,25-16,30-17,35-24,40-26,45-32,50-27,55-28,60-32,65-35,70-40)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
 
rects1 = plt.bar(index, More, 0.2, alpha=0.5, color='g', label='Wins with More Larvae')
rects2 = plt.bar(index + 0.2, Less, 0.2, alpha=0.5, color='r', label='Wins with Fewer Larvae')
plt.axis('tight')
# plt.xlim([0, 50]).tight

plt.xlabel('Training Replays')
plt.ylabel('Wins')
plt.title('Win Status Depending on Larvae Built')
plt.xticks(index + 0.2,[5,10,15,20,25,30,35,40,45,50,55,60,65,70])
plt.legend(loc = 0)
 
plt.show()

