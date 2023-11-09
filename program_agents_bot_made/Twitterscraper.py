# importing necessary libraries
import requests
from bs4 import BeautifulSoup
import re

# specifying the url
url = "https://twitter.com/trends"

# sending get request to the specified url
r = requests.get(url)

# parsing the html content
soup = BeautifulSoup(r.content, 'html5lib')

# finding all the elements with the class 'trend-name'
trends = soup.find_all('div', attrs={'class': 'trend-name'})

# extracting the text from the elements
trends_list = [trend.text for trend in trends]

# removing the hashtag from the trends
trends_list = [re.sub(r'#', '', trend) for trend in trends_list]

# printing the top 10 trends
print("Top 10 Trends on Twitter:")
for trend in trends_list[:10]:
    print(trend)
