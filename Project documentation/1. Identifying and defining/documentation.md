# Identifying and Defining
### Requirements
##### Functional Requirements
- User can input a string of text and the model will use Natural Language Processing to breakdown and understand the text so it can predict an output.
- The model will predict the best response to the inputted text and generate a response that satisfies the most accuracy and least error, based on the training data.
- The model can (hopefully) sustain a somewhat intelligable conversation with the user, or at least generate a prediction of each text input, expressed in natural language

##### Non-functional Requirements
- The model can generate a response in less than 10 seconds
- The model can handle an input of up to 500 tokens
- The model can handle colloquial language, including words with contractions and spelling errors

### Mind map of ideas
 ![IMG_7686](https://github.com/user-attachments/assets/cc6f3507-78c4-4064-8120-73d5858fd8cd)

### Data Structures and Data Types

### Data Dictionary of Global Data

### Implementation Methods
Suppose my new AI model is replacing another, older software model that the client is currently using. The old model was designed to predict the sentiment (good or bad) of a movie/book/show review, based on the way the reviewer described the piece of media (for example, if the review contained words such as 'forgettable', 'boring', 'unrealistic', then the model would predict the sentiment to be bad, and vice versa). The old model was trained strictly on movie review datasets, meaning it is useless in contexts outside of media reviews. However, the client now wants a model that is more versatile, being applicable to more broad contexts such as conversations, question answering, and predictions (the purpose of my new model). Below is a description of how each implementation method would work with this transition from the older model to my new project model.

##### Direct
Direct implementation is the process of completely deploying the new model and replacing the old model in one single step. In the context of my project, this method would somewhat work, as the new model needs to be trained on a larger quantity of data, or a completely different selection of data entirely. Direct implementation would also work with my project as there is no awkward transition phase between the two models; the transition would be seamless for the client and very user-friendly. However, this method of implementation could be ineffective as the process would be heavily resource and time costly, as the developers would need to build and train a completely seperate ML model on different datasets whilst also simulataneously maintaining and keeping the old model running. The transition would also be risky as a complete turnover to the new model means there is no fallback option if the new model is unsuccessful.

##### Phased

##### Parallel

##### Pilot
