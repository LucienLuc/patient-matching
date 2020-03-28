#code our own algorithm or use libraries?
import fuzzy 
import Levenshtein

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