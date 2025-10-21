import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("Hello world, this is a spaCy test.")
print([(t.text, t.pos_) for t in doc])