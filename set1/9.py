x,y=input().split()
li=input().split()
try:
  x,y=int(x),int(y)
  z = [int(a) for a in li]
  print(sum(z[:y]))
except:
  print("invalid")

