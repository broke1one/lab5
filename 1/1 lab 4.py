word = str(input("Enter a word: "))
word = word.upper()
result = 0
score_1 = "AEIOULNSTR"
score_2 = "DG"
score_3 = "BCMP"
score_4 = "FHVWY"
score_5 = "K"
score_6 = "JX"
score_10 = "QZ"
for i in word:
    if i in score_1:
        result += 1
    elif i in score_2:
        result +=2
    elif i in score_3:
        result += 3
    elif i in score_4:
        result += 4
    elif i in score_5:
        result += 5
    elif i in score_6:
        result += 6
    elif i in score_10:
        result += 10
    else:
        pass
print(result)