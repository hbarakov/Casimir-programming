import re
import nltk
import pprint

#nltk.download('stopwords')

### Extract the text and save it as a txt file ###
from url_extract_text import url_save_to_text_file
url_save_to_text_file(url='https://www.bbc.com/news/world-us-canada-46125121',file_name='data', style='whitespace')


### Load the text from the .txt file ###
in_file = open("data.txt", "rt") 
contents = in_file.read()        
in_file.close()                 

### Transform to a list of single sentences ###
from string_to_sentences import string_to_sentences
sentence_list=string_to_sentences(contents)

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
# Clean the text from punctuation symbols and numbers 
contents_clean = re.sub('[^a-z]+', ' ', contents.lower())

word_frequencies=word_frequencies(contents_clean)
pprint.pprint(word_frequencies)

### Sentence scores ###
from sentence_scores import sentence_scores

lenght_sentence_keep = 14
sentence_scores = sentence_scores(sentence_list, word_frequencies,lenght_sentence_keep)
pprint.pprint(sentence_scores)

### !!! I import nltk several times and it is a heavy library !!!  - Is it time to define a class ?! ###
### !!! Bug when extracting the text - details but could be improved !!! ###
