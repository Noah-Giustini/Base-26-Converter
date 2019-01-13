import sys
import math

def convertTo(x):
    num = x
    result = []
    string = ""
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    while num >= 0:
        last2 = num%100
        if last2 > 25:
            temp = last2%10
            result.append(alpha[temp])
            num = num//10
            if num == 0:    #if we set num to 0 above
                num = -1    #make loop halt
        else:
            result.append(alpha[last2])
            num = num//100
            if num == 0:    #if we set num to 0 above
                num = -1    #make loop halt
    while result != []:
        string += result[-1]
        del result[-1]
    print(string)


def main():
    if len(sys.argv) == 3:
        input1 = eval(sys.argv[1])
        input2 = eval(sys.argv[2])
    else:
        sys.exit("Incorrect number of arguments given. must be given as: python base26.py mode number")
    try:
        mode = int(input1)
    except:
        sys.exit("Invalid mode. Must be either (1) to convert to alpha or (2) to convert from alpha")
    
    if mode == 1:   #convert to
        try:
            num = input2
        except:
            sys.exit("Invalid number. Must be of type int in order to convert to alpha")
        
        if num >= 0:
            convertTo(num)
        else:
            print(type(input2))
            sys.exit("Invalid number. Must be an integer greater than or equal to 0")

    elif mode == 2:   #convert to
        try:
            num = str(input2)
            print(mode)
            print(num)
        except:
            sys.exit("Invalid number. Must be of type str in order to convert to alpha")

        
        
        

main()
