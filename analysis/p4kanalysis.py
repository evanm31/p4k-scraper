# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:26:45 2017

@author: Evan
"""
#import required packages
import nltk
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.book import *
import pylab

'''
Initially we import the data, then concatenates the reviews together
into a single string for tokenization and POS tagging. A wordcloud is generated
using the entire corpus for comparison with genre wordclouds.
'''
#extract and tokenize all review words
p4k = pd.read_csv("C:/Users/Evan/Documents/scrapeFork/p4kreviews.csv", encoding = "ISO-8859-1")
p4k = p4k.drop(p4k.index[13300]) #drop index that gives join a problem
string = ' '.join(p4k['review'])
words = nltk.word_tokenize(string)
#word frequency
stopwords = nltk.corpus.stopwords.words('english') 
fdistWord = FreqDist(word for word in words if word not in stopwords)
#pos tagging/adjective frequency
text_tag = nltk.pos_tag(words) #adj = jj
fdistAdj = FreqDist(token for token in text_tag if "JJ" in token)
fdistAdj.most_common(25)
#wordcloud - all text
allWordcloud = WordCloud().generate(string)
plt.imshow(allWordcloud, interpolation='bilinear')
plt.axis("off")
pylab.savefig('C:/Users/Evan/Documents/p4kdata/allCloud.png', dpi = 500, bbox_inches='tight', pad_inches = 0)

'''
Now, we consider subsets of the dataset by genre to help make conclusion about
how the language differs in each. Once these are created, a new string of just
those reviews is created and filtered based on the most common words that appear
in all genres. Once we have this, wordcloud and adjective frequency distributions
can be created for each genre. A smaller subset of the first 100 rows of each
genre is also created for use later in TF-IDF.
'''
#by genre
#rock
rock = p4k.loc[p4k["genre"] == "Rock"]
rockShort = rock.iloc[:100]
string = ' '.join(rock['review'])
string = string.replace("album", " ")
string = string.replace("song", " ")
rockString = string.replace("record", " ")
#wordcloud
rockWordcloud = WordCloud().generate(rockString)
plt.imshow(rockWordcloud, interpolation='bilinear')
plt.axis("off")
pylab.savefig('C:/Users/Evan/Documents/p4kdata/rockCloud.png', dpi = 500, bbox_inches='tight', pad_inches = 0)
#adjectives
rockWords = nltk.word_tokenize(rockString)
text_tag_rock = nltk.pos_tag(rockWords) #adj = jj
fdistAdjRock = FreqDist(token for token in text_tag_rock if "JJ" in token)
fdistAdjRock.most_common(10)

#jazz
jazz = p4k.loc[p4k["genre"] == "Jazz"]
jazzShort = jazz.iloc[:100]
string = ' '.join(jazz['review'])
string = string.replace("album", " ")
string = string.replace("song", " ")
jazzString = string.replace("record", " ")
#wordcloud
jazzWordcloud = WordCloud().generate(jazzString)
plt.imshow(jazzWordcloud, interpolation='bilinear')
plt.axis("off")
pylab.savefig('C:/Users/Evan/Documents/p4kdata/jazzCloud.png', bbox_inches='tight')
#adjectives
jazzWords = nltk.word_tokenize(jazzString)
text_tag_jazz = nltk.pos_tag(jazzWords) #adj = jj
fdistAdjJazz = FreqDist(token for token in text_tag_jazz if "JJ" in token)
fdistAdjJazz.most_common(25)

#metal
metal = p4k.loc[p4k["genre"] == "Metal"]
metalShort = metal.iloc[:100]
string = ' '.join(metal['review'])
string = string.replace("album", " ")
string = string.replace("song", " ")
metalString = string.replace("record", " ")
#wordcloud
metalWordcloud = WordCloud().generate(metalString)
plt.imshow(metalWordcloud, interpolation='bilinear')
plt.axis("off")
pylab.savefig('C:/Users/Evan/Documents/p4kdata/metalCloud.png', bbox_inches='tight')
#adjectives
metalWords = nltk.word_tokenize(metalString)
text_tag_metal = nltk.pos_tag(metalWords) #adj = jj
fdistAdjMetal = FreqDist(token for token in text_tag_metal if "JJ" in token)
fdistAdjMetal.most_common(25)

#rap
rap = p4k.loc[p4k["genre"] == "Rap"]
rapShort = rap.iloc[:100]
string = ' '.join(rap['review'])
string = string.replace("album", " ")
string = string.replace("song", " ")
rapString = string.replace("record", " ")
#wordcloud
rapWordcloud = WordCloud().generate(rapString)
plt.imshow(rapWordcloud, interpolation='bilinear')
plt.axis("off")
pylab.savefig('C:/Users/Evan/Documents/p4kdata/rapCloud.png', bbox_inches='tight')
#adjectives
rapWords = nltk.word_tokenize(rapString)
text_tag_rap = nltk.pos_tag(rapWords) #adj = jj
fdistAdjRap = FreqDist(token for token in text_tag_rap if "JJ" in token)
fdistAdjRap.most_common(25)

#electronic
elec = p4k.loc[p4k["genre"] == "Electronic"]
elecShort = elec.iloc[:100]
string = ' '.join(elec['review'])
string = string.replace("album", " ")
string = string.replace("song", " ")
elecString = string.replace("record", " ")
#wordcloud
elecWordcloud = WordCloud().generate(elecString)
plt.imshow(elecWordcloud, interpolation='bilinear')
plt.axis("off")
pylab.savefig('C:/Users/Evan/Documents/p4kdata/elecCloud.png', bbox_inches='tight')

#adjectives
elecWords = nltk.word_tokenize(elecString)
text_tag_elec = nltk.pos_tag(elecWords) #adj = jj
fdistAdjElec = FreqDist(token for token in text_tag_elec if "JJ" in token)
fdistAdjElec.most_common(25)

#best
best = p4k.loc[p4k["best"] == 1]
bestShort = best.iloc[:100]
string = ' '.join(best['review'])
string = string.replace("album", " ")
string = string.replace("song", " ")
bestString = string.replace("record", " ")
#wordcloud
bestWordcloud = WordCloud().generate(bestString)
plt.imshow(bestWordcloud, interpolation='bilinear')
plt.axis("off")
pylab.savefig('C:/Users/Evan/Documents/p4kdata/bestCloud.png', bbox_inches='tight')
#adjectives
bestWords = nltk.word_tokenize(bestString)
text_tag_best = nltk.pos_tag(bestWords) #adj = jj
fdistAdjBest = FreqDist(token for token in text_tag_best if "JJ" in token)
fdistAdjBest.most_common(25)

#pop
pop = p4k.loc[p4k["genre"] == "Pop/R&B"]
popShort = pop.iloc[:100]
str = ' '.join(pop['review'])
str = str.replace("album", " ")
str = str.replace("song", " ")
popString = str.replace("record", " ")
#wordcloud
popWordcloud = WordCloud().generate(popString)
plt.imshow(popWordcloud, interpolation='bilinear')
plt.axis("off")
pylab.savefig('C:/Users/Evan/Documents/p4kdata/popCloud.png', bbox_inches='tight')
#adjectives
popWords = nltk.word_tokenize(popString)
text_tag_pop = nltk.pos_tag(popWords) #adj = jj
fdistAdjPop = FreqDist(token for token in text_tag_pop if "JJ" in token)
fdistAdjPop.most_common(25)

'''
The functions and code used to compute the TF-IDF was found online, since there
is surprisingly no easy function that allows you to do this in Python already.
(source: http://stevenloria.com/finding-important-words-in-a-document-using-tf-idf/)
Short review strings were created and filtered using the small subsets of each
genre, then TF-IDF statistics were computed across the entire corpus. 
'''
#tf-idf functions
import math
from textblob import TextBlob as tb

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

#short strings
string = ' '.join(rockShort['review'])
string = string.replace("album", " ")
string = string.replace("song", " ")
rockStringShort = string.replace("record", " ")

string = ' '.join(rapShort['review'])
string = string.replace("album", " ")
string = string.replace("song", " ")
rapStringShort = string.replace("record", " ")

string = ' '.join(metalShort['review'])
string = string.replace("album", " ")
string = string.replace("song", " ")
metalStringShort = string.replace("record", " ")

string = ' '.join(jazzShort['review'])
string = string.replace("album", " ")
string = string.replace("song", " ")
jazzStringShort = string.replace("record", " ")

string = ' '.join(elecShort['review'])
string = string.replace("album", " ")
string = string.replace("song", " ")
elecStringShort = string.replace("record", " ")

string = ' '.join(bestShort['review'])
string = string.replace("album", " ")
string = string.replace("song", " ")
bestStringShort = string.replace("record", " ")

string = ' '.join(popShort['review'])
string = string.replace("album", " ")
string = string.replace("song", " ")
popStringShort = string.replace("record", " ")

stringlist = [rockStringShort, jazzStringShort, metalStringShort, elecStringShort, bestStringShort, rapStringShort, popStringShort]

bloblist = []

#filter stopwords
for string in stringlist:
    string = ' '.join([word for word in string.split() if word not in stopwords])
    bloblist.append(tb(string))
    
for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:5]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
