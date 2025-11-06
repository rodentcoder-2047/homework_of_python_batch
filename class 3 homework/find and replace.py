#programme to select and replace new word

print("Write the sentence")
Sentence =  input(">")
print("what word do you want to replace")
old_word = input(">")
print("What is the new word")
new_word = input(">")
new_sentence = Sentence.replace(old_word,new_word) 
print(new_sentence)               