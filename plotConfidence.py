import numpy as np
import matplotlib.pyplot as plt
 

year = [5,10,15,20,25,30,35,40,45,50,55,60,65,70]
gg_confidence = [0.6,0.62,0.63,0.65,0.73,0.55,0.65,0.72,0.71,0.85,0.81,0.72,0.74,0.75]
our_confidence = [0.8,0.75,0.86,0.94,0.73,0.70,0.81,0.69,0.052,0.60,0.63,0.60,0.59,0.55]


fig, ax = plt.subplots()

plt.ylim([0,1])
plt.xlim([0,70])
plt.grid(color='r', linestyle='-', linewidth=0.12)

plt.plot(year, gg_confidence, 'ro',color='g')
plt.plot(year, gg_confidence, color='g', label='gg_Replays\' Confidence')

plt.plot(year, our_confidence, 'ro',color='orange')
plt.plot(year, our_confidence, color='orange',label='Our Commenter\'s Confidence')

plt.xlabel('Training Size')
plt.ylabel('Normalized Confidence')
plt.title('Confidence in Prediction')


plt.legend(loc=3)
plt.show()