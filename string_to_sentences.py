import nltk
from nltk import sent_tokenize
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

def string_to_sentences(text_string):
    """ takes a text string and returns a list of sentences using nltk library
    
    caution: nltk prints newlines if they are present in the string
    
    text_string: str
        the text string
    """
    extra_abbreviations = ['dr', 'vs', 'mr', 'mrs', 'prof', 'inc']

    #nltk.download('punkt')

    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    tokenizer._params.abbrev_types.update(extra_abbreviations) 
    return(tokenizer.tokenize(text_string))
