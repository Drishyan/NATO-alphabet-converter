import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter:row.code for (index,row) in data.iterrows()}

word = input("Enter a word: ").upper()
letters = [letter for letter in word]
phonetic_code = [data_dict[letter] for letter in letters]
print(phonetic_code)
