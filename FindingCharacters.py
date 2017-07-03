#Finding Characters
word_list = ['hello','world','my','name','is','Anna']
char = 'o'

def find_characters(listOfWords, characters):
    newList = []
    for i in listOfWords:
        if char in i:
            newList.append(i)

    print newList

find_characters(word_list, char)