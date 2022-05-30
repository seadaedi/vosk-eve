import spacy


str = "You Take Me To the bathroom"
nlp = spacy.load('en_core_web_sm')
doc = nlp(str)

print(doc)
entities = [(i, i.label_) for i in doc.ents]

print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
# Find named entities, phrases and concepts
print("Entities : ")
for entity in doc.ents:
    print(entity.text, entity.label_)


# # Out[10]: [(Asia, 'LOC'), (Africa, 'LOC')]

# from nltk import word_tokenize , pos_tag , sent_tokenize  , pos_tag_sents  , extract , FreqDist  , chunk



# str = "go to the bathroom"
# tokens =  word_tokenize(str)
# print(tokens)
# tagged = pos_tag(tokens  , lang= "eng")
# print(tagged)
# fd =  FreqDist(tokens)
# # print(fd.most_common(3))
# print(chunk.ne_chunk(tagged))
