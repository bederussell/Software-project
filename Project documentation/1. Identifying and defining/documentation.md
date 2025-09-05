Testing...
# Identifying and Defining
### Requirements
##### Functional Requirements
- User can input a string of text and the model will use Natural Language Processing to breakdown and understand the text so it can predict an output.
- The model will predict the best response to the inputted text and generate a response that satisfies the most accuracy and least error, based on the training data.
- The model can (hopefully) sustain a somewhat intelligable conversation with the user, or at least generate a prediction of each text input, expressed in natural language

##### Non-functional Requirements
- The model can generate a response in less than 10 seconds
- The model can handle inputs of full sentences
- The model can handle colloquial language, including words with contractions and spelling errors

### Mind map of ideas
 ![IMG_7686](https://github.com/user-attachments/assets/cc6f3507-78c4-4064-8120-73d5858fd8cd)

### Data Structures and Data Types
In order to manage/maintain the large amount of text data needed to train the ML model, there are two different ways I can structure the storage of the data to ensure maximum efficiency of the program.

1. Two dimensional array: after downloading a large set of text data into a CSV file into my project, a reasonable way to implement the data into my program would be by storing the data into a 2D array consisting of every line/sentence being split into an individual object in an array, and then storing each word in that line or sentence into a nested object within the particular sentence index. This could be achieved through Python's list data type, which allows for 2D arrays to be created with ease and stored in a row/column type format where each object in the outside list is another list of words (in the context of a large file of text data, each row would represent a singular sentence in the text data, and each column would represent a singular word in that sentence). An advantage of using Python lists to store the training data is that lists automatically order all of its data, with each object having a sequential index that the Python interpreter recognises. This is effective as I plan on using a Recurrent Neural Network for my model, which is an ML model designed to process ordered data, meaning a list with pre-prepared object indexes will make it easier for the model to train itself as sentence/word structure will be numerically categorised and the program will be easier to chronologically iterate through all words of the text file. Additionally, a 2D array is very easy to navigate and will ensure that the readability of the training data will remain organised and easy to access throughout the training of the model.
 
2. Python dictionary/hash map: Another necessary way of storing the text training data is to format the data into a Python dictionary, allowing the text to be one-hot encoded and vocabulary mapped. Vocabulary mapping is the process of assigning raw text data into numerical representations that an ML model can process and draw relationships from, which is an essential step to text processing for an ML chatbot. A python dictionary would be effective for this method of data storage as a dictionary stores data in key:value pairs that significantly reduces RAM and processing power to locate important data, creating an efficient environment for the model to process training data and for me to manage the data storage.


### Data Dictionary of Global Data

|Data Item|Data Type|Data Format|Description|Example|
|----|----|----|----|----|
|df|Data Frame|[Column1 \t Column 2]|A two-dimensional table read file consisting of prompts in one column, and responses in another, each seperated by a tab \t|Hi, how are you doing today?      I'm doing great.|
|prompts|Python List|[x, y, z, ...]|A Python list including all the prompts of the text file, gathered and seperated by the first column.|['Hi, how are you doing?', 'I need help.']|
|responses|Python List|[x, y, z, ...]|A Python list including all the responses of the text file, gathered and seperated by the second column.|['I'm doing great.', 'How can I help you?']|
|encoder|2D Array|[[a, b, c], [x, y, z], ...]|A 2D array  where each item is another array of all tokenized, lemmatized words from each prompt in the 'prompts' list, all at a uniform length of 10 characters (through padding).|[['Hi        ', 'how       ', 'you       ', 'doing?    '], ['I         ', 'need      ', 'help      ']]|
|decoder|2D array|[[a, b, c], [x, y, z], ...]|A 2D array  where each item is another array of all tokenized, lemmatized words from each response in the 'reponses' list, all at a uniform length of 10 characters (through padding)|[['I'm       ', 'doing     ', 'great     '], ['How       ', 'can       ', 'help      ', 'you?      ']]|


### Implementation Methods
Suppose my new AI model is replacing another, older software model that the client is currently using. The old model was designed to predict the sentiment (good or bad) of a movie/book/show review, based on the way the reviewer described the piece of media (for example, if the review contained words such as 'forgettable', 'boring', 'unrealistic', then the model would predict the sentiment to be bad, and vice versa). The old model was trained strictly on movie review datasets, meaning it is useless in contexts outside of media reviews. However, the client now wants a model that is more versatile, being applicable to more broad contexts such as conversations, question answering, and predictions (the purpose of my new model). Below is a description of how each implementation method would work with this transition from the older model to my new project model.

##### Direct
Direct implementation is the process of completely deploying the new model and replacing the old model in one single step. In the context of my project, this method would somewhat work, as the new model relies on completely different data and serves a different purpose. Direct implementation would also work with my project as there is no awkward transition phase between the two models; the transition would be seamless for the client and instant. However, this method of implementation could be ineffective as the process would be heavily resource and time costly, as the developers would need to build and train a completely seperate ML model on different datasets whilst also simulataneously maintaining and keeping the old model running. The transition would also be risky as a complete turnover to the new model means there is no fallback option if the new model is unsuccessful.

##### Phased
Phased implementation is the process of gradually implementing aspects of the new model into the old model, allowing for a smooth transition. Phased implementation could somewhat work for my project as it allows the client a period of time to slowly familiarise themselves with the new model whilst it is slowly being deployed, allowing for better testing and less risk during the rollover of models. However, this method of implementation could also be ineffective as a lot of the process would be unnecessary; with the two different models serving two different purposes, the upkeep and maintenance required during the phases of installation would be a waste of time and cost. It would most likely be more effective to both the developers and the client to choose a different implementation method in the context of my project.

##### Parallel
Parallel implementation is the process of simultaneously running both the old and new model next to each other in order to compare and contrast the benefits and disadvantages of each. Parallel implementation would work very well for my project as it provides a time where the client can use both models to test and evaluate the effectiveness of the new model and what needs to be changed. Parallel implementation is also less risky than direct, as if the new model is unsuccessful, there is still a failsafe old model to fall back on. However, parallel implementation can be costly in terms of time and effort as developers are required to run two seperate models simultaneously.

##### Pilot
Pilot implementation is the process of deploying the new model to a small number of users in a controlled environment in order to maximise testing and evaluating before full deployment. This method would work well for my project because it allows for effective testing and provides developers with a chance to prototype solutions before having to commit to a full release. Additionally, pilot implementation holds little to no risk as the old model is still active whilst testing of the new model is being conducted, and only benefits can come from the pilot testing stage if it is conducted in a sandboxed environment whilst the old model is still online.

Overall, I think a mix between parallel and pilot implementation would work best for my project, because there is a lot of risk in rolling over a new ML model trained on completely different data as training and building new models is expensive and time consuming. Both parallel and pilot implementation eliminate risk by having failsafe options to fall back on if the new model is unsuccessful. Pilot and parallel implementation also brings benefits to the client, as they allow the client to compare and contrast the two models whilst both are active, which would be very effective in the context of an AI model trained on a large dataset.
