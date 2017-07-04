#Stars
def draw_stars(arr):
    for i in arr:
        if(isinstance(i, str) == True):
            for k in i:
                word = []
                word.append(k)
                lower = (word[0] * len(i))
                print lower.lower()
                break
        elif(isinstance(i, int) == True):
            print('*' * i)
            
#Test Cases
# x = [4, 6, 1, 3, 5, 7, 25]
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars(x)    
