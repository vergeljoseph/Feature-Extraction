
# coding: utf-8

# In[1]:


docA = "the cat sat on my face"
docB = "the dog sat on my bed"


# In[2]:


bowA = docA.split(" ")
bowB = docB.split(" ")


# In[3]:


bowB


# In[4]:


wordSet = set(bowA).union(set(bowB))
wordSet


# In[5]:


wordDictA = dict.fromkeys(wordSet, 0)
wordDictB = dict.fromkeys(wordSet, 0)


# In[6]:


wordDictA


# In[7]:


for word in bowA:
    wordDictA[word]+=1
    
for word in bowB:
    wordDictB[word]+=1


# In[8]:


wordDictA


# In[12]:


import pandas as pd


# In[13]:


pd.DataFrame([wordDictA, wordDictB])


# In[14]:


def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.iteritems():
        tfDict[word] = count / float(bowCount)
    return tfDict


# In[15]:


tfBowA = computeTF(wordDictA, bowA)
tfBowB = computeTF(wordDictB, bowB)


# In[23]:


def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)
    
    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.iteritems():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.iteritems():
        idfDict[word] = math.log(N/float(val))
    
    return idfDict


# In[24]:


idfs = computeIDF([wordDictA, wordDictB])


# In[25]:


def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.iteritems():
        tfidf[word] = val * idfs[word]
    return tfidf


# In[26]:


tfidfBowA = computeTFIDF(tfBowA, idfs)
tfidfBowB = computeTFIDF(tfBowB, idfs)


# In[27]:


import pandas as pd


# In[28]:


pd.DataFrame([tfidfBowA, tfidfBowB])

