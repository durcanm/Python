fin = open("words.txt")
d = dict()

for line in fin: #type-line:str
     word=line.strip().lower()
     """
     word: deltas
     sorted(word): ['a', 'd', 'e', 'l', 's', 't']
     ''.join(sorted(word)): adelst
     """
     
     key = ''.join(sorted(word))

     if key not in d:
          d[key]=[word]
     else:
          d[key].append(word)

#print(d)


for key,value in d.items():
     if len(value) > 10:
          print(key,value)




# order by descending
t=[]
for key,value in d.items():
     t.append((len(value),key))

t.sort(reverse=True)
for item in t:
     print(item[0],item[1],d[item[1]])
     


fin.close()

"""
aelrst ['alerts', 'alters', 'artels', 'estral', 'laster', 'ratels', 'salter', 'slater', 'staler', 'stelar', 'talers']
aeprs  ['apers', 'asper', 'pares', 'parse', 'pears', 'prase', 'presa', 'rapes', 'reaps', 'spare', 'spear']
"""
