#code our own algorithm or use libraries?
import fuzzy 
import Levenshtein
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

def abbrevSentence(sentence):
	result = ''
	for word in sentence:
		result += abbrevWord(word)
	return result

def abbrevWord(word):
	return word[0]

'''
name1 = 'Drake'
name2 = 'Dracke'
dmeta = fuzzy.DMetaphone()
print(dmeta(name1))
print(dmeta(name2))
print(fuzzy.nysiis(name1))
print(fuzzy.nysiis(name2))
'''

states = {
        'ak': 'alaska',
        'al': 'alabama',
        'ar': 'arkansas',
        'as': 'american samoa',
        'az': 'arizona',
        'ca': 'california',
        'co': 'colorado',
        'ct': 'connecticut',
        'dc': 'district of columbia',
        'de': 'delaware',
        'fl': 'florida',
        'ga': 'georgia',
        'gu': 'guam',
        'hi': 'hawaii',
        'ia': 'iowa',
        'id': 'idaho',
        'il': 'illinois',
        'in': 'indiana',
        'ks': 'kansas',
        'ky': 'kentucky',
        'la': 'louisiana',
        'ma': 'massachusetts',
        'md': 'maryland',
        'me': 'maine',
        'mi': 'michigan',
        'mn': 'minnesota',
        'mo': 'missouri',
        'mp': 'northern mariana islands',
        'ms': 'mississippi',
        'mt': 'montana',
        'na': 'national',
        'nc': 'north carolina',
        'nd': 'north dakota',
        'ne': 'nebraska',
        'nh': 'new hampshire',
        'nj': 'new jersey',
        'nm': 'new mexico',
        'nv': 'nevada',
        'ny': 'new york',
        'oh': 'ohio',
        'ok': 'oklahoma',
        'or': 'oregon',
        'pa': 'pennsylvania',
        'pr': 'puerto rico',
        'ri': 'rhode island',
        'sd': 'south carolina',
        'sd': 'south dakota',
        'tn': 'tennessee',
        'tx': 'texas',
        'ut': 'utah',
        'va': 'virginia',
        'vi': 'virgin islands',
        'vt': 'vermont',
        'wa': 'washington',
        'wi': 'wisconsin',
        'wv': 'west virginia',
        'wy': 'wyoming'
}


#Compares two patients and returns confidence that they are the same person
#@param data1 array of a row of patient data 
#@param data2 array of a row of patient data
def get_confidence_score(data1, data2):
    return 0