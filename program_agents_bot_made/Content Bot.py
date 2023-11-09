#!/usr/bin/env python

# Content Generation Bot
# This bot will generate blog posts, social media updates, or marketing copy based on input topics or keywords.

# Imports
import random

# Variables
topics = ["Technology", "Sports", "Politics", "Business", "Fashion", "Travel", "Food", "Entertainment"]

# Welcome Message
print("Welcome to the Content Generation Bot!")

# Ask for input
user_input = input("Please enter a topic or keyword: ")

# Check if input is in topics list
if user_input in topics:
    # Generate content
    content = "Today's topic is " + user_input + ". "
    content += "This is an interesting topic to explore. "
    content += "There are many different aspects of " + user_input + " that can be discussed. "
    content += "For example, one could talk about the latest developments in " + user_input + ", or the impact it has had on society. "
    content += "No matter what angle you choose to take, " + user_input + " is sure to be an interesting topic to explore. "

# If input is not in topics list
else:
    # Generate content
    content = "Today's topic is " + user_input + ". "
