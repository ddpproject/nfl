from NFLTweetsParser import parse_tweets_page, write_tweets_to_file
import os
import sys
import ujson

def main(dir):
    if not os.path.exists("./data"):
        os.makedirs("./data")
    tweetsfile = open("./data/player_tweets.json", "w")

    curplayers = set()
    try:
        with open("./data/player_stats.json", "r") as statsfile:
            for line in statsfile:
                player = ujson.loads(line)
                curplayers.add(player["Name"])
        curfile = open("./data/cur_player_tweets.json", "w")
    except IOError:
        pass
    
    os.chdir(dir)
    for playerfile in os.listdir("."):
        if playerfile.startswith("indexcfmCatID0AthleteID"):
            tweets = parse_tweets_page(playerfile)
            write_tweets_to_file(tweets, tweetsfile)
            if tweets[0]["Name"] in curplayers:
                write_tweets_to_file(tweets, curfile)
    tweetsfile.close()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        dir = sys.argv[1]
    else:
        dir = "./Crawls/Complete Tweet Crawl"
    if dir:
        main(dir)
    else:
        print "Usage: python NFLTweets.py ./Crawls/Complete Tweet Crawl"