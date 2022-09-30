import spacy as sp
from spacy import displacy
# Load English tokenizer, tagger, parser and NER
nlp = sp.load("en_core_web_sm")
sermon = ""
f = open("Transcripts/010718_FaithfulStewards_JeremySweets.txt", "r")
for x in f:
  sermon += x


# Process whole documents
doc = nlp(sermon)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)



doc = nlp("This is a sentence.")
displacy.serve(doc, style="dep")

