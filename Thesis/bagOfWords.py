import collections, re, csv
import math
from nltk import word_tokenize
from nltk.corpus import stopwords

stop = set(stopwords.words('english'))

fileNameIn = "unfilteredData.txt"
fileNameOut = "filteredData.txt"


with open(fileNameIn) as fI:  
  line = fI.readline()
  while line:
  	with open(fileNameOut, "a") as fO:
  		for i in line.lower().split():
  			if i not in stop:
  				fO.write(i + " ")
  		fO.write("\n")
  	line = fI.readline()

with open(fileNameOut, "r") as fI:  
	array = []
	for tweetLine in fI:
		array.append(tweetLine)

bagsofwords = [collections.Counter(re.findall(r'\w+', elements))
            for elements in array]
sumOfBagOfWords = sum(bagsofwords, collections.Counter())

with open('trial.csv', 'wb') as f:
    w = csv.DictWriter(f, sumOfBagOfWords.keys())
    w.writeheader()
    w.writerow(sumOfBagOfWords)