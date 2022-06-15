# https://course.spacy.io/en/: Chapter 4 parts 1-4
# SpaCy's Matcher is a great way to quickly create training data for 
# named entity models. A list of sentences is available as the variable TEXTS.
import json
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span, DocBin

with open("iphone.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

nlp = spacy.blank("en")
matcher = Matcher(nlp.vocab)
# Add patterns to the matcher
pattern1 = ([{"LOWER": "iphone"}, {"LOWER": "x"}])
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True}]
matcher.add("GADGET", [pattern1, pattern2])
docs = []
for doc in nlp.pipe(TEXTS):
    matches = matcher(doc)
    spans = [Span(doc, start, end, label=match_id) for match_id, start, end in matches]
    doc.ents = spans
    docs.append(doc)

# After creating the data for our corpus (docs), we need to save it to a .spacy file.
doc_bin = DocBin(docs=docs)
doc_bin.to_disk("./train.spacy")