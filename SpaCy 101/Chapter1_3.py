# Chapter 1 parts 9-12
import spacy

nlp = spacy.load("en_core_web_sm")

text = "Upcoming iPhone X release date leaked as Apple reveals pre-orders"

# Process the text
doc = nlp(text)

# Iterate over the entities
for ent in doc.ents:
    # Print the entity text and label
    print(ent.text, ent.label_)

# Manually Get the span for "iPhone X", since spaCy didn't predict it:
iphone_x = doc[1:3]
print(doc[1:3]) # a check

# Print the span text
print("Missing entity:", iphone_x.text)

#---------------------------------------------------------
# Example of SpaCy's rule-based matching (beats regex)
# Example: "duck" (verb) vs "duck" (noun)
# Import the Matcher
from spacy.matcher import Matcher

# Initialize the matcher with the shared vocab
matcher = Matcher(nlp.vocab)

# Add the pattern to the matcher
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
matcher.add("IPHONE_PATTERN", [pattern])

# Process some text
doc = nlp("Upcoming iPhone X release date leaked")

# Call the matcher on the doc
matches = matcher(doc)

# Iterate over the matches
for match_id, start, end in matches:
    # Get the matched span
    matched_span = doc[start:end]
    print(matched_span.text)
# match_id = hash value of the pattern name
# start/end = start/end idx of the matched span

# Matching Lexical attributes:
pattern = [
    {"IS_DIGIT": True},
    {"LOWER": "fifa"},
    {"LOWER": "world"},
    {"LOWER": "cup"},
    {"IS_PUNCT": True}
]
matcher.add("WC_PATTERN", [pattern])
doc = nlp("2018 FIFA World Cup: France won!")
matches = matcher(doc)

for match_id, start, end in matches:
    matched_span = doc[start:end]
    print(matched_span.text)

# Matching other token attributes:
pattern = [
    {"LEMMA": "love", "POS": "VERB"},
    {"POS": "NOUN"}
]
matcher.add("LOVE_PATTERN", [pattern])
doc = nlp("I loved dogs but now I love cats more.")
matches = matcher(doc)

for match_id, start, end in matches:
    matched_span = doc[start:end]
    print(matched_span.text)

# Using operators and quantifiers:
pattern = [
    {"LEMMA": "buy"},
    {"POS": "DET", "OP": "?"},  # optional: match 0 or 1 times
    {"POS": "NOUN"}
]
matcher.add("VERB_PATTERN", [pattern])
doc = nlp("I bought a smartphone. Now I'm buying apps.")
matches = matcher(doc)

for match_id, start, end in matches:
    matched_span = doc[start:end]
    print(matched_span.text)