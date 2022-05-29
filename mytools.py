import nltk 
import ast
from nltk.tokenize import word_tokenize


@staticmethod
def Analyze(result):
    # result = ast.literal_eval(sent)
    # result = result["text"]
    print(result)
    tokens =  word_tokenize(result)
    tagged  =  nltk.pos_tag(tokens,tagset="universal")
    # return nltk.chunk.ne_chunk(tagged)
    return tagged


@staticmethod
def log(*vals):
    print(vals)