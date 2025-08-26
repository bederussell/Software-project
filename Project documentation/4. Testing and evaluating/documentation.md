# Testing & Evaluating
### Methodologies to test and evaluate code
##### Desk Check

##### Test Data
Below is test data for the 'autocomplete' function in my program. The different cases are testing dufferent lengths of input 'seeds', and comparing the expected output of 'hi how are you' with what the program actually returns. Because words are predicted based on the last two words of the input (n1 and n2), the table shows what happens with each possibility of n1 and/or n2 being blank or populated. 

![IMG_8172](https://github.com/user-attachments/assets/58756784-babd-4e06-a1cf-ad9f8ea0af7e)

As seen in the table, errors are visible when the length of the input is less than or equal to one, because there is not enough data to assign the n1/n2 variables to. I attempted to counter this error before testing by adding these lines of code at the beginning of the function:

![code](https://github.com/user-attachments/assets/2e714d14-912e-4551-8894-e75ad7bd02c0)

However it seems that inserting an empty string into the 0 index of the 'words' list (the user's string input split into a list) does not work, potentially because of the 'predict_next's function's inability to handle an empty string as the n1 or n2 variable.

### Evaluate effectiveness of software solution
