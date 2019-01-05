from textblob import TextBlob
import re
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import treetaggerwrapper
import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer
import string
import gensim

########## FUNZIONI PER LA DETERMINAZIONE DEL POS ###################

def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']


def is_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']


def is_adverb(tag):
    return tag in ['RB', 'RBR', 'RBS']


def is_adjective(tag):
    return tag in ['JJ', 'JJR', 'JJS']


def penn_to_wn(tag):
    if is_adjective(tag):
        return wn.ADJ
    elif is_noun(tag):
        return wn.NOUN
    elif is_adverb(tag):
        return wn.ADV
    elif is_verb(tag):
        return wn.VERB
    return None


#################### FINE FUNZIONI #########################

file = open('./textTest/articleTest.txt', 'r')
file2 = open('./textTest/articleTest2.txt', 'r')
file3 = open('./textTest/toCompareTest.txt','r')

testo1 = file.read()
testo2 = file2.read()
textToComp = file3.read()
testi = [testo1,testo2]

tokenizer = RegexpTokenizer(r'\w+')
stop_words = stopwords.words('italian')
tagger = treetaggerwrapper.TreeTagger(TAGLANG='it', TAGPARFILE='italian.par')

print(stop_words)
exit()
gen_docs = [[w.lower() for w in tokenizer.tokenize(text) if not w.lower() in stop_words] 
            for text in testi]

lemGen_docs = [[re.sub('[^A-Z]', '', t) for t in tagger.tag_text(docs)] for docs in gen_docs]

# print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
#print(dictionary[5])
#print(dictionary.token2id['inter'])
#print("Number of words in dictionary:",len(dictionary))
#for i in range(len(dictionary)):
#    print(i, dictionary[i])

corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
# print(corpus)

tf_idf = gensim.models.TfidfModel(corpus)
#print(tf_idf)
#s = 0
#for i in corpus:
#    s += len(i)
#print(s)

sims = gensim.similarities.Similarity('/Users/massimilianoenea/similarity',tf_idf[corpus],num_features=int(len(dictionary)))
# print(sims)
# print(type(sims))

query_doc = [w.lower() for w in tokenizer.tokenize(textToComp) if not w.lower() in stop_words]
print(query_doc)
query_doc_bow = dictionary.doc2bow(query_doc)
#print(query_doc_bow)
query_doc_tf_idf = tf_idf[query_doc_bow]
#print(query_doc_tf_idf)

print(sims[query_doc_tf_idf])