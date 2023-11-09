import re

# Define a dictionary with the predefined responses
responses = {
  "what's your name?": "My name is FAQ Bot.",
  "what's today's weather?": "It is sunny today.",
  "default": "I'm sorry, I don't understand."
}

# Define a function to find the matching response for the user's input
def respond(message):
  # Check if the message is in the responses
  if message in responses:
    # Return the matching message
    bot_message = responses[message]
  else:
    # Return the "default" message
    bot_message = responses["default"]
  return bot_message

# Define a function to find a keyword in the message
def match_rule(rules, message):
  response, phrase = "default", None
  
  # Iterate over the rules dictionary
  for pattern, responses in rules.items():
    # Create a match object
    match = re.search(pattern, message)
    if match is not None:
      # Choose a random response
      response = random.choice(responses)
      if '{0}' in response:
        phrase = match.group(1)
  # Return the response and phrase
  return response, phrase

# Define a function