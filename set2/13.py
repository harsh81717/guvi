def fun(n):
  prime=[]
  for i in range(2,n+1):
    for j in prime:
      if i%j==0:
        break
    else:
      prime.append(i)
      a=i
      #print(a,end=" ")
  b=input()
  if b.isalpha()==True:
    print("invalid")
  else:
    b=int(b)
    if b in prime:
      print("yes") 
    else:
      print("no")   
      
n=1000
fun(n)
