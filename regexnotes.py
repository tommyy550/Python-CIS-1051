import re


text= "Agent Alice gave the secret documents to Agent bob."
agentRegex = re.compile("Agent [A-Z][a-z]*")
mo=agentRegex.search(text)
print(mo,mo.group())

for match in agentRegex.findall(text):
    print(match)

newText=agentRegex.sub('BLACK_HIGHLIGHTER',text)
print(newText) #replace whatever in regex with black highliter


###test question
#import re
text=open("ssn.txt",'r')
output=open("ssnRemoved.txt",'w')
ssnRegex=re.compile(r"\d\d\d-\d\d-\d\d\d\d")    #how to create a regex

for line in text:
    newline= ssnRegex.sub("REDACTED",line)
    output.write(newline)
output.close()
    
