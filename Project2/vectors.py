
vec = []

with open("sorted.txt", "r") as infile:
    for line in infile:
        words = line.split()
        vec.append(words[0])

dic = {}


out = []
with open("processed.tsv", "r") as infile, open("vectors.tsv", "w") as outfile:
    count = 1
    for line in infile:
        
        for entry in vec:
            dic[entry] = 0

        rev = line.split("\t")
 
        for item in range(2,len(rev)-1):
            word = rev[item]
            if word in dic:
                dic[word] += 1
        
       	for key in dic:
            out.append(dic[key])
        for value in out:
            outfile.write(str(value)+'\t') 
        #outfile.write(str(out))
        outfile.write(rev[1]+"\n")
              
        count += 1
        #if count == 3:
        #    break
        if (count % 1000) == 0:
           print("Processed line: " + str(count))

