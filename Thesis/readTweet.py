import io, re, collections
import string
import json, csv
from nltk import word_tokenize
from nltk.corpus import stopwords
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EmotionOptions, SentimentOptions


def initOutput(fileName):
  fileName = fileName.replace('.txt', '.xlsx')
  fileName = fileName.replace('input_files/', '')
  fileOut = 'output_files/' + fileName
  f = csv.writer(open(fileOut, "wb+"))
  f.writerow(["emotion_joy", 
              "emotion_anger", 
              "emotion_sadness", 
              "emotion_fear", 
              "sentiment_score", 
              "no_of_words"])
  return f

# GET EMOTION AND SENTIMENT #
def getEmotion(line, f):
  natural_language_understanding = NaturalLanguageUnderstandingV1(
    username='8f8f6353-8198-4241-a106-449c097a7970',
    password='OXyWnrd5fA0z',
    version='2018-03-16')

  wordCount = len(line.split(" "))
  response = natural_language_understanding.analyze(
    language="en",
    # url='https://www.time-to-change.org.uk/blog/school-i-never-wanted-anyone-know-about-my-anxiety',
    text = line,
    features=Features(
      emotion=EmotionOptions(),
      sentiment=SentimentOptions()))

  f.writerow([response['emotion']['document']['emotion']['joy'],
              response['emotion']['document']['emotion']['anger'],
              response['emotion']['document']['emotion']['sadness'],
              response['emotion']['document']['emotion']['fear'],
              response['sentiment']['document']['score'],
              wordCount])

# MAIN FUNCTION #

stopwords = set(stopwords.words('english'))
fileIn = 'input_files/icbsalvador.txt'  
fileOut = initOutput(fileIn)

with open(fileIn, 'r') as fp:  
  line = fp.readline()
  while line:
    if (len(line)) >= 10:
      getEmotion(line, fileOut)
      # countWords(line, fileOut)
    line = fp.readline()