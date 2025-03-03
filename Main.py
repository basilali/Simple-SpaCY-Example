import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Can you tell me what its like at Microsoft?") # Prints "Sorry, I don't know. I don't work for Microsoft."
doc2 = nlp("Tell me how beautiful Canada is.") # Prints "Sorry, I don't know. I've never been to Canada."

for ent in doc.ents:
    if ent.label_ == "ORG":
        print(f"Sorry, I don't know. I don't work for {ent.text}.")
    elif ent.label_ == "GPE":
        print(f"Sorry, I don't know. I've never been to {ent.text}.")
    else:
        print("Sorry, I don't know the answer to that question.")


