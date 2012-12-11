import collections
# import math
# import operator
# import heapq
import random
# import time
import ujson

POS_EMOTICONS = ">:] :-) :) :o) :] :c) :> =] =) :} :^)" + " ;)"
POS_WORDS = "lol love haha" + " amused awed bouncy chipper contemplative content determined dignified dreamy empowered energetic enlightened enthralled flirty giddy grateful harmonious hyper idyllic joyous jubilant liberating light-hearted loving mellow peaceful pleased refreshed rejuvenated relieved satiated satisfied  surprised thankful thoughtful touched trustful vivacious warm welcoming admiring adoring affectionate hilarious hopeful humorous appreciative approving bemused benevolent blithe calm casual celebratory cheerful comforting comic compassionate complimentary conciliatory confident contented delightful earnest ebullient ecstatic effusive elated empathetic encouraging euphoric excited exhilarated expectant facetious fervent flippant forthright friendly funny gleeful gushy happy interested introspective jovial joyful laudatory light lively mirthful modest nostalgic optimistic passionate placid playful poignant proud reassuring reflective relaxed respectful reverent romantic sanguine scholarly self-assured sentimental serene silly sprightly straightforward sympathetic tender tranquil whimsical wistful worshipful zealous"
NEG_EMOTICONS = ">:[ :-( :( :-c :c :-< :< :-[ :[ :{ :-|| :'-( :'( :'-) :')"
NEG_WORDS = "abhorring acerbic ambiguous hostile impatient incredulous ambivalent angry annoyed antagonistic anxious apathetic apprehensive belligerent bewildered biting bitter blunt bossy cold conceited condescending confused contemptuous curt cynical demanding depressed derisive derogatory desolate despairing desperate detached diabolic disappointed disliking disrespectful doubtful embarrassed enraged evasive fatalistic fearful forceful foreboding frantic frightened frustrated furious gloomy grave greedy grim harsh haughty holier-than-thou hopeless indifferent indignant inflammatory insecure insolent irreverent lethargic melancholy mischievous miserable mocking mournful nervous ominous outraged paranoid pathetic patronizing pedantic pensive pessimistic pretentious psychotic resigned reticent sarcastic sardonic scornful self-deprecating selfish serious severe sinister skeptical sly solemn somber stern stolid stressful strident suspicious tense threatening tragic uncertain uneasy unfriendly unsympathetic upset violent wry aggravated barren brooding confining cranky crushed discontented distressed drained dreary envious exhausted futile grumpy haunting heartbroken infuriated insidious intimidated irate irritated jealous lonely melancholic merciless moody morose nauseated nightmarish numb overwhelmed painful predatory rejected restless scared sick stressed suspenseful terrifying uncomfortable vengeful worried"

def filter_classes(tweets):
    """
    purpose: return of dict of positive and negative tweets
    parameters: tweets is an iterator of tweet dictionaries
    returns: a dictionary mapping class names (like "positive" or
             "negative") to a list of tweets in that class.

    This method removes tweets with no recognized emoticon or with emoticons
    from two different classes.
    """
    emoticons = dict(
        positive = POS_EMOTICONS.split() + POS_EMOTICONS[::-1].replace(')','(')
            .replace('>','<').replace(']','[').split() + POS_WORDS.split(),
        negative = NEG_EMOTICONS.split() + NEG_EMOTICONS[::-1].replace(')','(')
            .replace('(',')').replace('<','>').replace('[',']').replace('{','}')
            .split() + NEG_WORDS.split()
    )
    filtered = collections.defaultdict(list)
    for tweet in tweets:
        tweet_class = None
        # sometimes html gets into the emoticons
        text = tweet['Text'].replace('&lt;','<').replace('&gt;','>').lower()
        for clas,smilies in emoticons.iteritems():
            if any(smily in text for smily in smilies):
                if tweet_class:
                    # ignore tweets that fit in two classes
                    continue
                tweet_class = clas
        if tweet_class:
            filtered[tweet_class].append(tweet)

    smallest_class_size = min(len(tw) for tw in filtered.itervalues())
    for clas,tweets in filtered.iteritems():
        filtered[clas] = random.sample(tweets,smallest_class_size)
    return filtered

def read_tweets(tweetsfile):
    tweets = open(tweetsfile, "r")
    for line in tweets:
        yield ujson.loads(line)

if __name__ == '__main__':
    filtered = filter_classes(read_tweets("./data/player_tweets.json"))
    print "num pos:", len(filtered["positive"]) # 60065
    print "num neg:", len(filtered["negative"]) # 10574
    pos = open("./data/pos_tweets.json", "w")
    for tweet in filtered["positive"]:
        pos.write(ujson.dumps(tweet) + "\n")
    neg = open("./data/neg_tweets.json", "w")
    for tweet in filtered["negative"]:
        neg.write(ujson.dumps(tweet) + "\n")
