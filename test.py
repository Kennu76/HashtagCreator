
def main():
    import nltk
    from nltk.corpus import stopwords

    (dictOfTexts, fullText) = getTextFromFiles('test_docs')

    freqDist = getMostFrequentWords(fullText).most_common(10)
    hashTags = [w for  (w, num) in freqDist ]
    finalResultDictionary = {}
    for hashTag in hashTags:
      finalResultDictionary[hashTag] = getListOfOccurancesAndSentences(hashTag, dictOfTexts)
    print(finalResultDictionary)

def getListOfOccurancesAndSentences(hashTag, dictOfTexts):
  from nltk import sent_tokenize
  listOfSentences = []
  listOfFiles = []
  for (file, text) in dictOfTexts.items():
    occurs = False
    for sentence in sent_tokenize(text):
      if hashTag in sentence:
        occurs = True
        listOfSentences.append(sentence.replace(hashTag, hashTag.upper()))
    if occurs:
      listOfFiles.append(file)
  
  return  (listOfFiles, listOfSentences)

def getTextFromFiles(folder):
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    fullText = ""
    dictOfTexts = {}
    for file in onlyfiles:
        textFile = open(folder + '/' + file, encoding="utf8")
        if textFile.mode == "r":
            dictOfTexts[file] = textFile.read()
            fullText += dictOfTexts[file]
    return (dictOfTexts, fullText)

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