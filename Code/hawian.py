
import sys
def checkValid(data):
    valid=['a','e','i','o','u','p','k','h','l','m','n',' ',"'",'w']
    for i in range(len(data)):
        if data[i] not in valid:
            print(data[i]+" is not a valid character.")
            return False
    return True
            
def pronounce():
    VOWELS = {
    'a': 'ah',
    'e': 'eh',
    'i': 'ee',
    'o': 'oh',
    'u': 'oo'
    }

    VOWEL_PAIRS = {
    'ai': 'eye',
    'ae': 'eye',
    'ao': 'ow',
    'au': 'ow',
    'ei': 'ay',
    'eu': 'eh-oo',
    'iu': 'ew',
    'oi': 'oyo',
    'ou': 'ow',
    'ui': 'ooey',
    'iw': 'ee-v',
    'ew': 'eh-v',
    'uw': 'oo-w',
    'ow':'oh-w'
    }
       
    flag=True
    i = 0
    retval = []
    while flag:
        data=input("Enter a word to be converted ")
        word = data.lower()
        if checkValid(word)==False:
            return
        while i < len(word):
            
                
                
            char = word[i]

            if i < len(word) - 1:
                pair = char + word[i + 1]
                part = VOWEL_PAIRS.get(pair)

                if part is None:
                    part = VOWELS.get(char)
                else:
                    i = i + 1 
            else:
                part = VOWELS.get(char)

            if part is not None and i < len(word) - 1:
                part = part + '-'

            retval.append(part or char)
            i = i + 1
    
        print(''.join(retval))
        again=input("Would you like to go again?")
        if again=="yes" or again=="y":
            continue
        else:
            flag=False
             
        
