import spacy as sp
from spacy import displacy
import pandas as pd
import os



# TODO: Import CSV file and create a key for the files to txt transcription of the file
# TODO: Join together the various data sources to

dir_path = "/Users/chrisried/Documents/DataProjects/BroadmoorTalks/Transcripts"


def getFiles():
    res = []
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    print(res)

def getFile(filepath):
    return pd.read_csv(filepath)

def doTheSpacy():

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


def main():
    sermons = getFile("/Users/chrisried/Documents/DataProjects/BroadmoorTalks/CompleteSermonList.csv")

    #doTheSpacy()

if __name__ == "__main__":
    main()