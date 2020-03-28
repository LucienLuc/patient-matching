#code our own algorithm or use libraries?
import fuzzy #pip install fuzzy
import Levenshtein #pip install python-levenshtein
import collections
import string
import csv

# csv repo 1 = https://github.com/carltonnorthern/nickname-and-diminutive-names-lookup
# csv repo 2 = https://github.com/MrCsabaToth/SOEMPI/tree/master/openempi

def getCSVContents(csvFilePath):
	data = []
	with open(csvFilePath) as f:
		reader = csv.reader(f)
		for row in reader:
			data.append(row)
	return data

def compareNameByNickname(name1, name2):
	csvFilePaths = ['nicknames1.csv','nicknames2.csv']
	allCSVData = getCSVContents(csvFilePaths[0]) + getCSVContents(csvFilePaths[1])
	for nicknameList in allCSVData:
		if name1 in nicknameList and name2 in nicknameList:
			# returns true if name 1 is a nickname for name 2 or vice versa
			return True
	return False

def compareByContains(word1, word2):
	return word1 in word2 or word2 in word1

def compareSentenceBySwap(sentence1, sentence2, separationValue):
	tokens1 = sentence1.split(separationValue)
	tokens2 = sentence2.split(separationValue)
	# returns true if the sentences have the same values in swapped order
	return collections.Counter(tokens1) == collections.Counter(tokens2)

def compareFirstLastSwap(first1, last1, first2, last2):
	# returns true if the first and last names are swapped
	return (first1 == last2) and (last1 == first2)

def compareWordsWithoutSpecialChars(word1, word2):
	# returns true if the words are the same without punctuation and whitespace
    return removeSpecialCharsFromWord(word1) == removeSpecialCharsFromWord(word2)

def removeSpecialCharsFromWord(word):
	remove = string.punctuation + string.whitespace
	# returns word without punctuation and whitespace
	return word.translate(None, remove)

def compareByAbbrevWord(word1, word2):
	return abbrevWord(word1) == word2 or word1 == abbrevWord(word2)

def compareByCommonMisspells(name1, name2):
        return 0
def compareByVisuallySimilarChars(word1, word2):
        return 0

def compareByAbbrevSentence(sentence1, sentence2):
	return abbrevSentence(sentence1) == sentence2 or sentence1 == abbrevSentence(sentence2)

def abbrevSentence(sentence):
	result = ''
	for word in sentence:
		result += abbrevWord(word)
	return result

def abbrevWord(word):
	return word[0]

def doubleMetaphone(word):
        dmeta = fuzzy.DMetaphone()
        return dmeta(word)

def levenshtein(string1, string2):
    return Levenshtein.distance(string1,string2)

#Compares two patients and returns confidence that they are the same person
#@param data1 array of a row of patient data 
#@param data2 array of a row of patient data
def get_confidence_score(data1, data2):
    return 0