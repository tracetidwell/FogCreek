# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 17:05:20 2016

@author: Trace
"""

# Import the necessary packages: Pandas for the DataFrame and Counter to count
# the occurence of each digit in the text
import pandas as pd
from collections import Counter

# I created a text file with the text to be searched. 
# Open the file, read the lines to the variable 'text' and then close it.
text_file = open('Documents/text.txt', "r")
text = text_file.read()
text_file.close()

# The string of characters to be counted.
string = 'abcdefghijklmnopqrstuvwxyz_'

# The built-in counter function counts every instance of every character passed to it.
# Pass the complete text file, and it does all the work.
counter = Counter(text)

# Create a DataFrame to hold each character and it's count in the text
order = pd.DataFrame(index = range(0,len(string)), columns = ['Character', 'Count'])

# Loop through the string and counter variables.
for i, s in enumerate(string):
    # Assigns the character from the string.
    order.iloc[i,0] = s
    # Assigns the chracter's respective count from the counter.
    order.iloc[i,1] = counter[s]
    
# Sort the DataFrame by Count, descending.
order = order.sort_values(['Count'], ascending=False)

# Set the newly sorted characters to the original string variable.
string = ''.join(order.Character.values)

# Create a substring by finding the index of the '_' and removing it and everything that follows.
string = string[:string.index('_')]

#Print the new value of our string - unprovable
print(string)