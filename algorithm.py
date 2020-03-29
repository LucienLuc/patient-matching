import csv

import utility
import dictionaries
#import database

#assume all strings all lower

def calculatePatientAcctNumConfidence(patientAcctNum1, patientAcctNum2):
    distance = utility.levenshtein(patientAcctNum1, patientAcctNum2)
    confidence = 1/pow(distance+1,0.15*distance)
    return confidence

def calculateNameConfidence(first1, last1, first2, last2):
    total = 0
    if utility.compareFirstLastSwap(first1, last1, first2, last2):
        total += 0.2
    total += calculateNameConfidence(first1, first2) * 0.3
    total += calculateNameConfidence(last1, last2) * 0.5
    return total

def calculateNameConfidence(name1, name2):
    total = 0

    if utility.compareByAbbrevWord(name1, name2):
        total += 0.2
    
    if utility.compareWordsWithoutSpecialChars(name1, name2):
        total += 0.9

    if utility.compareNameByNickname(name1, name2):
        total += 0.5
    
    if utility.compareByContains(name1, name2):
        total += 0.6
    
    if utility.doubleMetaphone(name1, name2):
        total += 0.8

    if utility.compareByVisuallySimilarChars(name1, name2):
        total += 0.9
    
    utility.compareByKeyboardDistance(name1, name2)

    levDistance = utility.levenshtein(name1, name2)
    levConfidence = 1/(pow(levDistance+1,0.2*levDistance))
    total += levConfidence
    return min(total,1)

def calculateMiddleIConfidence(middle1, middle2):
    return 1

def calculateDOBConfidence(dob1, dob2):
    distance = utility.levenshtein(dob1, dob2)
    confidence = 1/pow(distance+1,0.5*distance)
    return confidence

def calculateSexConfidence(sex1, sex2):
    try:
        sex1 = dictionaries.sex[sex1]
    except KeyError:
        pass
    try:
        sex2 = dictionaries.sex[sex2]
    except KeyError:
        pass
    distance = utility.levenshtein(sex1, sex2)
    confidence = 1/(pow(distance+1, distance))
    return confidence

def calculateStreetConfidence(street1, street2):
    street1 = street1.split(' ')
    street2 = street2.split(' ')

    #convert street abbreviations to fully spelled out
    try:
        street1[-1] = dictionaries.streets[street1[-1]]
    except KeyError:
        pass
    try: 
         street2[-1] = dictionaries.streets[street2[-1]]
    except KeyError:
        pass
    
    #levenshtein
    #double metaphone
    #shortened versions

    return 0

def calculateCityConfidence(city1, city2):

    #calculate two fully spelled out cities
    #levenshtein
    distance = utility.levenshtein(city1, city2)

    dmetaScore = 0
    #double metaphone
    if utility.compareDoubleMetaphone(city1, city2):
        dmetaScore = 0.5

    #calculate abbreviations
    abbreviationScore = 0
    shortenedScore = 0
    if utility.compareByAbbrevSentence(city1, city2):
        abbreviationScore = (min(len(city1),len(city2)))/5
    #calculate shortened versions (if abbreviated skip)
    elif utility.compareByContains(city1,city2):
        shortenedScore = (min(len(city1),len(city2)))/max(len(city1),len(city2))

    confidence = min(1/(pow(distance+1, distance+1)) + dmetaScore + abbreviationScore + shortenedScore, 1)
    return confidence

#typos on abbreviations really screw this up   
def calculateStateConfidence(state1, state2):
    #convert abbreviations to full states
    try: 
        state1 = dictionaries.states[state1]
    except KeyError:
        pass
    try:
        state2 = dictionaries.states[state2]
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

    #use dictionary in case their columns are messed up
    PAN = calculatePatientAcctNumConfidence(row1[2], row2[2])
    CN = calculateNameConfidence(row1[3], row1[5], row2[3], row2[5])
    CMI = calculateMiddleIConfidence(row1[4], row2[4])
    DOB = calculateDOBConfidence(row1[6], row2[6])
    S = calculateSexConfidence(row1[7], row2[7])
    CS1 = calculateStreetConfidence(row1[8], row2[8])
    CS2 = calculateStreetConfidence(row1[9], row2[9])
    CC = calculateCityConfidence(row1[10], row2[10])
    CS = calculateStateConfidence(row1[11], row2[11])
    CZ = calculateZipConfidence(row1[12], row2[12])

    PN = calculateNameConfidence(row1[13], row1[15], row2[13], row2[15])
    PMI = calculateMiddleIConfidence(row1[14], row2[14])
    PS1 = calculateStreetConfidence(row1[16], row2[16])
    PS2 = calculateStreetConfidence(row1[17], row2[17])
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