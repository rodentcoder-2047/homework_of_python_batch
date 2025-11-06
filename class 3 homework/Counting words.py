#Programme to count number of words in a sentence and total number of characters excluding spacing
print("Write the sentence")
Sentence  = input(">")
Sen = Sentence.lstrip()
print("Number of words")
print(len(Sen.split()))
print("Number of characters")
print(len(Sen.replace(" ","")))

