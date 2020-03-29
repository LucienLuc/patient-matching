import csv

import utility
import dictionaries
#import database

#assume all strings all lower

def calculatePatientAcctNumConfidence(patientAcctNum1, patientAcctNum2):
    if patientAcctNum1 == "" or patientAcctNum2 == "":
        return 0
    distance = utility.levenshtein(patientAcctNum1, patientAcctNum2)
    confidence = 1/pow(distance+1,0.15*distance)
    return confidence

def calculateFullNameConfidence(first1, last1, first2, last2):
    if (first1 == '' or first2 == '') and (last1 != '' or last2 != ''):
        return calculateNameConfidence(last1, last2)
    elif (first1 != '' or first2 != '') and (last1 == '' or last2 == ''):
        return calculateNameConfidence(first1, first2)
    elif ((first1 == '' or first2 == '') and (last1 == '' or last2 == '')):
        return none
    else:
        total = 0
        if utility.compareFirstLastSwap(first1, last1, first2, last2):
            total += 0.2
        total += calculateNameConfidence(first1, first2) * 0.3
        total += calculateNameConfidence(last1, last2) * 0.5
        return total

def calculateNameConfidence(name1, name2):
    total = 0

    if utility.compareByAbbrevWord(name1, name2):
        total += 0.1
    
    if utility.compareWordsWithoutSpecialChars(name1, name2):
        return 1

    if utility.compareNameByNickname(middle1, middle2):
        total += 0.35

    if utility.compareByContains(name1, name2):
        total += 0.05
    
    if utility.compareByDoubleMetaphone(name1, name2):
        total += 0.25

    if utility.compareByVisuallySimilarChars(name1, name2):
        return 1
    
    #CHANGE
    manhattandistance = utility.compareWordsByKeyboardDistance(name1, name2)

    levDistance = utility.levenshtein(name1, name2)
    levConfidence = 1/(pow(levDistance+1,0.9*levDistance)) * 0.25
    total += levConfidence
    return total

def calculateMiddleIConfidence(middle1, middle2):
    if middle1 == "" or middle2 == "":
        return None
    total = 0

    if utility.compareByAbbrevWord(middle1, middle2):
        total += 0.1
    
    if utility.compareWordsWithoutSpecialChars(middle1, middle2):
        return 1

    if utility.compareNameByNickname(middle1, middle2):
        total += 0.35
    
    if utility.compareByContains(middle1, middle2):
        total += 0.05
    
    if utility.compareByDoubleMetaphone(middle1, middle2):
        total += 0.25

    if utility.compareByVisuallySimilarChars(middle1, middle2):
        return 1
    
    #change
    manhattandistance = utility.compareWordsByKeyboardDistance(middle1, middle2)

    levDistance = utility.levenshtein(middle1, middle2)
    levConfidence = 1/(pow(levDistance+1,0.2*levDistance)) * .25
    total += levConfidence
    return total

def calculateDOBConfidence(dob1, dob2):
    if dob1 == "" or dob2 == "":
        return None
    distance = utility.levenshtein(dob1, dob2)
    confidence = 1/pow(distance+1,0.5*distance)
    return confidence

def calculateSexConfidence(sex1, sex2):
    if sex1 == "" or sex2 == "":
        return None
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
    if street1 == "" or street2 == "":
        return None
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
    
    if street1 == street2:
        return 1
    
    #double metaphone for each word
    for elem1, elem2 in zip(street1, street2):
        if elem1 == None or elem2 == None:
            break
        if utility.compareByDoubleMetaphone(elem1,elem2):
            metaphoneConfidence = 1/(max(len(street1),len(street2)))
    
    street1 = ' '.join(str(elem) for elem in street1)
    street2 = ' '.join(str(elem) for elem in street2)

    #levenshtein
    distance = utility.levenshtein(street1, street2)
    levenshteinConfidence = 1/(pow(distance+1,0.2*distance))

    return metaphoneConfidence * 0.5 + levenshteinConfidence * 0.5

def calculateCityConfidence(city1, city2):
    if city1 == "" or city2 == "":
        return None
    #calculate two fully spelled out cities
    #levenshtein
    else:
        distance = utility.levenshtein(city1, city2)

        dmetaScore = 0
    #double metaphone
        if utility.compareByDoubleMetaphone(city1, city2):
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
    if state1 == "" or state2 == "":
        return None
    else:
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
    if zip1 == "" or zip2 == "":
        return None
    else:
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
    row1 = [x.strip() for x in row1]
    row2 = [x.strip() for x in row2]

    print(row1)
    print(row2)
    #use dictionary in case their columns are messed up
    notBlankCount = 0
    for elem1, elem2 in zip(row1, row2):
        if elem1 != "" or elem2 != "":
            notBlankCount += 1
    PAN = calculatePatientAcctNumConfidence(row1[2], row2[2]) * 0.01
    print('PAN: ' + str(PAN))
    CN = calculateFullNameConfidence(row1[3], row1[5], row2[3], row2[5]) * 0.075
    print('CN: ' + str(CN))
    CMI = calculateMiddleIConfidence(row1[4], row2[4]) * 0.01
    print('CMI: ' + str(CMI))
    DOB = calculateDOBConfidence(row1[6], row2[6]) * 0.02
    print('DOB: ' + str(DOB))
    S = calculateSexConfidence(row1[7], row2[7]) * 0.04
    print('S: ' + str(S))
    CS1 = calculateStreetConfidence(row1[8], row2[8]) * 0.2
    print('CS1: ' + str(CS1))
    CS2 = calculateStreetConfidence(row1[9], row2[9]) * 0.01
    CC = calculateCityConfidence(row1[10], row2[10]) * 0.07
    CS = calculateStateConfidence(row1[11], row2[11]) * 0.07
    CZ = calculateZipConfidence(row1[12], row2[12]) * 0.03

    PN = calculateFullNameConfidence(row1[13], row1[15], row2[13], row2[15]) * 0.075
    PMI = calculateMiddleIConfidence(row1[14], row2[14]) * 0.01
    PS1 = calculateStreetConfidence(row1[16], row2[16]) * 0.2
    PS2 = calculateStreetConfidence(row1[17], row2[17]) * 0.01
    PC = calculateCityConfidence(row1[18], row2[18]) * 0.07
    PS = calculateStateConfidence(row1[19], row2[19]) * 0.07
    PZ = calculateZipConfidence(row1[20], row2[20]) * 0.03
    
    score = (PAN + CN + CMI + DOB + S + CS1 + CS2 + CC + CS + CZ + PN + PMI + PS1 + PS2 + PC + PS + PZ)
    print('score': str(score))
    return score

def groupByConfidenceScore(data, confidenceThreshold):
    alreadyAddedList = []
    result = []
    counter = 0
    for row1 in data:
        if row1 in alreadyAddedList:
            continue
        group = [row1]
        alreadyAddedList.append(row1)
        for row2 in data:
            if row2 not in alreadyAddedList:
                if getConfidenceScore(row1, row2) >= confidenceThreshold:
                    counter += 1
                    group.append(row2)
                    alreadyAddedList.append(row2)
                if counter == 7:
                    exit()
        result.append(group)
    # return an array of groups
    print(len(result))
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