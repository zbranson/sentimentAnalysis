from nltk.corpus import stopwords
import string

def remove_punct(text):
    text = "".join([ch for ch in text if ch not in string.punctuation])
    return text

with open("./Data/yelp_reviews.tsv", "r") as infile, open ("processed.tsv", "w") as outfile:
    count = 1
    for line in infile:

        print("Processing line: " + str(count))
        count +=1
        data = line.split("\t")
        data[2] = remove_punct(data[2])
        words = data[2].split()

        outfile.write(data[0]+"\t")
        outfile.write(data[1]+"\t")
        for word in words:
            if word.lower() not in stopwords.words('english'):
                outfile.write(word.lower() + "\t")
                print(word.lower())
        outfile.write("\n")
        if count == 5:
            break
