from NFLStatsParser import parse_stats_page, write_player_to_file
import os
import sys

def main(dir):
    statsfile = open("player_stats.json", "w")
    os.chdir(dir)
    for playerfile in os.listdir("."):
        if playerfile.endswith("careerstats.html"):
            write_player_to_file(parse_stats_page(playerfile), statsfile)
    statsfile.close()

if __name__ == '__main__':
    dir = sys.argv[1]
    if dir:
        main(dir)
    else:
        print "Usage: python NFLStats.py ./Crawls/Complete Player Pages"