## HashtagCreator

The purpose of this Python script is to take an input of texts and find the most common occurring words and the sentences where they are used to create the following table:

| Word(#)  | Documents | Sentences containing the word |
| ------------- | ------------- | ------------- |
| philosophy  | x, y, z  |  I don't have time for philosophy. Surely this was a touch of fine philosophy; though no doubt he had never heard there was such a thing as that. Still, her pay-as-you-go philosophy implied she didn't take money for granted. |
| -  | -  | - |

### Requirements

First requirement is for the PC to have atleast Python 3. Version 3.7 was used to create this script.
Main requirement is the Python package nltk for language processing. Import and download its packages with the following commands:
```
>pip install --user -U nltk
>python
>>> import nltk
>>> nltk.download()
```
You will then get a pop-up, choose the popular corpus and download it. After this everything should work.

### Running script

In the command line, go into the folder where the file `main.py` is located. 

Run it with two arguments:
*  First argument: Folder where the text files are located, which are the input.
*  Second argument: The location and name of the CSV file, where the output aka the table will go to.

So if your text-files folder is `test-docs` and CSV file is `csvFile.csv` for example then write into the command prompt:
```
> python main.py test_docs csvFile.csv
```

Then you should have the output in the CSV file, keep in mind that there are a lot of sentences that contain the hashtags. 
