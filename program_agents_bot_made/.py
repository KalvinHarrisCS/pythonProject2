#import necessary libraries
import random
import time

#greeting message
print("Hello! I'm your friendly chatbot. Let's chat!")

#list of possible responses
responses = ["I'm doing great!", "That's interesting!", "Tell me more!", "That sounds fun!", "That's too bad."]

#infinite loop
while True:
    #get user input
    user_input = input("What would you like to talk about?\n")

    #generate random response
    response = random.choice(responses)
    print(response)

    #wait for two seconds
    time.sleep(2)