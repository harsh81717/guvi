#Not optimized
lower,upper=map(str,input().split())
try:
  lower=int(lower)
  upper=int(upper)
  for num in range(lower,upper + 1):
    if num > 1:
      for i in range(2,num):
        if (num % i) == 0:
          break
      else:
        print(num,end=" ")
except:
  print("invalid")
   
