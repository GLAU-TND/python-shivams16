def fun(k, a):
    for i in range(len(a)):
           if a[i] >= k:
              continue
           for j in range(i+1, len(a)):
              if (a[i] + a[j]) == k:
                return [i+1, j+1]
    return None
a=eval(input("Enter list of integers"))
k=int(input("Enter k"))
b=fun(k,a)
print(b)