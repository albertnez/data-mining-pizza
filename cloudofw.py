from text_to_word_cloud import *
from nltk import *
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def word_freqs_file(filename):
    with open(filename,'r') as fh:
        text = fh.read()
    return word_tokenize(text)

# Llegeix el fitxer de la constitucio americana i fa el nuvol de paraules
words=word_freqs_file("const.txt")
cnt = Counter(words)
"""
save_il_to_word_cloud_file("a.txt",cnt,len(words),call_R=True)


# Fa el nuvol de paraules passant a minuscules i eliminant les stopwords
stop = stopwords.words('english')
porter = PorterStemmer()
w2 = [i.lower() for i in words if i.lower() not in stop]
cnt = Counter(w2)
save_il_to_word_cloud_file("a2.txt",cnt,len(w2),call_R=True)
"""


# Fa el nuvol de paraules passant a minuscules, eliminant les stopwords 
# i aplicant stemer
stop = stopwords.words('english')
porter = PorterStemmer()
w2 = [porter.stem(i.lower()) for i in words if i.lower() not in stop]
cnt = Counter(w2)
save_il_to_word_cloud_file("a3.txt",cnt,len(w2),call_R=True)
