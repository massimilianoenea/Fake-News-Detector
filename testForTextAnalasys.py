from textblob import TextBlob
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer
import string
import gensim

file = open('./textTest/articleTest.txt', 'r')
file2 = open('./textTest/articleTestv2.txt', 'r')
file3 = open('./textTest/toCompareTest.txt','r')
testi = [file.read(),file2.read()]
textToComp = file3.read()
# wiki = TextBlob(file.read())
tokenizer = RegexpTokenizer(r'\w+')
stop_words = stopwords.words('italian')
gen_docs = [[w.lower() for w in tokenizer.tokenize(text) if not w.lower() in stop_words] 
            for text in testi]

# cane_lemmas = wn.lemmas("chiuso", lang="ita")
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
#print(query_doc)
query_doc_bow = dictionary.doc2bow(query_doc)
#print(query_doc_bow)
query_doc_tf_idf = tf_idf[query_doc_bow]
#print(query_doc_tf_idf)

print(sims[query_doc_tf_idf])
