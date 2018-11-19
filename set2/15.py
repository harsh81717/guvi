x,y=map(str, input().split())
try:
  x=int(x)
  y=int(y)
  if x%2==0:
    num = x
  else:
    num = x+1
  for i in range(num,y,2):
    print(i,end=" ")
except:
  print("invalid")
