import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import defaultdict

stop_words=set(stopwords.words('english')) # not used in this program

def tokenize1(data): # unimportant, will delete later
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
        self.bigrams=defaultdict(list) # a dictionary consisting of two word pairs that are linked together
        self.trigrams=defaultdict(list) #  a dictionary consisting of three word groups that are linked together
        self.build_model(tokens)

    def build_model(self, tokens): # for each word in the training data, assign variables to the next two words in order to create bigrams and trigrams of these words
        for i in range(len(tokens)-2):
            n1, n2, n3 = tokens[i], tokens[i+1], tokens[i+2]  
            self.bigrams[n1].append(n2)
            self.trigrams[n1, n2].append(n3)
    
    def predict_next(self, n1, n2, top_k=3):  ###### n2=None  # locates the neighbours of a word through trigrams and bigrams - trigrams are prioritised as they are more specific, but if no trigrams are found then a bigram is found. If no bigram is found, then nothing is returned
        candidates=[]
        if n2 and (n1, n2) in self.trigrams:
            candidates=self.trigrams[(n1, n2)]
        elif n1 in self.bigrams:
            candidates=self.bigrams[n1]   

        if not candidates:
            return None
        
        freq=nltk.FreqDist(candidates)  # orders the most common common neighbours of the words from highest to lowest in a freqdist table
        ret=[word for word, i in freq.most_common(top_k)]
        print(ret)
        return ret
    
    def autocomplete(self, seed, num_words):  ### num_words=10  # calls the 'predict_next' function on the last two words of the prompt, finding the nearest nieghbours and adding them to the end of the prompt, repeating this for the number of words the user wants to be predicted
        words=seed.lower().split()
        
        if len(words) < 2:
            words.insert(0, "")  # this is currently bugged

        n1, n2 = words[-2], words[-1]  # last two words of the prompt

        for i in range(num_words):
            next_candidates = self.predict_next(n1, n2, top_k=1)  # find the nearest neighbours for the last two words and repeat for the length of predicted response
            if not next_candidates:
                break
            next_word = next_candidates[0]
            words.append(next_word)
            n1, n2 = n2, next_word

        return " ".join(words)

def run():
    with open('en_twitter.txt', 'r', errors='ignore') as file:
        lines = file.readlines()
        file_content = ''.join(lines)
    
    tokens=tokenize2(file_content)

    autocomplete_model=autocomplete(tokens)

     while True:
        seed=input("\nEnter a prompt (or 'quit' to exit): ").strip()
        
        if seed.lower() == "quit":
            break

        numwords=int(input('Length of autocomplete response: '))

        print("\nDid you mean -")
        print(autocomplete_model.autocomplete(seed, numwords)) 

if __name__ == '__main__':
    print()
    print('--- Please be patient while the program loads ---')
    run()
