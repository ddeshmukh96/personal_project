
"""
Problem statement 5

Write a program for multiple repetitive words  to be replaced by
character '#' having length same as that of the word that is repiting.
"""

r_words=['dark','very','fast','long']

with open("repetitive_words_para.txt","r") as f:
    file_content=f.read()


for word in r_words:
    file_content=file_content.replace(word,("#"*len(word)))


with open("repetitive_words_para.txt","w") as f:
    f.write(file_content)


"""
Input str:

The dark night felt very dark, and the cold wind blew very cold. He ran fast,
faster than he ever ran before, searching for a fast way home. But the road
ahead seemed to go on forever, with no end in sight, as he realized
that the long night would only get longer.

Output:

The #### night felt #### ####, and the cold wind blew #### cold. He ran ####,
####er than he ever ran before, searching for a #### way home. But the
# road ahead seemed to go on forever, with no end in sight, as he realized
# that the #### night would only get ####er.

So, we can clearly see that the word 'faster' and 'longer'
is also replaced with '#' as '####er' and '####er'. But that
was not supoosed to be happened.

"""