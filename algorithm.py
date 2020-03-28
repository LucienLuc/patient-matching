import csv
import utility
#import database

#assume all strings all lower

def calculatePatientAcctNumConfidence(patientAcctNum1, patientAcctNum2):
    return 0

def calculateNameConfidence(first1, last1, first2, last2):
    utility.compareFirstLastSwap()
    calculateNameConfidence()
    calculateNameConfidence()
    
def calculateNameConfidence(name1, name2):
    utility.levenshtein()
    utility.compareByAbbrevWord()
    utility.compareWordsWithoutSpecialChars()
    utility.compareNameByNickname()
    utility.compareByContains()
    utility.doubleMetaphone()
    utility.compareByCommonMisspells()
    utility.compareByVisuallySimilarChars()

    # keyboard distance

def calculateMiddleIConfidence(middle1, middle2):
    return 0

def calculateDOBConfidence(DOB1, DOB2):
    return 0

def calculateSexConfidence(sex1, sex2):
    try:
        sex1 = utility.sex[sex1]
    except KeyError:
        pass
    try:
        sex2 = utility.sex[sex2]
    except KeyError:
        pass
    distance = utility.levenshtein(sex1, sex2)
    confidence = 1/(pow(distance+1, distance))
    return confidence

def calculateStreet1Confidence(street11, street12):
    return 0

def calculateStreet2Confidence(street21, middle22):
    return 0

def calculateCityConfidence(city1, city2):
    distance = utility.levenshtein(city1, city2)
    dmeta1 = utility.doubleMetaphone(city1)
    dmeta2 = utility.doubleMetaphone(city2)

    distance = utility.levenshtein(dmeta1[0],dmeta2[0])
    

    confidence = 1/(pow(distance+1, distance+1))
    return confidence

#typos on abbreviations really screw this up   
def calculateStateConfidence(state1, state2):
    #convert abbreviations to full states
    try: 
        state1 = utility.states[state1]
    except KeyError:
        pass
    try:
        state2 = utility.states[state2]
    except KeyError:
        pass
    distance = utility.levenshtein(state1, state2)
    confidence = 1/(distance+1)
    return confidence

def calculateZipConfidence(zip1, zip2):
    distance = utility.levenshtein(zip1, zip2) 
    # distance -> confidence
    #0 -> 1
    #1 -> 0.5
    #2 -> 0.11
    #3 -> .0156
    confidence = 1/(pow(distance+1, distance))
    return confidence

def getConfidenceScore(row1, row2):
    row1 = [x.lower() for x in row1]
    row2 = [x.lower() for x in row2]

    PAN = calculatePatientAcctNumConfidence(row1[2], row2[2])
    CN = calculateNameConfidence(row1[3], row1[5], row2[3], row2[5])
    CMI = calculateMiddleIConfidence(row1[4], row2[4])
    DOB = calculateDOBConfidence(row1[6], row2[6])
    S = calculateSexConfidence(row1[7], row2[7])
    CS1 = calculateStreet1Confidence(row1[8], row2[8])
    CS2 = calculateStreet2Confidence(row1[9], row2[9])
    CC = calculateCityConfidence(row1[10], row2[10])
    CS = calculateStateConfidence(row1[11], row2[11])
    CZ = calculateZipConfidence(row1[12], row2[12])

    PN = calculateNameConfidence(row1[13], row1[15], row2[13], row2[15])
    PMI = calculateMiddleIConfidence(row1[14], row2[14])
    PS1 = calculateStreet1Confidence(row1[16], row2[16])
    PS2 = calculateStreet2Confidence(row1[17], row2[17])
    PC = calculateCityConfidence(row1[18], row2[18])
    PS = calculateStateConfidence(row1[19], row2[19])
    PZ = calculateZipConfidence(row1[20], row2[20])

    return PAN + CN + CMI + DOB + S + CS1 + CS2 + CC + CS + CZ + PN + PMI + PS1 + PS2 + PC + PS + PZ



def groupByConfidenceScore(data, confidenceThreshold):
    alreadyAddedList = []
    result = []
    for row1 in data:
        group = [row1]
        alreadyAddedList.append(row1)
        for row2 in data:
            if row2 not in alreadyAddedList:
                if getConfidenceScore(row1, row2) >= confidenceThreshold:
                    group.append(row2)
        result.add(group)
    # return an array of groups
    for group in result:
        print("group: ")
        for person in group:
            print(person[1] + ", ")
    return result




'''
STRINGS
Soundex vs metaphone
Levenstein distance
Abrevations for States


Account Number: check for name in account number (feel like this is useless)
Names: abreviations, common shorter versions, soundex, levenstein, make all lowercase when checking
        common longer versions (also try to deal with anne-marie vs anne), common other spellings, keyboard distance typos, characters that look similiar
        switch first/last, special characters (T-J vs T.J vs TJ)
Date of Birth: Levenstein, swapping month/day/year, spelled out date?
Sex: abbreviations
Streets: possibly swapping of words, (do everything as names but for multiple words)
Zip: Levenstein
States: (same as names) - almost

General Notes:
lonber the word/input = more weight in confidence (because more chance to get it right)
a/o l/i m/n for physical writing forms
levenshtein or mederau/levenshtein

Street > State > City > Zip > Sex 

How to sort/compare people:
    add streets into a set (unique)
    go through the set for that street to 
'''