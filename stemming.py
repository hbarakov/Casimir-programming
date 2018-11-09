import nltk
from nltk.stem.porter import PorterStemmer

# All the available stemmers 
#from nltk.stem.api import StemmerI
#from nltk.stem.regexp import RegexpStemmer
#from nltk.stem.lancaster import LancasterStemmer
#from nltk.stem.isri import ISRIStemmer
#from nltk.stem.snowball import SnowballStemmer
#from nltk.stem.wordnet import WordNetLemmatizer
#from nltk.stem.rslp import RSLPStemmer

def stemming(phrase):
    """ 
    Takes a single phrase and outputs the stems of the words
    
    For now using a single stemmer algorithm - implement an argument to change it in the future
    
    phrase: str
        A single phrase
    """
    porter_stemmer = PorterStemmer()
    
    # First Word tokenization
    nltk_tokens = nltk.word_tokenize(phrase)
    #Next find the roots of the word
    stems=[]
    for w in nltk_tokens:
        #print("Actual: %s  Stem: %s"  % (w,porter_stemmer.stem(w)))
        stems.append('Actual: %s  Stem: %s '  % (w,porter_stemmer.stem(w)))
    
    return stems