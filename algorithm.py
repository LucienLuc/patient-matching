import csv
import utility

#dictreader object
data = csv.DictReader(open('Patient Matching Data.csv'))

data_array = []
for row in data:
    data_array.append([row])
#print(data_array)
sort = []
for i in range(len(data_array)):
    index = 0
    for j in range(len(data_array)):
        if i == j:
            continue
        max = 0
        cs = utility.get_confidence_score(data_array[i], data_array[j])
        if cs > max:
            max = cs
            index = j
    data_array[i].append(data_array[j])
    del data_array[j]
        
exit()
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
States: (same as names)

General Notes:
lonber the word/input = more weight in confidence (because more chance to get it right)
a/o l/i m/n for physical writing forms
levenshtein or mederau/levenshtein

Street > State > City > Zip > Sex 

How to sort/compare people:
    add streets into a set (unique)
    go through the set for that street to 
'''