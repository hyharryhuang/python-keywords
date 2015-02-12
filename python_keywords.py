#!/usr/bin/python
# coding: utf8
from nltk.corpus import stopwords
import re
import string

cachedStopWords = stopwords.words("english")

def removeStopWordsFromString(string):
    return ' '.join([word for word in string.split() if word.lower() not in cachedStopWords])

def removeLinksFromString(string):
	return re.sub(r"(?:https?\://)\S+", "", string).strip()

def removeMentionsFromString(string):
	return re.sub(r"(?:\@)\S+", "", string).strip()

def removeHashtagsFromString(string):
	return re.sub("#", "", string).strip()

#remove retweets
def removeRTsFromString(string):
	return re.sub(r"(?i)\brt\b", "", string).strip()

def removePunctuationFromString(string):
	for p in string.punctuation:
		string = string.replace(p, "")

	return string.strip()