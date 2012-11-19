import ujson
import fileinput
import operator
import re
import pymongo
import utils
import time
from collections import defaultdict

from settings import settings

def main():
    db = utils.connect_db('nfl', remove_existing=False)
    stats = utils.read_json()
    
    #player stat collection
    player_collection = db['players']
    
    count = 0
    for stat in stats:
        stat['id']=count
        print 'Inserting player:', stat['Name']
        player_collection.insert(stat)
    
    
    player_collection.ensure_index([('id',pymongo.ASCENDING), 
                                        ('Name', pymongo.ASCENDING), 
                                        ('Team', pymongo.ASCENDING),
                                        ('Position', pymongo.ASCENDING)
                                        ])
        
if __name__=="__main__":
    print 'Starting player index'
    start_time = time.time()
    main()
    end_time = time.time()
    print 'done with indexing after %.3f seconds'%(end_time-start_time)
    