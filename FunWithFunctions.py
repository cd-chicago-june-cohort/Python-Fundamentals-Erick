#Odd/Even
def odd_even():
    for i in range(1, 2001):
        if(i%2 == 0):
            print('Number is ' + str(i) + '.' + '    This is an even number.')
        else:
            print('Number is ' + str(i) + '.' + '    This is an odd number.')

odd_even()

#Multiply
def multiply(listOfNumbers, x):
    newlist = []
    for i in listOfNumbers:
        newlist.append(i*x)
    return newlist

a = [2,4,10,16]
multiple = multiply(a, 5)
print multiple

#Hacker Challenge
def layered_multiples(arr):
    new_array = []
    for i in arr:
        new_array.append('1' * i)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x