import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
from pathlib import Path
import glob

def main():
    finished = 0
    full = []
    for f in glob.glob('**/*.xml', recursive=True):
        if finished % 100 == 0:
            print(finished)
        my_file = get_file(f)
        text = parse_file(my_file)
        tokenized_text = word_tokenize(text)
        tokenized_text = clean(tokenized_text)
        #full = full + tokenized_text
        with open("output.txt", "a+", encoding="utf-8") as txt_file:
            for line in tokenized_text:
                txt_file.write("".join(line) + "\n")
        finished += 1
    print("writing array to txt")
    #freqs = analyse_text(full)

def get_file(path):
    file_to_open = Path(path)
    return file_to_open

def parse_file(file):
    root = ET.parse(file).getroot()
    for i in root.iter("{http://purl.org/dc/elements/1.1/}description"):
        return i.text

def clean(text):
    unwanted_chars = {",", ".",":","'",";","«","»","'","M."}
    for word in text:
        if word in unwanted_chars:
            text.remove(word)
    return text

def analyse_text(text):
    fdist = FreqDist(text)
    fdist.plot(50)
    plt.show()
    #return fdist

def plot(values):
    pass


#tokenized_text = word_tokenize(text)
#fdist = FreqDist(tokenized_text)

#fdist.plot(30,cumulative=False)
#plt.show


if __name__ == "__main__":
    main()