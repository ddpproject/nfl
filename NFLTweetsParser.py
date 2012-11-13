import sys
import ujson
from bs4 import BeautifulSoup

def parse_tweets_page(filename):
	soup = BeautifulSoup(open(filename),"lxml")
	tweets = []
	name = soup.find("h1",class_="name").string.encode("ascii","ignore")
	profile_image = soup.find("div",class_="profile_image").a.img['src']

	tweet_set = set()
	for twt in soup.find_all("div",class_="status_content"):
		timeago = twt.find("abbr",class_="timeago")
		tweet_url = timeago.parent["href"]
		timeago = timeago.string.encode("ascii","ignore")
		tweet = twt.find("div",class_="text")
		tweet.div.extract()
		tweet.strong.extract()
		tweet_text = ' '.join([text.encode("ascii","ignore") for text in tweet.stripped_strings])

		if tweet_text not in tweet_set:
			tweet_set.add(tweet_text)
			tweets.append({
				"Name": name,
				"profile_image": profile_image,
				"tweet_url": tweet_url,
				"Tweet": tweet_text,
				"Timeago": timeago
			})
	return tweets

def write_tweets_to_file(tweets, file=None):
    if not file:
        file = open(tweets[0]["Name"] + " tweets.json", "w")
    for tweet in tweets:
    	file.write(ujson.dumps(tweet) + "\n")

if __name__ == '__main__':
    filename = sys.argv[1]
    if filename:
        tweets = parse_tweets_page(filename)
        write_tweets_to_file(tweets)
    else:
        print "Usage: python NFLTweetsParser.py playertweets.html"