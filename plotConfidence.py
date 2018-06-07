import numpy as np
import matplotlib.pyplot as plt
 

year = [5,10,15,20,25,30,35,40,45,50,55,60,65,70]
gg_confidence = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
our_confidence = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
year = range(0,len(gg_confidence))

# workingReplays/ggtracker_95895.SC2Replay
# [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]


# fig, ax = plt.subplots()

plt.ylim([-1,3])
plt.xlim([0,15])

plt.grid(color='r', linestyle='-', linewidth=0.12)

plt.plot(year, gg_confidence, 'ro',color='g')
plt.plot(year, gg_confidence, color='g', label='gg_Replays\' Confidence')

plt.plot(year, our_confidence, 'ro',color='orange')
plt.plot(year, our_confidence, color='orange',label='Our Commenter\'s Confidence')

plt.xlabel('Timestamp')
plt.ylabel('Winning Status')
plt.title('ggtracker_95895.SC2Replay')


plt.legend(loc=4)
plt.show()