

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv") #read data
print(data)
#prints:
#  letter      code
# 0       A      Alfa
# 1       B     Bravo
# 2       C   Charlie
# 3       D     Delta........... and so on. THIS IS A DATA FRAME


#Create a dictionary in this format: #To iterate through a DataFrame we use dataframe.iterrows() **
#dictionary comprehension used
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()} #letter and code are 2 headings in csv file.
# row is a fixed name which we tap into, to access anything rom the 2 headings
print(phonetic_dict)

#Create a list of the phonetic code words from a word that the user inputs.
# is_on = True
# while is_on:
#     try:
#         word = input("Enter a word: ").upper()
#         new_list = [phonetic_dict[letter] for letter in word] #list comprehension used
#     except KeyError: #catches the EXCEPTION when user enters a number instead of a letter
#         print("Only letters please")
#     else:
#         print(new_list)

#__________________________OR___________________________________________

#Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        new_list = [phonetic_dict[letter] for letter in word] #list comprehension used
    except KeyError: #catches the EXCEPTION when user enters a number instead of a letter
        print("Only letters please")
        word = input("Enter a word: ").upper()
    else:
        print(new_list)

generate_phonetic()