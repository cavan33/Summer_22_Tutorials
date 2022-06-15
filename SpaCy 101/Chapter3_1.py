# https://course.spacy.io/en/: Chapter 3 parts 1-6
# When nlp() is called, spaCy first tokenzies the text (making a Doc object),
# then it applies every component in the pipeline on the doc, in order.
import spacy

# Load the en_core_web_sm pipeline
nlp = spacy.load("en_core_web_sm")

# Print the names of the pipeline components
print(nlp.pipe_names)

# Print the full pipeline of (name, component) tuples
print(nlp.pipeline)

# You can add custom components to your spaCy pipeline. Custom components are great for
# adding custom values to documents, tokens and spans, and customizing the doc.ents.
# Example: a simple component:
from spacy.language import Language
@Language.component("length_component")
def length_component_function(doc):
    # Get the doc's length
    doc_length = len(doc)
    print(f"This document is {doc_length} tokens long.")
    # Return the doc
    return doc


# Load the small English pipeline
nlp = spacy.load("en_core_web_sm")

# Add the component first in the pipeline and print the pipe names
nlp.add_pipe("length_component", first=True)
print(nlp.pipe_names)

# Process a text
doc = nlp("This is a sentence.")