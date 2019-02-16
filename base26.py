import sys

#The convertTo method takes one parameter x and is the input integer that will be converted to a base26 number
def convertTo(x):
    num = x
    result = []
    string = ""
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    #While loop to convert the last one or two digits from the input integer into the base 26 equivalent
    while num >= 0:
        last2 = num%100
        #convert the last digit to base26
        if last2 > 25:
            temp = last2%10
            result.append(alpha[temp])
            num = num//10
            if num == 0:    #if we set num to 0 above
                num = -1    #make loop halt
        #convert the last two digits to base26
        else:
            result.append(alpha[last2])
            num = num//100
            if num == 0:    #if we set num to 0 above
                num = -1    #make loop halt
    #while the result is not empty we append the last element of result to string and remove the last element from result
    while result != []:
        string += result[-1]
        del result[-1]
    #print output
    print(string)

def convertFrom(x):
    inpt = x.lower()
    result = []
    string = ""
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    num = list(inpt)
    for i in num:
        if i not in alpha:
            sys.exit("Illegal input. input can only contain characters a-z")
        temp=ord(i)
        temp -= 97
        string += str(temp)
    print(string)




def main():
    if len(sys.argv) == 3:
        input1 = eval(sys.argv[1])
        try:
            input2 = int(sys.argv[2])
        except:
            try:
                input2 = str(sys.argv[2])
            except:
                sys.exit("There was an error with your input number") 
    else:
        sys.exit("Incorrect number of arguments given. must be given as: python base26.py mode number")
    try:
        mode = int(input1)
    except:
        sys.exit("Invalid mode. Must be either (1) to convert to alpha or (2) to convert from alpha")
    
    if mode == 1:   #convert to
        try:
            num = int(input2)
        except:
            sys.exit("Invalid number. Must be of type int in order to convert to alpha")
        
        if num >= 0:
            convertTo(num)
        else:
            print(type(input2))
            sys.exit("Invalid number. Must be an integer greater than or equal to 0")

    elif mode == 2:   #convert from
        try:
            num = str(input2)
            convertFrom(num)
        except:
            sys.exit("Invalid number. Must be of type str in order to convert to alpha")

        
        
        

main()
