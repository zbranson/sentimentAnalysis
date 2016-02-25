from collections import OrderedDict
from operator import itemgetter

freq = {}
sorted_freq = {}
with open("processed.tsv", "r") as infile:
    count = 1
    for line in infile:
        rev = line.split("\t")
        for item in range(2,len(rev)-1):
            if rev[item] not in freq:
                freq[rev[item]] = 1
            else:
                freq[rev[item]]+=1
       	   
        count += 1
        #if count == 10:
        #    break
        if (count % 1000) == 0:
           print("Processed line: " + str(count))

sorted_freq = OrderedDict(sorted(freq.items(), key=itemgetter(1)))

with open("content_words.txt", "w") as outfile:
    for key in sorted_freq:
        outfile.write(str(key)+"\t" + str(sorted_freq[key])+"\n")
    

