import time

# Greeting message
print("Welcome to the Customer Support Bot!")

# Ask for user's name
name = input("What is your name? ")

# Ask for user's issue
issue = input("What is your issue? ")

# Provide initial response
print("Thanks for reaching out, " + name + ". Let me see if I can help you with your issue: " + issue)

# Provide loading message
print("Please wait while I look into this...")

# Simulate loading time
time.sleep(3)

# Provide solution
print("I think I have a solution for you. Please try the following steps:")
print("1. Restart your device")
print("2. Check your internet connection")
print("3. Try the action again")

# Ask if the solution worked
solution_worked = input("Did this solution work? (yes/no) ")

# Provide follow-up response
if solution_worked == "yes":
  print("Glad I could help!")
else:
  print("Sorry I couldn't be of more help. Please contact our customer service team for further assistance.")