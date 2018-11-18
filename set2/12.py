n=input()
if n.isdigit()==True and n==n[::-1]:
  print("yes")
elif n.isdigit()==True:
  print("No")
else:
  print("invalid")
