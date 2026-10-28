text = input("Enter a character:").lower()
if text in"aeiou" and len(text)==1:
  print("Vowel")
elif text.alpha() and len(text)==1:
  print("Consonant")
else:
  print("Please entera single alphabet")
