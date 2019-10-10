def split_into_substrings(string,k):
   d=[]
   size = len(string)
   for i in range(0, size, k):
      c= string[i:i+k]
      d.append(c)
   return d
s=input("Enter the string")
k=int(input("Enter k"))
a=[]
substrings=split_into_substrings(s,k)
print(substrings)