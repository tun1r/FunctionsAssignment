'''Write a function SwapChar that accepts a string as a parameter. It then swaps all the odd indexed consonant characters with a random vowel. Write the main program to invoke this function.

Ex: original string, s = ‘red string’
Modified string, s = ‘redasirino’
'''
import random
def SwapChar(s):
    s=s.lower()
    new_string=''
    vowel=['a','e','i','o','u']
    for i in range(len(s)):
        if i%2==0:
            new_string+=s[i]
        else:
            if s[i] not in 'aeiou':
                new_string+= vowel[random.randint(0,4)]
            else:
                new_string+=s[i]
    return new_string
old_string=input("Enter string.")
print(SwapChar(old_string))
            
            
    
