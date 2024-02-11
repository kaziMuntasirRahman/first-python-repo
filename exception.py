def voter(age):
  if age < 18:
    raise ValueError("Invalid Voter")
  return "You are allowed to vote."

print(voter(9))
print("Hello World")