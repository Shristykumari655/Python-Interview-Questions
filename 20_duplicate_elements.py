numbers = list(map(int,input("enter numbers separated by spaces:").split()))
duplicates=[]
for num in numbers:
  if numbers.count(num)>1 and num not in duplicates:
    duplicates.append(num)
print("Duplicates elements:", duplicates)
