import random

def sort_password():
    arquivo = open("word_list.txt","r")
    words = []

    for word in arquivo:
        words.append(word.strip())

    arquivo.close()

    index_words = random.randrange(0,len(words))
    word_selected = words[index_words]

    return word_selected