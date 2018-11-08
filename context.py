import re
from counters import count_words
from collections import Counter

def context_count(word, sentences):
    """This counts all words that are in the same sentences as the given word"""
    
    wordcount = count_words("")
    
    for sentence in sentences:
        wordcount += count_words(sentence)
    return wordcount


#words = context_count("is",["This is the first sentence", "Another example is this", "And"])

#for item in words.most_common(10): print("{}\t{}".format(*item))