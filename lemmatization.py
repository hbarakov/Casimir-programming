import nltk
from nltk.stem import WordNetLemmatizer

def lemmatization(phrase):
    """
    Takes a phrase and returns the lemmas
    
    phrase: str
        The phrase 
    """
    wordnet_lemmatizer = WordNetLemmatizer()
    nltk_tokens = nltk.word_tokenize(phrase)
    
    # Uncomment the first time to download
    #nltk.download('wordnet')
    lemmas=[]
    for w in nltk_tokens:
        #print("Actual: %s  Lemma: %s"  % (w,wordnet_lemmatizer.lemmatize(w)))
        lemmas.append("Actual: %s  Lemma: %s "  % (w,wordnet_lemmatizer.lemmatize(w)))
    
    return lemmas 