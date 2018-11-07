import re
def txt_to_string(filename):

    file = open(filename,"r")  
    txtdata = file.read().lower()
    txtdata = re.sub('[^a-z]+', ' ', txtdata)
    return txtdata    
    file.close() 

    
def count_word_occurences(word, text):
    data = " " + text
    return text.count(" " + word + " ", 0, len(text))

def count_letter_occurences(letter, text):
    return text.count(letter, 0, len(text))


text = txt_to_string("testfile.txt")
print(count_letter_occurences("e", text))