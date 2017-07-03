#Type List 

def type_list(words):
    newString = 'Welcome to '
    newSum = 23
    word = False
    number = False
    for i in words:
        if(isinstance(i, str) == True):
            newString += i
            word = True
        elif(isinstance(i, int) == True):
            newSum += i
            number = True
        elif(isinstance(i, float) == True):
            newSum += i
    if(word == True and number == True):
        print("The array you entered is of mixed type")
        print ('String: ') + newString
        print ('Sum: ') + str(newSum)
        print '-' * 50
    elif(word == True):
        print("The array you entered is of string type")
        print ('String: ') + newString
        print '-' * 50
    elif(number == True):
        print("The array you entered is of integer type")
        print ('Sum: ') + str(newSum)
        print '-' * 50

l = ['magical unicorns ',19,'hello ',98.98,'world ']
m = ['magical','unicorns']
n = [2,3,1,7,4,12]

#Testing list with different data types
type_list(l)
type_list(m)
type_list(n)

