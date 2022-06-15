# Chapter 2 parts 6-10
import spacy

nlp = spacy.blank("en")

# Import the Doc and Span classes
from spacy.tokens import Doc, Span

words = ["I", "like", "David", "Bowie"]
spaces = [True, True, True, False]

# Create a doc from the words and spaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

# Create a span for "David Bowie" from the doc and assign it the label "PERSON"
span = Span(doc, 2, 4, label="PERSON")
print(span.text, span.label_)

# Add the span to the doc's entities
doc.ents = [span]

# Print entities' text and labels
print([(ent.text, ent.label_) for ent in doc.ents])

# Example of looking for a phrase using SpaCy's tokens:
doc = nlp("Berlin looks like a nice city")

# Iterate over the tokens
for token in doc:
    # Check if the current token is a proper noun
    if token.pos_ == "PROPN":
        # Check if the next token is a verb
        if doc[token.i + 1].pos_ == "VERB":
            print("Found proper noun before a verb:", token.text)
# It's best to keep things as tokens, not strings, for as long as possible.

#------------------------------------------------------------
# Word vectors and semantic similarity
# Load a larger pipeline with vectors
nlp = spacy.load("en_core_web_md")

doc = nlp("I have a banana")
# Access the [word] vector via the token.vector attribute
print(doc[3].vector)

# Compare two documents
doc1 = nlp("It's a warm summer day")
doc2 = nlp("It's sunny outside")
# Get the similarity of doc1 and doc2
similarity = doc1.similarity(doc2)
print(similarity)

# Compare 2 tokens:
doc = nlp("I like pizza and pasta")
token1 = doc[2]
token2 = doc[4]
print(token1.similarity(token2))

# Compare 2 spans:
doc = nlp("This was a great restaurant. Afterwards, we went to a really nice bar.")

# Create spans for "great restaurant" and "really nice bar"
span1 = doc[3:5]
span2 = doc[12:15]

# Get the similarity of the spans
similarity = span1.similarity(span2)
print(similarity)