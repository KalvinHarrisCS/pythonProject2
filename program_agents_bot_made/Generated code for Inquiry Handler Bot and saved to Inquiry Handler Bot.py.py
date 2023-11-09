import random

# Greeting message
print("Welcome to our customer support team!")

# Ask user for their name
name = input("What is your name? ")

# Ask user for their issue
issue = input("What is your issue? ")

# Generate a random number
rand_num = random.randint(1,100)

# Give the user a ticket number
print("Thank you for contacting us, " + name + ". We have assigned your issue a ticket number: " + str(rand_num))

# Ask user if they need any other help
help_needed = input("Do you need any other help? (yes/no) ")

# If yes, ask for more details
if help_needed == "yes":
    more_details = input("Please provide more details: ")
    print("Thank you for the additional information. We will look into this and get back to you soon.")

# If no, thank the user
elif help_needed == "no":
    print("Thank you for contacting us. We will look into this and get back to you soon.")