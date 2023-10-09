#create a string s as DRU.
s = 'DRU'
#define a new function named anti to get the anticlockwise version of base.
def anti(s):
        r=''
        #using for loop to iterate i till the length of s.
        for i in range(len(s)):
            #create an empty string r.
            
            #using if-else statement to define the new directions of base accordingly.
            if s[i] == 'D':
                r+='R'
             
            elif s[i] == 'R':
                r+='D'

            elif s[i] == 'U':
                r+='L'
            elif s[i] == 'L':
                r+='U'
             
        return r

    #define a new function clock() to get the clockwise version of base.
def clock(s):
        r=''
        #using for loop to iterate i till the length of s.
        for i in range(len(s)):
            #create an empty string r.
            
            #using if-else statement to define the new directions of base accordingly.
            if s[i] == 'D':
                r+='L'

            elif s[i] == 'R':
                r+='U'

            elif s[i] == 'U':
                r+='R'
            elif s[i] == 'L':
                r+='D'
        return r

#define a function called final to write the given set of commands to draw the pattern given in the question.
def final(n):
#using if else statements to define the function at 1 and using recursion for subsequent values.
        if n == 1:
             return 'DRU'
       
        else:
             g= anti(final(n-1))+'D'+final(n-1)+'R'+final(n-1)+'U'+clock(final(n-1))
        return g 

    #now finally define a new function coor which will convert the above final string into coordinates as tuples.
def coor(s):
        #create an empty list l.
        l = [(1,1)]
        
        #define two variables x and y as both 1 to represent (1,1).
        x = 1
        y = 1

        #using if else statement to define the new coordinates of x and y.
        for i in range(len(s)):
            if s[i] == 'D':
                x +=1

            elif s[i] == 'U':
                x -=1

            elif s[i] == 'L':
                y -=1

            elif s[i] == 'R':
                y +=1
            
            l.append((x,y))
        return l

#take input of a number from the user.
n = int(input("enter a number: "))
print(coor(final(n)))
