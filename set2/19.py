a=int(input())
factorial = 1
if a<0:
  print("not possible")
elif a==0:
  print("1")
else:
  for i in range(1,a+1):
    factorial = factorial*i
  print(factorial)
