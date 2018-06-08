# StarCraft 2 Commentator Bot

## Manual

	python trueMaster.py path/to/replay/replay.SC2Replay

Where path `path/to/replay/replay.SC2Replay` is the replay including path to the replay. It can be an absolute or relative path.

## Requirement

Python 2.7

### SC2Reader

We use SC2Reader to process the replays.
SC2Reader can be downloaded, as well as the instructions on how to use it can be found [here](https://github.com/GraylinKim/sc2reader).

SC2 Reader is a python module that can be used to process a StarCraft 2 replay. the replay object returns from calling `sc2reader.load_replay('MyReplay.SC2Replay', load_level=4)` contains information about the replays such as the player's user names, factions, ... as well as differents events that the players make in game and tracker events such as a unit dying.