import re

##text= open("word.txt",'r')
##
###(cat)|(dog)
####for line in text:
####    print(line)
####x=re.findall("dog",text)
####print(x)
##
##agentFour=re.compile("r'\b\w{4}\b'")
##agentFour.findall(r'\b\w{4}\b',text)


text= open("word.txt",'r')
total = len(re.findall(r'\b\w{4}\b',text))
print (total)

\b(\w+ing)\b|\b(\w+ion)\b

\b\w*q(?!u)\w*\b    q question


