# importing necessary libraries
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# initializing sentiment analyzer
sid = SentimentIntensityAnalyzer()


# defining function to interpret sentiment
def sentiment_analyzer_scores(sentence):
    score = sid.polarity_scores(sentence)
    if score['compound'] >= 0.05:
        return "Positive"
    elif score['compound'] <= - 0.05:
        return "Negative"
    else:
        return "Neutral"


# defining main function
def main():
    # getting user input
    user_input = input("Please enter your message: ")
    # removing punctuation
    user_input = re.sub(r'[^\w\s]', '', user_input)
    # analyzing sentiment
    sentiment = sentiment_analyzer_scores(user_input)
    # printing sentiment
    print("Your sentiment is: " + sentiment)


# calling main function
if __name__ == "__main__":
    main()
