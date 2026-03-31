import re

words=['dark','very','fast','long']

with open("repetitive_words_para.txt","r") as f:
    content=f.read()

for word in words:
    word_to_replace=rf"\b{word}\b"
    replacing_word='#' * len(word)
    content=re.sub(word_to_replace,replacing_word,content,flags=re.IGNORECASE)

with open("repetitive_words_para.txt","w") as f:
    f.write(content)

"""
(word_to_replace,replacing_word,content,flags=re.IGNORECASE)

 which word need to be replaced , with what it is replaced, where to find the word location which
 needs to be replaced and lastly character sensitivity

"""