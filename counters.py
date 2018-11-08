import re
from collections import Counter

    
def count_words(text_string):
    text_string = re.sub('[^a-z]+', ' ', text_string.lower())
    return Counter(text_string.split())
    
def count_letters(letter, text_string):
    return text_string.count(letter, 0, len(text_string))


#wordcount = count_word_occurences("a b c d e e e f  a")

#for item in wordcount.most_common(10): print("{}\t{}".format(*item))