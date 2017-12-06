import string



fin=open("alice-in-wonderland.txt")

text = fin.read()

words = text.split(" ")



for i in range(len(words)-1):
     for c in string.whitespace:
          words[i]=words[i].replace(c,'')
     for c in string.punctuation:
          words[i]=words[i].replace(c,'')
     words[i]=words[i].lower()

for word in words:
     if len(words)==0:
          del word

print(len(words),"words found")

print(words[0])

"""
for i in range(100):
     print(words[i])
"""
