import csv
import utility
#import database

print(utility.doubleMetaphone('2341', '2341'))
print(utility.states['ca'])
try:
    print(utility.states['aa'])
except KeyError:
    print("No Key")
exit()

#assume all strings all lower

def calculatePatientAcctNumConfidence(patientAcctNum1, patientAcctNum2):
    
def calculateNameConfidence(first1, last1, first2, last2):
    
def calculateFirstNameConfidence(first1, first2):

def calculateLastNameConfidence(last1, last2):
    
def calculateMiddleIConfidence(middle1, middle2):
    
def calculateDOBConfidence(DOB1, DOB2):
    
def calculateSexIConfidence(sex1, sex2):
    
def calculateStreet1IConfidence(street11, street12):
    
def calculateStreet2Confidence(street21, middle22):
    
def calculateCityConfidence(city1, city2):
    

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
    distance = utility.levenshtein(state1,state2)
    confidence = 1/(distance+1)
    return confidence

def calculateZipIConfidence(zip1, zip2):
    distance = utility.levenshtein(zip1,zip2) 
    # distance -> confidence
    #0 -> 1
    #1 -> 0.5
    #2 -> 0.11
    #3 -> .0156
    confidence = 1/(pow(distance+1,distance))
    return confidence


def getConfidenceScore(row1, row2):
    
    patientID
    patientAcct#
    firstName
    middleI
    lastName
    dateOfBirth
    sex
    currentStreet1
    currentStreet2
    currentCity
    currentState
    currentZipCode
    previousfirstName
    previousmiddleI
    previouslastName
    previousStreet1
    previousStreet2
    previousCity
    previousState
    previousZipCode




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