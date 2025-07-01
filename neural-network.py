from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import pandas as pd
import tensorflow as tf

text='This is a test set of text data - only used for testing purposes only. Abandonments are not only abbreviating the absentmindedness.'
stop_words=set(stopwords.words('english'))

def tokenize(data):
    tokenized=[] # list containing lemmatized phrases
    for item in data:
        word_list=[]
        nonstopwords=[]
        tokens=word_tokenize(item) # tokenize all words in the phrase
        for word in tokens:
            if word.strip().lower() not in stop_words: # check if the word is a stop word 
                nonstopwords.append(word)
        lemmatizer = WordNetLemmatizer() # initiate lemmatizer object
        for word in nonstopwords:  # only lemmatize the word if it is not a stop word
            word=lemmatizer.lemmatize(word).lower() # lemmatize each word
            word_list.append('{:10}'.format(word))  # pad each word to a certain length (max 12 characters) and add to word list
        # padding is necessary as the RNN model needs items with a uniform length to iterate through
        tokenized.append(word_list)
    return tokenized

df = pd.read_csv("dialogs.txt", sep='\t', header=None, names=["prompt", "response"])
prompts = df['prompt'].astype(str).tolist()
responses = df['response'].astype(str).tolist()

encoder=tokenize(prompts)
decoder=tokenize(responses)

def create_dataset(encoder, decoder):
    batch_size = 64
    buffer_size = 1000
    dataset = tf.data.Dataset.from_tensor_slices(
        {
            'encoder_input': encoder,
            'decoder_input': decoder
        },
    )
    dataset = dataset.shuffle(buffer_size).batch(batch_size)
    return dataset
