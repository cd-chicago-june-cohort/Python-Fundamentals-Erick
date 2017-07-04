import random

def coin_tosses(numOfTosses):
    headCounter = 0
    tailCounter = 0
    print('Starting the program...')
    for i in range(1, numOfTosses + 1):
        randomNum = random.randint(0,1)
        if(randomNum == 1):
            headCounter += 1
            print('Attempt #' + str(i) + ': Throwing a coin... Its a head! ... Got ' +  str(headCounter) + ' head(s) so far and ' + str(tailCounter) + ' tail(s) so far')
        if(randomNum == 0):
            tailCounter += 1
            print('Attempt #' + str(i) + ': Throwing a coin... Its a tail! ... Got ' +  str(tailCounter) + ' tail(s) so far and ' + str(headCounter) + ' head(s) so far')
    print('Ending the program, thank you!')

coin_tosses(5000)