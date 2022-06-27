# https://course.spacy.io/en/: Chapter 2 parts 1-5
import spacy
# The hash is spacy's way to efficiently index strings:
# Any string, even a non-regular word, can be converted to a hash
nlp = spacy.blank("en")
doc = nlp("I have a cat")

# Look up the hash for the word "cat"
cat_hash = nlp.vocab.strings["cat"]
print(cat_hash)

# Look up the cat_hash to get the string
cat_string = nlp.vocab.strings[cat_hash]
print(cat_string)

# Creating a Doc object:
# Import the Doc class
from spacy.tokens import Doc

# Desired text: "spaCy is cool!"
words = ["spaCy", "is", "cool", "!"]
spaces = [True, True, False, False]

# Create a Doc from the words and spaces
# the vocab needs to be passed in, by the way
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
# print(doc.ents)