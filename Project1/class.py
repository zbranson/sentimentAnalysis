#!/usr/bin/python3

import string, os, operator, re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


#for lemmatizing tweets
wordnet_lemmatizer = WordNetLemmatizer()

# gets 2D list of positive words from file, removes underscores, hypens, and newlines
pos_words = []
with open('./pos.wn','r',encoding='utf-8', errors='ignore') as pos:
    lines = pos.readlines()
    for line in lines:
        line = line.replace('\n', '')
        line = re.split('[^a-z]',line)
        for word in line:
            #had to remove stopwords because I split multi-word expressions
            #if word not in stopwords.words('english'):
            #removing stopwords negatively effected performance for some reason
            pos_words.append(word) 

# gets 2D list of negative words from file, removes underscores, hypens, and   newlines
neg_words = []
with open('./neg.wn','r',encoding='utf-8', errors='ignore') as neg:
    lines = neg.readlines()
    for line in lines:
        line = line.replace('\n', '')
        line = re.split('[^a-z]',line)
        for word in line:
            #had to remove stopwords because I split multi-word expressions
            #if word not in stopwords.words('english'):
            #removing stopwords negatively effected performance for some reason
            neg_words.append(word) 

#takes in tweet as string and returns integer score
def get_score(tweet):
    score = 0
    tweet = tweet.lower()
    tweet = re.split('[^a-z]',tweet)
    #using a list instead of a set results in a slightly higher accuracy
    #for negative tweets but slows things down quite a bit O(n) vs O(1) lookup
    #tweet = set(tweet)
    for word in tweet:
	#lemmatizing results in a slight increase in accuracy of a few
	# thousandths of a percent but it also takes a lot longer
        word = wordnet_lemmatizer.lemmatize(word)
        if word in set(pos_words):
            score +=1
        if word in set(neg_words):
            score -=1
    return score

#calculates scores for each tweet
#writes tuple of tweet and score to file
#prints number of (in)correctly identified tweets and simple accuracy
files = ['posTweets.txt','negTweets.txt']
for fi in files:
    with open(fi,'r',encoding='utf-8', errors='ignore') as ptweets, open(fi+'.scored','w') as out:
        tweets = ptweets.readlines()
        tot = 0
        pos = 0
        neg = 0
        zero = 0
        for tweet in tweets:
            tot +=1
            score = get_score(tweet)
            if score > 0:
                pos +=1
            elif score < 0:
                neg +=1
            else: zero +=1
            tup = (tweet, score)
            out.write(str(tup)+'\n')
        if fi == "posTweets.txt":
            print("Results for positive tweets: ")
        else: print("Results for negative tweets: ")
        print(str(pos)+' out of '+str(tot)+' identified as positive.')
        print(str(neg)+' out of '+str(tot)+' identified as negative.')
        print(str(zero)+' out of '+str(tot)+' have zero score.')
        if fi == "posTweets.txt":
            print('Simple Accuracy: '+str(pos/tot))
        else: print('Simple Accuracy: '+str(neg/tot))
        
