n = int(input("Enter a number:"))
if n<=1:
  print(" Not a prime no")
else:
  for i in range(2, n-1):
    if n%i==0:
      print("Not a prime no")
      break
    else:
      print("Prime no")
      
  
