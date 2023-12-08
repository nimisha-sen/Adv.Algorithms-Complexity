This project aims to consume CVS comma-separated files which can be further worked upon to consume multiple CSV Files or multiple Txt files. Such that the program is more robust and could work on with any legal dataset.

This project first opens the provided CSV and uses a sorting algorithm to sort the rows on the basis of the length of the first row the first row is the legal doc text 2nd is the deadline and 3rd is the amount.

After the sorting, we save the new CSV with another name and open it again




Now we also utilize a job-searching algorithm which is a type of greedy algorithm which aims to select jobs which can be completed within the deadline and maximize the amount.

By selecting most profitable task first we maximize the profit from processing the legal text.

Here processing refers to us selecting the task then processing it to see how many words are there in the text which matches our array of words given by us example 

Mywordstomatch =[’legal’,’person’] etc

At the end we print how many of such words were found in each of the selected tasks 


In future:
We could instead consume doc or txt files instead.

Provide a graphically representation of matched words

Implement AI models which tell the sentiment of the docs and compare with other docs
