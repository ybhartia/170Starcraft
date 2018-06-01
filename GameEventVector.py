import sys
import sc2reader
import numpy


def loadReplay(path):
	return sc2reader.load_replay(path, load_level=4)



# returns 2D array, each row is structured as below
# [time, TargetPointCommandEvent (1 or 0, if happens), TargetUnitCommandEvent(1 or 0, if happens), DataCommandEvent(1 or 0, if happens)]
def get1HotVec(replay):
	rtn = []
	for event in replay.events:
		# ignore CameraEvent and SelectionEvents, only focus on CommandEvents, mainly ability used
		if type(event) != sc2reader.events.game.CameraEvent and type(event) != sc2reader.events.game.SelectionEvent:
			# row vector
			vec = ['', 0, 0, 0]
			# get event time as as string
			vec[0] = event.__str__()[0:5]
			# if command targets a unit
			if type(event) == sc2reader.events.game.TargetUnitCommandEvent:
				# print 'target'
				vec[1] = 1
			# if command targets a point on the map/screen
			if type(event) == sc2reader.events.game.TargetPointCommandEvent:
				# print 'aoe'
				vec[2] = 1
			# if command doesn't require a target
			if type(event) == sc2reader.events.game.DataCommandEvent:
				# print 'passive'
				vec[3] = 1
			rtn.append(vec)
	return rtn






# replay = loadReplay('/home/hqmai/sc2reader/test_replays/2.0.0.23925/Akilon Wastes.SC2Replay')
replay = loadReplay('Lunar Colony V.SC2Replay')
print get1HotVec(replay)




