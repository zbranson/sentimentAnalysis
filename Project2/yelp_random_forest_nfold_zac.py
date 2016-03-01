import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn import metrics
from sklearn import cross_validation
from sklearn.cross_validation import cross_val_score
import string
import linecache



#train = pd.read_csv('yelp.tsv', header=0, delimiter='\t', quoting=3)
#num_reviews_all = train['text'].size

test_tags = []

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def preprocessor(line_number):

    tags = ["/FW","/JJ","JJR","JJS","/MD","/NN","NNS","/RB","RBR","RBS","/VB","VBD","/VBG","VBN","VBP","VBZ"]

    line = linecache.getline('yelp.tsv', line_number).split('\t')
   
    words = line[2].split()

    content_words = []
    for word in words:

        if len(word) > 2:
            #print(word[-3:])
            tag = word[-3:]
            if tag in tags:
                clean_word = "".join([ch for ch in word if ch not in string.punctuation]) 
          
                content_words.append(clean_word.lower()) 
    
    #print(content_words)
    #print("****************************")
    test_tags.append(line[1])
    clean_review = ""
    for word in content_words:
        clean_review += word
        clean_review += " "
    return clean_review

def review_compiler():
    global clean_reviews
    clean_reviews = []
    for i in range(2, num_reviews_all):
        if ((i+1)%100 == 0):
            print("Review %d of %d\n" % (i+1, num_reviews_all))
        clean_reviews.append(preprocessor(i))
    return clean_reviews

def vector():
    global vectorizer
    vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None, \
                             stop_words = None, max_features = 5000) 
    global features
    features = vectorizer.fit_transform(clean_reviews)
    return features.toarray()


#num_reviews_test = 500

num_reviews_all = 1000
compiled_reviews = []

review_compiler()
print(clean_reviews)
vector()


#test_tags = []
#for i in range(0,num_reviews_all):
#    test_tags.append(train['star'][i])

vecs = features
tags = np.array(test_tags)

print("Training the random forest...")

forest = RandomForestClassifier(n_estimators = 100,max_depth=None, min_samples_split=1, random_state=0)
scores = cross_val_score(forest, vecs, tags)

#forest.fit(features, train["star"][0:num_reviews_all])
forest.fit(features, test_tags[0:num_reviews_all])

#result = forest.predict(test_features)
print("="*50, "\n")
print("Results with 5-fold cross validation:\n")
print("="*50, "\n")

predicted = cross_validation.cross_val_predict(forest, vecs, tags, cv=10)
print("\t accuracy_score\t", metrics.accuracy_score(tags, predicted))
print("*"*20)
print("precision_score\t", metrics.precision_score(tags, predicted, average="macro"))
print("recall_score\t", metrics.recall_score(test_tags, predicted, average="macro"))
print("\nclassification_report:\n\n", metrics.classification_report(tags, predicted))
print("\nconfusion_matrix:\n\n", metrics.confusion_matrix(tags, predicted))

outfile = open("cross_val.txt", 'wt')
outfile.write(metrics.classification_report(tags, predicted))
