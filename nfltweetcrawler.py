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
    nfltweetcrawler = Crawler()
    seeds = ['http://www.tweeting-athletes.com/index.cfm?CatID=2&People=1']
    
    nfltweetcrawler.add_seeds(seeds)
    
    rules = {'^(http://www.tweeting-athletes.com/)(index.cfm\?CatID=2&People=1)$': ['^(http://www.tweeting-athletes.com/)(index.cfm\?AthleteID=[0-9]+)$'],
    '^(http://www.tweeting-athletes.com/)(index.cfm\?AthleteID=[0-9]+)$':['^(http://www.tweeting-athletes.com/index.cfm)(\?CatID=0&AthleteID=[0-9]+&p=[0-9]+)$'],
    '^(http://www.tweeting-athletes.com/index.cfm)(\?CatID=0&AthleteID=[0-9]+&p=[0-9]+)$': ['^(http://www.tweeting-athletes.com/index.cfm)(\?CatID=0&AthleteID=[0-9]+&p=[0-9]+)$']}
    
    nfltweetcrawler.add_rules(rules)
    nfltweetcrawler.start()



if __name__=="__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print 'done with crawling after %.3f seconds'%(end_time-start_time)
   
    #http://www.tweeting-athletes.com/index.cfm?CatID=2&People=1 main page
    
   #http://www.tweeting-athletes.com/index.cfm?AthleteID=21958 anthony sherman first page
   #done with crawling after 42040.978 seconds

    
    