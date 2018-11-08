import re
import nltk
from string_to_sentences import string_to_sentences
from counters import count_words
from collections import Counter
from nltk.corpus import gutenberg

def context_count(word, sentences):
    """This counts all words that are in the same sentences as the given word"""
    
    wordcount = count_words("")
        
    for sentence in sentences:
        counts = count_words(sentence)
        if counts[word] > 0:
            wordcount += counts
    return wordcount

text = ""

for file_id in gutenberg.fileids():
    text += gutenberg.raw(file_id)
    
#words = context_count("joe",string_to_sentences(text))
words = count_words(text)

for item in words.most_common(1000): print("{}\t{}".format(*item))