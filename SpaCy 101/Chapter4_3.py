# Chapter 4 parts 10-13
# Complete the token offsets for "WEBSITE" and "PERSON" entities in the data:
import spacy
from spacy.tokens import Span

nlp = spacy.blank("en")

doc1 = nlp("Reddit partners with Patreon to help creators build communities")
doc1.ents = [
    Span(doc1, 0, 1, label="WEBSITE"),
    Span(doc1, 3, 4, label="WEBSITE"),
]

doc2 = nlp("PewDiePie smashes YouTube record")
doc2.ents = [Span(doc2, 0, 1, label="PERSON"), Span(doc2, 2, 3, label="WEBSITE")]

doc3 = nlp("Reddit founder Alexis Ohanian gave away two Metallica tickets to fans")
doc3.ents = [Span(doc3, 0, 1, label="WEBSITE"), Span(doc3, 2, 4, label="PERSON")]

# And so on...