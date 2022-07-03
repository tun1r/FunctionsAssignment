'''Write a Python function to check whether a string is a pangram or not. 
Pangrams are words or sentences containing every letter of the alphabet at least once.
Example : "The quick brown fox jumps over the lazy dog"
'''
def panagramchecker(string):
    done=[]
    string=string.lower()
    for i in string:
        if i.isalpha() and i not in done:
            done.append(i)
    if len(done)==26:
        print("It is a panagram.")
    else:
        print("It is not a panagram.")
s=input("Enter string to check if it is a panagram or not.")
panagramchecker(s)
    
