import ujson
import re
import heapq
import math
from collections import Counter
from operator import itemgetter
from scipy.sparse import lil_matrix
from happinessAnalyzer import read_tweets
from happinessAnalyzer import filter_classes
from stemming import porter2

def tokenize(text):
    """
    Take a string and split it into tokens on word boundaries.

    A token is defined to be one or more alphanumeric characters,
    underscores, or apostrophes.  Remove all other punctuation, whitespace, and
    empty tokens.  Do case-folding to make everything lowercase. This function
    should return a list of the tokens in the input string.
    """
    tokens = re.findall("[\w']+", text.lower())
    return [porter2.stem(token) for token in tokens]

class SentimentAnalyzer(object):
    def __init__(self):
        self.vects = []
        self.vect_class = []

    def train(self, tweets):
        """
        Take a group of tweets, split them into classes, and train on the
        tweets. This method is only called when using the classifer to index
        tweets, and it is not used when evaluating the classifier.
        """
        self.train_on_filtered(filter_classes(tweets))

    def train_on_filtered(self, filtered_tweets):
        """
        purpose: train a knn classifier on labeled tweets.
        parameters:
            filtered_tweets - a dictionary mapping class names to a list of
            tweets in that class
        returns: None
        """
        for label in filtered_tweets:
            for tweet in filtered_tweets[label]:
                vect = dict(Counter(tokenize(tweet["Text"])))
                self.vects.append(vect)
                self.vect_class.append(label)

    
    def classify(self, k, tweet):
        vect = dict(Counter(tokenize(tweet["Text"])))
        vect_dists = [self._dist(vect, n) for n in self.vects]
        knn = heapq.nsmallest(k, enumerate(vect_dists), key=lambda n: n[1])
        # print knn
        num_pos = 0
        num_neg = 0
        for n in knn:
            if self.vect_class[n[0]] == 'positive':
                num_pos += 1
            else: # self.vect_class[n[1]] == 'negative'
                num_neg += 1
        if num_pos > num_neg:
            return 'positive'
        else:
            return 'negative'

    def _dist(self, a, b):
        dist = 0
        keys = set(a.keys() + b.keys())
        for x in keys:
            dist += (a.get(x,0) - b.get(x,0))**2
        return dist**0.5

def main():
    classifier = SentimentAnalyzer()
    classifier.train(read_tweets("./data/player_tweets.json"))
    file = open("./data/player_sentiment.json", "w")
    # sentfile = open("./data/sentiment.txt", "w")
    for tweet in read_tweets("./data/cur_player_tweets.json"):
        sent = classifier.classify(3, tweet)
        tweet['sentiment'] = sent
        file.write(ujson.dumps(tweet) + "\n")
        print sent
        # sentfile.write(sent + "\n")


if __name__ == '__main__':
    main()