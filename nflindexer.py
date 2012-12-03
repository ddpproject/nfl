import ujson
import fileinput
import operator
import re
import pymongo
import utils
import time
from collections import defaultdict

# from settings import settings

def main():
    db = utils.connect_db('nfl', remove_existing=True)
    stats = read_json('./data/player_stats.json')
    
    #player stat collection
    player_collection = db['players']
    player_collection.ensure_index([('id',pymongo.ASCENDING), 
                                    ('Name', pymongo.ASCENDING), 
                                    ('Team', pymongo.ASCENDING),
                                    ('Position', pymongo.ASCENDING)
                                    ])

    count = 0
    for stat in stats:
        stat['id']=count
        count += 1
        print 'Inserting player:', stat['Name']
        player_collection.insert(stat)



    tweets = read_json('./data/player_sentiment.json')
    tweets_collection = db['tweets']
    tweets_collection.ensure_index([('Name', pymongo.ASCENDING)])

    happiness = defaultdict(int)
    sadness = defaultdict(int)
    for tweet in tweets:
        if tweet['sentiment'] == 'positive':
            happiness[tweet['Name']] += 1
        else:
            sadness[tweet['Name']] += 1
        tweets_collection.insert(tweet)

    for player in happiness:
        print player_collection.update({"Name":player},{'$set': {"num_pos": happiness[player]}})
    for player in sadness:
        print player_collection.update({"Name":player},{'$set': {"num_neg": sadness[player]}})


def read_json(file):
    json = open(file, "r")
    for line in json:
        yield ujson.loads(line)


if __name__=="__main__":
    print 'Starting player index'
    start_time = time.time()
    main()
    end_time = time.time()
    print 'done with indexing after %.3f seconds'%(end_time-start_time)
    
