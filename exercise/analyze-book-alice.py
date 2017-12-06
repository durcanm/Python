import string


# 'alice-in-wonderland.txt'
# lines: 3736
# header_index: 20
# footer_index: 3375
# body_lines: 3355
# words: 152061


# open&read file
filename='alice-in-wonderland.txt'
fin = open(filename)
lines = fin.readlines()


# header-footer cleaning
header_text = "*** START OF THIS PROJECT GUTENBERG EBOOK ALICE'S ADVENTURES IN WONDERLAND ***"
for i in range(len(lines)-1):
     if lines[i].startswith(header_text):
          header_index=i
          break
footer_text = "End of Project Gutenberg's Alice's Adventures in Wonderland, by Lewis Carroll"
for i in range(len(lines)-1,1,-1):
     if lines[i].startswith(footer_text):
          footer_index=i
          break

#print("header_index:",header_index)
#print("footer_index:",footer_index)

del lines[footer_index+1:]
del lines[:header_index+1]


# prepare words list
words=[]
i=0
strippables = string.whitespace + string.punctuation
for line in lines:
     wlist=line.replace('-',' ').split()
     for w in wlist:
          w=w.strip(strippables)          
          if len(w)>1:
               words.append(w.lower())

# count words
d=dict()
for word in words:
     d[word] = d.get(word,0)+1

# order words by counts
t=list()
for key,value in d.items():
     t.append((value,key))
t.sort(reverse=True)

# print result
print("*** total distinct words in file",filename,"is",len(t),"***")
print("*** 100 top used words from the file",filename,"***")
for i in range(50):
     print(t[i])
