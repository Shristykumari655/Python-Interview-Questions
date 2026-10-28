n = int(input("Enter a number:"))
original = n
digits = len(str(n))
total = 0
while n>0:
  digit = n%10
  total = total +digit**digit
  n = n//10
if total== original:
  print("Armstrong number:")
else:
  print("Not an Armstrong number:")
