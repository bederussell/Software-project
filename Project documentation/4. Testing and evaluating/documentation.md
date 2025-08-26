# Testing & Evaluating
### Methodologies to test and evaluate code
##### Desk Check

##### Test Data
Below is test data for the 'autocomplete' function in my program. The different cases are testing different lengths of input 'seeds', and comparing the expected output of 'hi how are you' with what the program actually returns. Because words are predicted based on the last two words of the input (n1 and n2), the table shows what happens with each possibility of n1 and/or n2 being either blank or populated. 

![IMG_8172](https://github.com/user-attachments/assets/58756784-babd-4e06-a1cf-ad9f8ea0af7e)

As seen in the table, errors are visible when the length of the input is less than or equal to one, because there is not enough data to assign the n1/n2 variables to. I attempted to counter this error before testing by adding these lines of code at the beginning of the function:

![code](https://github.com/user-attachments/assets/2e714d14-912e-4551-8894-e75ad7bd02c0)

However it seems that inserting an empty string into the 0 index of the 'words' list (the user's string input split into a list) does not work, potentially because of the 'predict_next's function's inability to handle an empty string as the n1 or n2 variable.

The way that I fixed this bug was by instead of inserting an empty string as the first index of the 'words' list (when len(words) is less than 2), I changed the code so that the word inserted was a duplicate of the word that was inputted i.e. the 0 index of the 'words' list:

![code2](https://github.com/user-attachments/assets/1e0f7ab3-f2a9-4925-8534-1a4fb3bd0ce3)

Additionally, I added this code to the end of the function that deletes the 0 index of the 'words' list (the duplicated word) so it isn't printed to the user that the word was duplicated:

![code3](https://github.com/user-attachments/assets/78fbbd45-3b4d-444f-9103-c88eb0994534)

Now here in effect:

![terminal](https://github.com/user-attachments/assets/04ed7f7b-b544-460e-82c9-af2705555139)

As for when the user inputs an empty string (ie with no indexes), I added this while loop to ensure that the user has to input a string of at least one word (the 'strip()' function ensures that a series of whitespaces cannot be inputted) in order for the program to continue running:

![code4](https://github.com/user-attachments/assets/254f1d7a-71c0-44be-8304-a55ff083d872)

### Code Optimisation Techniques
Something I noticed whilst testing my program was that anytime I tried to run the program it would take about 10-15 seconds before the option to input a seed was shown to the user. In order to find why this was happening, I used Python's built-in time library to locate which part of the code would take so long. During the 'run' function, I implemented the time() function between every process and printed in the terminal how long every line of code would take:

![code5](https://github.com/user-attachments/assets/93ad100a-03da-4fda-900a-5e62f8f2b04f)
![terminal2](https://github.com/user-attachments/assets/7a55e13c-7871-4f95-a8b7-bb75b723b25d)

As you can see, the bulk of the time taken to start the program is **tokenizing the text file contents** into the 'tokens' list. In order to optimise this process and cut the time down, I used the Python pickles library to cache the tokens list locally so it can be retrieved instantly, instead of having to tokenize the entire file everytime I run the program.
First I ran this code to locally cache the tokenized list as a file:

![pickle](https://github.com/user-attachments/assets/23cc28df-975e-4659-aab1-99c5ccfcc6cd)

After the list is cached, this code now retrieves the file almost instantaneously from local storage:

![pickle2](https://github.com/user-attachments/assets/82fb5588-d181-4d0b-b923-c74e3524e4a7)

And as you can see, the time taken to tokenize the text file is cut down from ~10 seconds to virtually nothing: 

![terminal3](https://github.com/user-attachments/assets/ac2843ab-4aef-4dd6-8836-322338bb05c4)


### Evaluate effectiveness of software solution
