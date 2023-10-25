""" PS: pour qu'un nombre sois premier il faut exactement 2 diviseur """

n=int(input("entrer un nombre : "))
c=0
for i in range(1,n+1):
  if n%i==0:
    c=c+1
    print(i)
if c==2:
  print("premier")
else:
  print("pas premier")