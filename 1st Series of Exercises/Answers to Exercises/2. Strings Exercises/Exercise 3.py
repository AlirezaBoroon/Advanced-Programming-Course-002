print("Please enter your text:")
the_text= input()
nofwords= the_text.split()
print("The number of words in the text is:", len(nofwords))
nofsentences= the_text.count(".")
print("The number of sentences in the text is:", nofsentences)
# or we can use:
#count = 0
#for i in the_text:
#    if i == ".":
#        count = count + 1
nofvowels= the_text.count("a")+ the_text.count("A")+ the_text.count("e")+ the_text.count("E")+ the_text.count("i")+ the_text.count("I")+ the_text.count("o")+ the_text.count("O")+ the_text.count("u")+ the_text.count("U")
print("The number of vowels in your text is:", nofvowels)
# or we can use:
#count = 0
#for i in the_text:
#    if i == "a" or i == "A" or i == "e" or i == "E" or i == "o" or i == "O" or i== "i" or i== "I" or i == "u" or i == "U":
#        count = count + 1
print("Please enter a word for finding:")
the_word= input()
result= the_text.find(the_word)
if result!= -1:
    print("The word is in the text.")
else:
    print("The word is not in the text.")
## find function returns -1 if the word isn't in the text.
