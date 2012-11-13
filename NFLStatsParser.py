import sys
import re
import ujson
from bs4 import BeautifulSoup

def parse_stats_page(filename):
    soup = BeautifulSoup(open(filename),"lxml")

    player = {}
    player["Name"] = soup.find("span",class_="player-name").string.encode("ascii","ignore")
    number = re.split('[^\w#]+' ,soup.find("span",class_="player-number").string.encode("ascii","ignore"))
    player["Number"] = number[0][1:]
    player["Position"] = number[1]
    player["Team:"] = soup.find("p", class_="player-team-links").a.string.encode("ascii","ignore")
    stats_soup = soup.find("div",id="player-stats-wrapper")
    
    if len(stats_soup.find_all("table")) == 0:
        return None

    for table in stats_soup.find_all("table"):
        Pos = table.find("tr", 
            class_="player-table-header").td.div.string.encode("ascii","ignore")
        player[Pos] = {}

        table_key = table.find_all("tr", class_="player-table-key")
        if len(table_key) == 1:
            table_keys = table_key[0].find_all("td")
        else:
            table_keys = table_key[1].find_all("td")
        table_stats = table.find("tbody").find_all("tr")

        for year_stats in table_stats:
            if len(year_stats) == 1:
                continue
            for i, stat in enumerate(year_stats.find_all("td")):
                key = table_keys[i].string.encode("ascii","ignore")
                if key == "Year" and stat.string.encode("ascii","ignore") != "2012":
                    break
                elif key == "Team":
                    player[Pos][key] = stat.a.string.encode("ascii","ignore")
                else:
                    player[Pos][key] = stat.string.encode("ascii","ignore")
        if player[Pos] == {}:
            return None
    return player

def write_player_to_file(player, file=None):
    if player is None:
        return
    if not file:
        file = open(player["Name"] + ".json", "w")
    file.write(ujson.dumps(player) + "\n")

if __name__ == '__main__':
    filename = sys.argv[1]
    if filename:
        player = parse_stats_page(filename)
        write_player_to_file(player)
    else:
        print "Usage: python NFLStatsParser.py nflplayer.html"