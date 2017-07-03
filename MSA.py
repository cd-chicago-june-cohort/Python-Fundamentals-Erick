#Multiples
# Part 1 - Loop That prints Only Odds
for i in range(1, 1000):
    if (i%2 == 0):
        continue
    else:
        print i

#Part 2 - Prints all multipes of 5 from 5 to 1,000,000
for i in range(5, 1000000):
    if(i%5 == 0):
        print i

#Sum List
sum = 0
a = [1, 2, 5, 10, 255, 3]
for i in a:
    sum+= i
print sum

#Average List
sum = 0
a = [1, 2, 5, 10, 255, 3]
for i in a:
    sum += i
print sum / len(a)