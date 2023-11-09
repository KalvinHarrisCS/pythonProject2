#importing necessary libraries
import nltk
import pandas as pd
import numpy as np
import re
import random
import spacy
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt

#importing necessary functions
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#importing the dataset
data = pd.read_csv('customer_support_data.csv')

#preprocessing the data
#removing punctuation
data['message'] = data['message'].apply(lambda x: re.sub('[^\w\s]','',x))

#tokenizing
data['message'] = data['message'].apply(lambda x: nltk.word_tokenize(x))

#lemmatizing
lemmatizer = WordNetLemmatizer()
data['message'] = data['message'].apply(lambda x: [lemmatizer.lemmatize(word) for word in x])

#removing stopwords
stop_words = set