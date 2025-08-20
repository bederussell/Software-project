import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import defaultdict

stop_words=set(stopwords.words('english')) # not used in this program (from previous program attempt)

def tokenize1(data): # unimportant, will delete later (from previous program attempt)
    tokenized=[] # list containing lemmatized phrases
    lemmatizer=WordNetLemmatizer()
    sentence=data.split('.') # split the input data into a list, seperated by each sentence
    for item in sentence:
        word_list=[]
        nonstopwords=[]
        tokens=word_tokenize(item) # tokenize all words in the phrase
        for word in tokens:
            if word.strip().lower() not in stop_words: # check if the word is a stop word 
                word=lemmatizer.lemmatize(word)
                nonstopwords.append(word)
        for word in nonstopwords:  
            word_list.append('{:10}'.format(word))  # pad each word to a certain length (max 12 characters) and add to word list
        tokenized.append(word_list)
    return tokenized

def tokenize2(data): # new tokenize function
    tokenized=[] # list containing phrases
    sentence=data.split('.') # split the input data into a list, seperated by each sentence
    for item in sentence:
        tokens=word_tokenize(item) # tokenize all words in the phrase
        for word in tokens:
            if not word == '!':
                tokenized.append(word.lower().strip())
    return tokenized

class autocomplete:  # autocomplete object that contains the subroutines to autocomplete an input
    def __init__(self, tokens):
        self.bigrams = defaultdict(list) # bigrams are a dictionary consisting of two word pairs that are linked together
        self.trigrams = defaultdict(list) # trigrams are a dictionary consisting of three word groups that are linked together
        self.build_model(tokens)

    def build_model(self, tokens): # for each word in the training data, assign variables to the next two words in order to create bigrams and trigrams of these words
        for i in range(len(tokens)-2):
            n1, n2, n3=tokens[i], tokens[i+1], tokens[i+2]  
            self.bigrams[n1].append(n2)
            self.trigrams[n1, n2].append(n3)
