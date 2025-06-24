from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
from collections import Counter

text='This is a test set of text data - only used for testing purposes only.'
stop_words=set(stopwords.words('english'))

def preprocess(data):
    s=re.sub(r'[\.\?\!\,\:\;\"]', '', data)
    # Replace punctuation with no space
    s = re.sub(r"[^\w\s]", '', s)
    # replace digits with no space
    s = re.sub(r"\d", '', s)
    return s

def tokenize(text):
    word_list=[] # list containing lemmatized important words
    nonstopwords=[]
    tokens=word_tokenize(text) # tokenize all words in the text
    for word in tokens:
        if word.strip().lower() not in stop_words: # check if the word is a stop word 
            nonstopwords.append(word)
    lemmatizer = WordNetLemmatizer() # initiate lemmatizer object
    for word in nonstopwords:  # only lemmatize the word if it is not a stop word
        word_list.append(lemmatizer.lemmatize(word).lower()) # lemmatize each word and add it to the word list

    corpus=Counter(word_list) # count the number of times each word appears
    ordered_corpus = sorted(corpus,key=corpus.get,reverse=True)[:1000] # sort the list into an ordered format from most common to least common words
    onehot_dict = {w:i+1 for i,w in enumerate(ordered_corpus)} # create an ordered dictionary of most common words that are one-hot encoded

    return onehot_dict
