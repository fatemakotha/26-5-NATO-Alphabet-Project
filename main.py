

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv") #read data
print(data)
#prints:
#  letter      code
# 0       A      Alfa
# 1       B     Bravo
# 2       C   Charlie
# 3       D     Delta........... and so on. THIS IS A DATA FRAME


#TODO 1. Create a dictionary in this format: #To iterate through a DataFrame we use dataframe.iterrows() **
#dictionary comprehension used
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()} #letter and code are 2 headings in csv file.
# row is a fixed name which we tap into, to access anything rom the 2 headings
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
new_list = [phonetic_dict[letter] for letter in word] #list comprehension used
print(new_list)
