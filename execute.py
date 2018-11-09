import re
import nltk

#nltk.download('stopwords')

### Extract the text and save it as a txt file ###
from url_extract_text import url_save_to_text_file

url_save_to_text_file(url='https://www.bbc.com/news/world-us-canada-46125121',file_name='data', style='whitespace')

### Load the text from the .txt file ###
in_file = open("data.txt", "rt") # open file lorem.txt for reading text data
contents = in_file.read()         # read the entire file into a string variable
in_file.close()                   # close the file

### Transform to a list of single sentences ###
from string_to_sentences import string_to_sentences
sentence_list=string_to_sentences(contents)

#print(type(string_sentence))

### Context ###

from context import context_count

#print(context_count('boxing',string_to_sentences(contents)))

### Counters ###

from counters import count_words

#print(count_words(contents))


### Stemming ###

from stemming import stemming

#print(stemming('Disadvantages and advantages of the holy and unholy grail.'))
#print("\n".join(stemming(sentence_list[1])))

### Lemmatization ###

from lemmatization import lemmatization

#print(lemmatization('Disadvantages and advantages of the holy and unholy grail.'))
#print("\n".join(lemmatization(sentence_list[1])))

### Word frequencies ###
from word_frequencies import word_frequencies

import pprint
word_frequencies=word_frequencies(contents)
pprint.pprint(word_frequencies)

lenght_sentence_keep = 30
sentence_scores = {}  
for sent in sentence_list:  
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < lenght_sentence_keep:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

pprint.pprint(sentence_scores)
### !!! I import nltk several times and it is a heavy library !!! ###
