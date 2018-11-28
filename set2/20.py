a=input()
try:
  a=int(a)
  for i in range(1,6):
    print(a*i,end=" ")
except:
  print("invalid code")
