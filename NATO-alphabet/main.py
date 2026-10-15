import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter:row.code for (index,row) in data.iterrows()}

while True:
    word = input("Enter a word: ").upper()
    try:
        letters = [letter for letter in word]
        phonetic_code = [data_dict[letter] for letter in letters]

    except KeyError:
        print("Please enter valid letters")
        continue
    else:
        print(phonetic_code)
        break
