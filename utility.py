#code our own algorithm or use libraries?
import fuzzy 
import Levenshtein

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'md': 'Maryland',
        'me': 'Maine',
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