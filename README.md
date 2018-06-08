# StarCraft 2 Commentator Bot

## Manual

Download or clone the project [here](https://github.com/ybhartia/170Starcraft).

Use the following command to run the project:

	python trueMaster.py path/to/replay/replay.SC2Replay

Where path `path/to/replay/replay.SC2Replay` is the replay including path to the replay. It can be an absolute or relative path.

Some replays are provided

Use `sudo pip install` for any modules that requires by `trueMaster.py` or any missing modules.

### Other Modules

#### SC2Reader

We use SC2Reader to process the replays.
SC2Reader can be downloaded, as well as the instructions on how to use it can be found [here](https://github.com/GraylinKim/sc2reader).

SC2 Reader is a python module that can be used to process a StarCraft 2 replay. the replay object returns from calling `sc2reader.load_replay('MyReplay.SC2Replay', load_level=4)` contains information about the replays such as the player's user names, factions, ... as well as differents events that the players make in game and tracker events such as a unit dying.

## Requirement

Python 2.7

## Replays

All StarCraft replays should work for upto the current patch (4.3.2). Replays in future patch should work if Blizzard does not make major changes to replays files.

Some replays are included in the project, in `workingReplays` folder. Use:

	python trueMaster.py workingReplays/AIvsAlGhadouriTvP.SC2Replay

To run one of the replay in this file.

## Output Description

Output is in the form:

	******* BASIC PRINTS ********
	This section contains the AI commentator's messages, describing the events that currently happen in the game (includes the timestamp of the event).It shows the last 5 comments on game events.
	******* AI PRINTS ********  05:00 (This is the current timestamp)   *******
	This section contains the commentator's messages regarding the general state of the game (includes the timestamp of the event), which player is in favor. This shows up to 5 previous comments.
	*********************************************	
	This section animate the current message (printing out the message letter by letter as if the AI is typing it)

The outputs starts with an introduction line as shown below:

	******* BASIC PRINTS ********
	Hey everyone and welcome to my live commentatory of the best game ever. My name is AI and yes I am very intelligent
	It's gonna be an interesting match with 1 human on Team 1 against 1 human on Team 2!
	We're gonna see AlGhadouri VS A.I. 1 (Hard)!
	******* AI PRINTS ********  00:11  *******

	*********************************************

Then thi is an example of the output afterward:

	******* BASIC PRINTS ********
	09:18 - What will AlGhadouri do with 2 new Probes?
	09:19 - TerranInfantryWeaponsLevel1 upgrade completed for A.I..
	09:20 - What will A.I. do with that new MULE?
	09:20 - The production of 15 Probes is completed for AlGhadouri.
	09:47 - What will AlGhadouri do with 10 new Immortals?
	******* AI PRINTS ********  10:13  *******
	06:02  It's looking really bleak for A.I. 1 (Hard). [Team 1: 5 Team 2: 0 ]
	06:56  At this rate, AlGhadouri will win pretty soon against A.I. 1 (Hard)! [Team 1: 6 Team 2: 1 ]
	08:00  At this rate, AlGhadouri will win pretty soon against A.I. 1 (Hard)! [Team 1: 7 Team 2: 2 ]
	09:18  A.I. 1 (Hard) is getting dominated by AlGhadouri! [Team 1: 8 Team 2: 2 ]
	10:10  A.I. 1 (Hard) is getting dominated by AlGhadouri! [Team 1: 9 Team 2: 2 ]
	*********************************************
	 
	10:10 - A.I. has upgraded SiegeTank

