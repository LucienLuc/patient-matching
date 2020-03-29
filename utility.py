#code our own algorithm or use libraries?
import fuzzy #pip install fuzzy
import Levenshtein #pip install python-levenshtein
import collections
import string
import csv
import homoglyphs
import dictionaries

# csv repo 1 = https://github.com/carltonnorthern/nickname-and-diminutive-names-lookup
# csv repo 2 = https://github.com/MrCsabaToth/SOEMPI/tree/master/openempi

def getCSVContents(csvFilePath):
	data = []
	with open(csvFilePath) as f:
		reader = csv.reader(f)
		for row in reader:
			data.append(row)
	return data

def compareWordsByKeyboardDistance(word1, word2):
	total = 0
	for i,j in word1,word2:
		x1 = dictionaries.keyboard_cartesian[i][x]
		y1 = dictionaries.keyboard_cartesian[i][y]
		x2 = dictionaries.keyboard_cartesian[j][x]
		y2 = dictionaries.keyboard_cartesian[j][y]
		total += manhattanDistance(x1, y1, x2, y2)
	return total
	
def manhattanDistance(x1, y1, x2, y2):
	return abs(x2 - x1) + abs(y2 - y1)

def euclidean_distance(a,b):
    X = (keyboard_cartesian[a]['x'] - keyboard_cartesian[b]['x'])**2
    Y = (keyboard_cartesian[a]['y'] - keyboard_cartesian[b]['y'])**2
    return math.sqrt(X+Y)
     
     
for i in keyboard_cartesian.keys():
    for j in keyboard_cartesian.keys():
        distance_from_i_to_j = [(i, j, euclidean_distance(i, j))]







def removeNumbersFromWord(word):
    return ''.join([i for i in word if not i.isdigit()])

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

def compareByVisuallySimilarChars(word1, word2):
	# rn and m. deal with it. cant go char by char
	for i,j in word1,word2:
		if not homoglyphs.Homoglyphs().get_combinations(i) == homoglyphs.Homoglyphs().get_combinations(j) or dictionaries.similarChars[i] in dictionaries.similarChars[j] or i==j:
			return False
	return True

def compareByAbbrevSentence(sentence1, sentence2):
	return abbrevSentence(sentence1) == sentence2 or sentence1 == abbrevSentence(sentence2)

def abbrevSentence(sentence):
	result = ''
	for word in sentence:
		result += abbrevWord(word)
	return result

def abbrevWord(word):
	return word[0]

def compareDoubleMetaphone(word1, word2):
        dmeta = fuzzy.DMetaphone()
        return dmeta(word1[0]) == dmeta(word2[0]) or dmeta(word1[1]) == dmeta(word2[1])

def levenshtein(string1, string2):
    return Levenshtein.distance(string1,string2)

#Compares two patients and returns confidence that they are the same person
#@param data1 array of a row of patient data 
#@param data2 array of a row of patient data
def get_confidence_score(data1, data2):
    return 0