from NFLTweetsParser import parse_tweets_page, write_tweets_to_file
import os
import sys

def main(dir):
    tweetsfile = open("player_tweets.json", "w")
    os.chdir(dir)
    for playerfile in os.listdir("."):
        if playerfile.startswith("indexcfmCatID0AthleteID"):
            write_tweets_to_file(parse_tweets_page(playerfile), tweetsfile)
    tweetsfile.close()

if __name__ == '__main__':
    dir = sys.argv[1]
    if dir:
        main(dir)
    else:
        print "Usage: python NFLTweets.py ./Crawls/medium crawl Adam Snyder tweets"