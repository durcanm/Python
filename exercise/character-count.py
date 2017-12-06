def get_string():
     #return "iiiistaanbbbul"
     return open("string.txt").read()

def histogram(s):
     d=dict()
     for c in s:
          """
          if c in d:
               d[c]+=1
          else:
               d[c]=1
          """
          d[c]=d.get(c,0)+1
     return d 

def histogram_sorted(d):
     l=list()
     for key,value in d.items():
          t=value,key #tuple
          l.append(t)
     l.sort(reverse=True)
     return l

def print_counts(l):
     print("*** character counts ***")
     for item in l:
          print(item[1],item[0]) #item:tuple
     


string = get_string() #type:str
histogram = histogram(string) #type:dict
histogram_sorted = histogram_sorted(histogram) #type:list

#print("string:",string)
print("histogram:",histogram)
print("histogram_sorted:",histogram_sorted)

print_counts(histogram_sorted)
