# This Is Jeopardy!

This is a codeacademy project where create several functions to investigate dataset of Jeopardy! questions and answers.  Filter the dataset for topics interested in, compute average difficulty of those questions, and train to become the next Jeopardy champion.

Project occurs as follows:
- Load data from 'Jeopardy.csv' containing data about Jeopardy! and investigate its content.
- Create way to filter dataset for questions that contains all words in list of words.  
- Test this way with few different sets of words to see if function breaks.  Consider capitalization and don't find rows where contains substrings of given words.
- Create function to compute aggregate stats like .mean() on "Value" column.  But first, need to convert that column to floats.  
- Write function so returns count of unique answers to all questions in dataset.
- Investigate how questions change over time by filtering the date.  

What to expand to this are as follows:
- Find the difficulty of certain topics such as average value of questions.
- Consider whether there is a connection between the round and the category?  Are you more likely to find certain categories, like "Literature" in Single Jeopardy or Double Jeopardy?
- Build a system to quiz yourself. Grab random questions, and use the input function to get a response from the user. Check to see if that response was right or wrong. 
