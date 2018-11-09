import nltk

def word_frequencies(formatted_text_single_str):
    """
    The function gives the frequency with which each word appears in the text
    
    formatted_tex_single_str: str
        the text as a single string
        
    Return: A dictionary 
    """
    stopwords = nltk.corpus.stopwords.words('english')

    word_frequencies = {}  
    for word in nltk.word_tokenize(formatted_text_single_str):  
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
               
    # Evaluate the frequency with respect to the max that appeared - normalized frequency
    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():  
        word_frequencies[word] = word_frequencies[word]/maximum_frequncy
    
    return (word_frequencies)


