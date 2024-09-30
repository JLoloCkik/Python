text = input()
sentences = text.split(".")
capitalized_sentences = [] 

for sentence in sentences:  
    capitalized_sentences.append(sentence.capitalize()) 

result = '. '.join(capitalized_sentences)  

print(result)
