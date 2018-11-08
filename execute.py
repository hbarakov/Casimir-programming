import re

### Extract the text and save it as a txt file ###
from url_extract_text import url_save_to_text_file

url_save_to_text_file(url='https://www.theguardian.com/sport/blog/2018/nov/08/womens-boxing-television-deals',file_name='data', style='whitespace')

### Load the text from the .txt file ###
in_file = open("data.txt", "rt") # open file lorem.txt for reading text data
contents = in_file.read()         # read the entire file into a string variable
in_file.close()                   # close the file

### Transform to a list of single sentences ###
from string_to_sentences import string_to_sentences

print(type(string_to_sentences(contents)))