# Python program to demonstrate
# string slicing

# String slicing as 's'


def Convert(s):
    li = list(s.split(" "))
    return li

    
s = (input("entrer a word: "))

#First condition
'''
if input string is less than 3 characters long,
 return a list with input string as the only element.
'''
if len(s)< 3:

    print (Convert(s))
else:
    #otherwise, return list with all string slices greater than 1 character long
     print( Convert(s[:2]), Convert(s[:3]), Convert(s[1:]) )

     print( Convert(s[:2]), Convert(s[:3]), Convert(s[0:4]), Convert(s[0:]), Convert(s[1:3] ), Convert(s[1:4] ), Convert(s[1:5] ), Convert(s[2:4]),  Convert(s[2:4]),  Convert(s[2:]),  Convert(s[3:]) )

     #print(s[:2],s[:3]).split('')

