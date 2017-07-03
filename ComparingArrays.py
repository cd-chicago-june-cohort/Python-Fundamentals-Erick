# Uncomment the test case you want to use 
# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]

# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]

# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']


def compare_arrays(arr1, arr2):
    list1 = False
    list2 = False
    if(len(arr1) == len(arr2)):
        for i in range(0, len(arr1)):
            if(arr1[i] == arr2[i]):
                list1 = True
            else:
                list2 = True
    else:
        print('The list are not the same.')
    if(list1 == True and list2 == False):
        print('The list are the same.')
    elif(list1 == True and list2 == True):
        print('The list are not the same.')    
    
compare_arrays(list_one, list_two)
    