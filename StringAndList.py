#Find And Replace
words = "It's thanksgiving day. It's my birthday,too!"

print words.find('day')

newWords = "It's thanksgiving day. It's my birthday,too!"
print newWords.replace('day', 'month')

#Min And Max
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

#First And Last
x = ["hello",2,54,-2,7,12,98,"world"]
first = x[0]
print first
index = len(x) - 1
last = x[index]
print last
newList = [first, last]
print newList

#New List
y = []
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x

firstHalf = x[:len(x)/2] 
SecondHalf = x[len(x)/2:]

SecondHalf.insert(0,firstHalf)
print SecondHalf