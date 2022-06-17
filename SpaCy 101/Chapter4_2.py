# Chapter 4 parts 5-9 (training)
# Re-read part 5 (https://course.spacy.io/en/chapter4) if you're stuck.

# For terminal:
# python -m spacy init config ./config.cfg --lang en --pipeline ner
# View:
# cat ./config.cfg

# Train a model from this cfg file:
# python -m spacy train ./config_gadget.cfg --output ./output --paths.train ./train_gadget.spacy --paths.dev ./dev_gadget.spacy
# train_gadget contains training examples; dev_gadget contains evaluation examples