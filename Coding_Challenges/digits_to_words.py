"""
Write a code to convert a given number into words

Example: n=568 becomes Five Six Eight

"""

n=int(input("Enter the number: "))

"""  Normal Approach  """
def num_to_word(n):
    num=str(n)
    print(num,type(num))
    word=" "
    for i in range(len(num)):
        if num[i]=="1":
            word=word+"One "
        elif num[i]=="2":
            word=word+"Two "
        elif num[i]=="3":
            word=word+"Three "
        elif num[i]=="4":
            word=word+"Four "
        elif num[i]=="5":
            word=word+"Five "
        elif num[i]=="6":
            word=word+"Six "
        elif num[i]=="7":
            word=word+"Seven "
        elif num[i]=="8":
            word=word+"Eight "
        elif num[i]=="9":
            word=word+"Nine "
        else:
            word=word+"Zero "
    return word

# print(num_to_word(n))


"""  Dictionary   """

def digit_to_word(n):
    num=str(n)
    word=""
    digit_word={
        "1":"One", "2":"Two", "3":"Three", "4":"Four",
        "5":"Five", "6":"Six", "7":"Seven", "8":"Eight",
        "9":"Nine","0":"Zero"}
    for digit in num:
        word=word+digit_word[digit]+" "

    return word

# print(digit_to_word(n))


"""   List lookup   """

def int_to_string(n):
    num=str(n)
    word=[]
    word_for_digit=["Zero","One","Two","Three","Four",
                    "Five","Six","Seven","Eight","Nine"]
    for digit in num:
        word.append(word_for_digit[int(digit)])

    return " ".join(word)

print(int_to_string(n))