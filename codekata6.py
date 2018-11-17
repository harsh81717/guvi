a=input("Enter a year")
try:
  a = int(a)
  if a%400==0 or (a%4==0 and a%100!=0):
    print("yes")
  else:
    print("no")
except:
  print("Invalid")
