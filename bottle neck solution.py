n = int(input("Enter number of bottles"))
res = list(map(int,input("Enter the radius of the bottles").split()))
print(max([res.count(i) for i in res]))



