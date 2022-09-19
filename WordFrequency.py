import re
infile = open('sometext.txt','r')

wordfrequency = dict()


for line in infile:
    line = line.strip()
    line = re.sub(r'[^\w\s]','',line)
    line = line.lower()
    words = line.split(" ")

    for word in words:
        if word in wordfrequency:
            wordfrequency[word] = wordfrequency[word] + 1
        else: 
            wordfrequency[word] = 1
    print("Word: " "Frequency", '\n')

for key in list(wordfrequency.keys()):
    print(key, ": ", wordfrequency[key], sep = '')
