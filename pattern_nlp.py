




from pattern.text.en import  parse , Sentence , mood  , suggest , tag , parsetree ,pprint ,tree


txt = "tak me to the bathroom"
parsed = parse(txt)
result= Sentence(parsed)
cmd = "";
for ch in result.chunk :
    cmd+=ch.string+" "

# print(mood(result))
print(cmd)

#END REGION


# parsed = parse(txt)

# parsed = parse(txt)       

# result= Sentence(parsed)
# cmd = "";
# for ch in result.chunk :
#     cmd+=ch.string+" "


# print(mood(result))
# print(cmd)


# print(mood(result),modality(result))
# print(sentiment(result))


# taged = tag(txt)
# print(taged)
# print(Chunk(sent,taged))

# pprint(parse('will you take me to the bathroom', relations=True, lemmata=True))
# print(parsetree(sent, relations=True, lemmata=True))
# words=[]
# for word,pos in result.tagged :
#     words.append(suggest(word)[0])
# #     # print(tag_w[0],wordnet.synsets(tag_w[0],tag_w[1]))



# print(words)
# ch = PNPChunk(txt,words)
# print(words)


# print(result.chunk)
# print("Anchors " , result.anchors )
# print("Adjectives " , result.adjectives )

# ch = Chunk(parsed,words)
# print(ch)
# # s = Sentence(sent)
# # print(s)
# print(mood(sent))

# # print(sentiment(sent).assessments)

# tokens = tokenize(sent)
# tagged = tag(sent)
# # print(tagged)

# # print(ngrams(sent , 4))

# # pprint(parse(sent))
# # print(suggest("wal"))





