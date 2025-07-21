vowels = 0
consoants = 0
word = input("Enter a word: ")
word = list(word.lower())
for letter in word:
    if letter in 'aeiou':
        vowels+= 1
    else:
        consoants+= 1
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consoants}")