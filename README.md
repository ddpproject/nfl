## NFL Player Stats
### Files:

`NFLStatsParser.py` - Parser for html page of NFL player's stats

* Usage: `NFLStatsParser.py von-miller-stats.html`

`NFLStats.py` - Parses every player's NFL stats page and produces a `player_stats.json` file with each player's stats

* Usage: `NFLStats.py ./Crawls/Complete Player Pages`

`DataAnalysis.py` - Outputs the number of players for each position using the data in `player_stats.json`

* Usage: `DataAnalysis.py`

`nflindexer.py` - Puts each player's stats from `player_stats.json` into [mongodb](http://www.mongodb.org/)

* Usage: `nflindexer.py player_stats.json`

`playerRanker.py` - Calculates a score for each player based on their stats in the mongodb

* Usage: `playerRanker.py`

* This value is deduced from a custom built algorithm specific to each positions that multiplies each stat by a factor and adds it all together. This value is added to each player's info and every player will be put into a new database based on position. Currently at the end of each build method there is a function that prints everything in the database in decending order starting with the highest ranked player of that position. This is for demonstration only and will be altered later.

## NFL Player Tweets
### Files:

`NFLTweetsParser.py` - Parser for html page of NFL player's tweets

`NFLTweets.py` - Parses every (current and retired) player's tweets pages and produces a `cur_player_tweets.json` file for current player's tweets and a `player_tweets.json` for every (current and retired) player's tweets

## Server
Requires: [node.js](http://nodejs.org/)

``` bash
cd node-server
npm install    # install dependencies
node serve.js  # run webserver on http://localhost:8000/
```