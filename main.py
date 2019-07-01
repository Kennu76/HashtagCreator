import nltk
from nltk.corpus import treebank
from nltk.corpus import stopwords

#Sample sentence used for processing
sentence = """John came to office at eight o'clock on Monday morning & left the office with Arthur bit early."""

#Tokenizing the sentence into words 
word_tokens = nltk.word_tokenize(sentence)
#Tagging words
tagged_words = nltk.pos_tag(word_tokens)
#Identify named entities
named_entities = nltk.chunk.ne_chunk(tagged_words)

#Removing the stopwords from the text - Predefined stopwords in English have been used.
stop_words = set(stopwords.words('english'))
filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print('Sentence - ' + sentence)
print('Word tokens - ')
print(word_tokens)
print('Tagged words - ')
print(tagged_words)
print('Named entities - ')
print(named_entities)
print('Word tokens - ')
print(word_tokens)
print('Filtered sentence - ')
print(filtered_sentence)