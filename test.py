
def main():
    import nltk
    from nltk.tokenize import sent_tokenize
    from nltk import word_tokenize  
    from nltk.corpus import stopwords

    text = getTextFromFiles('test_docs')

    freqDist = getMostFrequentWords(text).most_common(100)
    print(freqDist)

def getTextFromFiles(folder):
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    text = ""
    for file in onlyfiles:
        textFile = open(folder + '/' + file, encoding="utf8")
        if textFile.mode == "r":
            text += textFile.read()
    return text

def getMostFrequentWords(text):
    from nltk import FreqDist
    from nltk import word_tokenize  
    from nltk import pos_tag
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    tokenizedText = word_tokenize(text.lower())
    taggedWords = pos_tag(tokenizedText)
    nouns = [w for  (w, pos) in taggedWords if pos == 'NN']

    filteredText = [w for w in nouns if not w in stop_words]
    return FreqDist(filteredText)

    
if __name__== "__main__":
  main()