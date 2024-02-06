text = input("Enter a string: ")
wordCounter = 1
letterCounter = 0
digitCounter = 0


for x in text:
  if('a' <= x <= 'z') or ('A' <= x <= 'Z'):
    letterCounter += 1
  elif ('0' <= x <= '9'):
    digitCounter += 1
  elif(x == ' '):
    wordCounter += 1


print(wordCounter)
print(letterCounter)
print(digitCounter)