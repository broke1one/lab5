word = input(str("Enter a word: "))
word = word.lower()
vowels = "aeioyu"
consonants = "bcdfghjklmnpqrstvwxyz"
wordsvowels = ""
count_vowels = 0
count_consonants = 0
word_count = 0
for i in word:
    if i.isalpha():
        if i in vowels:
            count_vowels += 1
            wordsvowels += i
        elif i == " ":
            pass
        elif i in consonants:
            count_consonants += 1
        else:
            pass
    
if count_consonants == count_vowels:
    print(wordsvowels)
else:
    print(f"there is {count_vowels} vowels and {count_consonants} consonants")

