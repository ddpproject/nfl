from crawler.crawler import Crawler
import time
#mycrawler = Crawler()
#seeds = ['http://www.example.com/'] # list of url
#mycrawler.add_seeds(seeds)
#rules = {'^(http://.+example\.com)(.+)$':[ '^(http://.+example\.com)(.+)$' ]}
#your crawling rules: a dictionary type, 
#key is the regular expressions for url, 
#value is the list of regular expressions for urls which you want to follow from the url in key.
#mycrawler.add_rules(rules)
#mycrawler.start() # start crawling

def main():
    nflcrawler = Crawler()
    seeds = [
        'http://www.nfl.com/teams/roster?team=STL',
        'http://www.nfl.com/teams/roster?team=TEN',
        'http://www.nfl.com/teams/roster?team=WAS',
        'http://www.nfl.com/teams/roster?team=CAR',
        'http://www.nfl.com/teams/roster?team=CLE',
        'http://www.nfl.com/teams/roster?team=JAC',
        'http://www.nfl.com/teams/roster?team=KC'
    ]
    
    nflcrawler.add_seeds(seeds)
    
    rules = {'^(http://www.nfl.com/teams/roster)(\?team=[a-zA-Z]+)$':[ '^(http://www.nfl\.com/player/)([a-zA-Z]+/[0-9]+/profile)$' ],
            '^(http://www.nfl\.com/player/)([a-zA-Z]+/[0-9]+/profile)$' : ['^(http://www.nfl\.com/player/)([a-zA-Z]+/[0-9]+/careerstats)$']
    }
    
    nflcrawler.add_rules(rules)
    nflcrawler.start()



if __name__=="__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print 'done with crawling after %.3f seconds'%(end_time-start_time)
    
    """
        seeds = ['http://www.nfl.com/teams/roster?team=DEN', 'http://www.nfl.com/teams/roster?team=ATL']
    nflcrawler.add_seeds(seeds)
    
    rules = {'^http://www.nfl.com/teams/roster?team=[a-zA-Z]+$':[ '^http://www.nfl\.com/player/[a-zA-Z]+/[0-9]+/profile$' ],
            '^http://www.nfl\.com/player/[a-zA-Z]+/[0-9]+/profile$' : ['^http://www.nfl\.com/player/[a-zA-Z]+/[0-9]+/careerstats$']
    }
    
        'http://www.nfl.com/teams/roster?team=ATL', 
        'http://www.nfl.com/teams/roster?team=CHI',
        'http://www.nfl.com/teams/roster?team=HOU',
        'http://www.nfl.com/teams/roster?team=BAL',
        'http://www.nfl.com/teams/roster?team=SF',
        'http://www.nfl.com/teams/roster?team=GB',
        'http://www.nfl.com/teams/roster?team=NYG',
        'http://www.nfl.com/teams/roster?team=DEN',
        'http://www.nfl.com/teams/roster?team=IND',
        'http://www.nfl.com/teams/roster?team=NE',
        'http://www.nfl.com/teams/roster?team=PIT',
        'http://www.nfl.com/teams/roster?team=MIN',
        'http://www.nfl.com/teams/roster?team=SEA',
        'http://www.nfl.com/teams/roster?team=DET',
        'http://www.nfl.com/teams/roster?team=MIA',
        'http://www.nfl.com/teams/roster?team=SD',
        'http://www.nfl.com/teams/roster?team=TB',
        'http://www.nfl.com/teams/roster?team=ARI',
        'http://www.nfl.com/teams/roster?team=BUF',
        'http://www.nfl.com/teams/roster?team=CIN',
        'http://www.nfl.com/teams/roster?team=DAL',
        'http://www.nfl.com/teams/roster?team=NO',
        'http://www.nfl.com/teams/roster?team=NYJ',
        'http://www.nfl.com/teams/roster?team=OAK',
        'http://www.nfl.com/teams/roster?team=PHI',
        'http://www.nfl.com/teams/roster?team=STL',
        'http://www.nfl.com/teams/roster?team=TEN',
        'http://www.nfl.com/teams/roster?team=WAS',
        'http://www.nfl.com/teams/roster?team=CAR',
        'http://www.nfl.com/teams/roster?team=CLE',
        'http://www.nfl.com/teams/roster?team=JAC',
        'http://www.nfl.com/teams/roster?team=KC'
    
    
    
    """
    #http://www.nfl.com/player/vonmiller/2495202/profile
    #http://www.nfl.com/player/vonmiller/2495202/careerstats
    #15840.372 seconds