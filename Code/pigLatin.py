def findFirstVowel(s):
    for i in range(len(s)):
        if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
            return i
    else:
        return -1

def convertToPigLatin(s):
    index=findFirstVowel(s)
    retval=""
    if index>=1:
        s=s[index:]+s[0:index]+"ay"
    if index==0:
        s=s[1:]+s[0:1]+"way"
    return s

def reverse(s):
    retval=""
    for x in range(len(s)-1,-1,-1):
        retval=retval+s[x]
    return retval
        
        
def main():
    while(True):
        text=input("Enter a word to see pig latin and reversed")
        if text=="done":
            break
        else:
            print("Pig Latin: "+convertToPigLatin(text.lower()))
            print("Reversed: "+reverse(text.lower()))
        
        
        
        
