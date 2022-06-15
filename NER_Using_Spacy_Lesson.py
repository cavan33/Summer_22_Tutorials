# NER (Named Entity Recognition) with SpaCy Lesson
# https://www.analyticsvidhya.com/blog/2021/06/nlp-application-named-entity-recognition-ner-in-python-with-spacy/

import spacy
from spacy import displacy

NER = spacy.load("en_core_web_sm")
# ^ Needs 'python -m spacy download en_core_web_sm'

# Sample text we shall be testing:
raw_text = "The Indian Space Research Organisation or is the national space agency of India, headquartered in Bengaluru. It operates under Department of Space which is directly overseen by the Prime Minister of India while Chairman of ISRO acts as executive of DOS as well."

text1 = NER(raw_text)

# Print the data on the NEs:
for word in text1.ents:
    print(word.text,word.label_)

# If we want to see more info on a particular NE:
spacy.explain("ORG")
spacy.explain("GPE")

# Visualize NEs directly in the text:
# displacy.render(text1,style="ent",jupyter=True)


# Second example:
raw_text2 = "The Mars Orbiter Mission (MOM), informally known as Mangalyaan, was launched into Earth orbit on 5 November 2013 by the Indian Space Research Organisation (ISRO) and has entered Mars orbit on 24 September 2014. India thus became the first country to enter Mars orbit on its first attempt. It was completed at a record low cost of $74 million."
text2 = NER(raw_text2)
for word in text2.ents:
    print(word.text,word.label_)
# displacy.render(text2,style="ent",jupyter=True)

# We shall web scrape data from a news article and do NER on the text data gathered from there.
# We shall use Beautiful Soup for web scraping purposes.

from bs4 import BeautifulSoup
import requests
import re

# Now, we will use the URL of the news article.

URL="https://www.zeebiz.com/markets/currency/news-cryptocurrency-news-today-june-12-bitcoin-dogecoin-shiba-inu-and-other-top-coins-prices-and-all-latest-updates-158490"
html_content = requests.get(URL).text
soup = BeautifulSoup(html_content, "lxml")
# Now, we get the body content.

body=soup.body.text

# Now, we use regex to clean the text.
body= body.replace('\n', ' ')
body= body.replace('\t', ' ')
body= body.replace('\r', ' ')
body= body.replace('\xa0', ' ')
body=re.sub(r'[^\w\s]', '', body)
# Still has some foreign characters, but it's good enough.
# Let us now have a look at the text.

body[1000:1500]

# Now, let us proceed with Named Entity Recognition.

text3= NER(body)
# displacy.render(text3,style="ent",jupyter=True)