## NFL Player Stats
### Files:

`NFLStatsParser.py` - Parser for html page of NFL player's stats

* Usage: `python NFLStatsParser.py von-miller-stats.html`

`NFLStats.py` - Parses every player's NFL stats page and produces a `player_stats.json` file with each player's stats

* Usage: `python NFLStats.py ./Crawls/Complete Player Pages`

`DataAnalysis.py` - Outputs the number of players for each position using the data in `player_stats.json`

* Usage: `python DataAnalysis.py`

`nflindexer.py` - Puts each player's stats from `player_stats.json` into [mongodb](http://www.mongodb.org/)

* Usage: `python nflindexer.py player_stats.json`

`playerRanker.py` - Computes a score for each player based on their stats in the mongodb

* Usage: `python playerRanker.py`

## NFL Player Tweets
### Files:

`NFLTweetsParser.py` - Parser for html page of NFL player's tweets

* Usage: `python NFLTweetsParser.py playertweets.html`

`NFLTweets.py` - Parses every (current and retired) player's tweets pages and produces a `cur_player_tweets.json` file for current player's tweets and a `player_tweets.json` for every (current and retired) player's tweets

* Usage: `python NFLTweets.py ./Crawls/Complete Tweet Crawl`

`happinessAnalyzer.py` - Filters tweets into training set for knn based on emoticons and strong sentiment words

* Usage: `python happinessAnalyzer.py`

`knn.py` - Classifies tweets from `cur_player_tweets.json` as positive or negative using knn classification

* Usage: `python knn.py`

## Server
Requires: [node.js](http://nodejs.org/)

``` bash
cd node-server
npm install    # install dependencies
node serve.js  # run webserver on http://localhost:8000/
```
