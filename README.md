Our project is split into two parts, this part focuses on the stats portion.

------------***** finish *****----------
filename.py
crawler

players stats are gathered
once we have the data, it is stored in a .json file

_________________________________________________

### nflindexer.py
Takes input json file and stores each player and his stats and info into mongodb
each player is assigned a auto_increment id separate from the default id

- requires mongo and json input file. also needs utils.py and settings.py

ex. `python nflindexer.py file.json`

### playerRanker.py
Takes info from mongodb built from nflindexer.py and assigns each player a value based on stats. 

This value is deduced from a custom built algorithm specific to each positions that multiplies each stat by a factor and adds it all together. This value is added to each player's info and every player will be put into a new database based on position. Currently at the end of each build method there is a function that prints everything in the database in decending order starting with the highest ranked player of that position. This is for demonstration only and will be altered later.

- requires nflindexer.py to be run first and to keep the mongodb constant
