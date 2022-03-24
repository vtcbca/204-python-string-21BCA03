#WAS to enter five string in a list and check and print string whose length has even no. of character

def createlist():
    l=[]
    for i in range(5):
      s=input("enter string:")
      l.append(s)
createlist()
def evenno(l):
    count=0
    for i in l:
        for j in i:
          count +=1
        if len(s%2==0):
          print(l)
    return count
evenno(l)    
