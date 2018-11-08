import nltk
from nltk import sent_tokenize
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

def string_to_sentence(sentences):
    extra_abbreviations = ['dr', 'vs', 'mr', 'mrs', 'prof', 'inc']

    #nltk.download('punkt')

    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    tokenizer._params.abbrev_types.update(extra_abbreviations) 
    return(tokenizer.tokenize(sentences))

#print(string_to_sentence("Mr. James told me Dr. Brown is not available today. I will try tomorrow."))