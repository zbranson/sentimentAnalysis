Project 1 README
Zac Branson

For the first project I decided to write a simple, rule-based sentiment classifier using Python.  Although I have previously used implementations of more complex classifiers, I was not ready to implement them myself.
Pre-processing:
I pre-processed the positive and negative wordlists to remove underscores and hypens, although it's not clear that this improved performance of my classifer.  I couldn't think of a (computationally) simple way to search for sequences of words in a string, I simply treated each word of multi-word expressions as individual expressions.
I also pre-processed the tweets by changing uppercase letters to lowercase letters, and splitting strings by all non-alphabet characters using a regular expression.  I could have just as easily removed them for the current application, but keeping them in doesn't affect the score (because the wordlists don't include punctuation), and they may be useful in future versions of this project.
The classifer:
The classifer turns each tweet into a list of words, then checks the sets of positive words and negative words.  If a word in the tweet is in the postive set, the score is incremented by 1, if a word in the tweet is in the negative set, the score is decremented by 1.  I turned the wordlists into sets for two reasons: 1) sets are implemented as hash tables in Python, so they have a lookup time of O(1).  2) there are unlikely to be duplicates in the list, and duplicates would be undesirable anyway, because they would artificially change the score by double counting certain words.  
I tried removing stopwords from the wordlists because some of the multi-word expressions contained prepositions but it caused performance to tank severely so I commented that out.  I'm not sure if this is a random occurance, or if the NLTK stopword list was too broad.
Output:
The script contains an output file to which it writes newline seperated tuples of (original tweet, classifier score) for future reference.  It also prints to screen the number of tweets identified as positive, negative, and zero for both positive and negative tweet sets, and also prints out the simple accuracy (classified pos/total pos, classifed neg/total neg) for each set of tweets.  
Technical:
The filenames are hard-coded so both the wordlists and the tweet files must be in the same directory as the script.  The script is written in Python3 (although I think it runs in Python2 as well).  The script is executable.



