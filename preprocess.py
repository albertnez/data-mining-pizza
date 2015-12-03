from nltk import *
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from csv import DictWriter
import json


TEXT_KEY = 'request_text'
EDIT_KEY = 'request_text_edit_aware'
PIZZA_KEY = 'requester_received_pizza'
FORBIDEN_WORDS = [',', '.']


def load_data(filename):
    """ Returns the json data from a filename. """
    with open(filename, 'r') as data_file:
        return json.load(data_file)


def get_post_text(post):
    """ Returns the text from a post. """
    if post.has_key(TEXT_KEY):
        return post[TEXT_KEY]
    elif post.has_key(EDIT_KEY):
        return post[EDIT_KEY]
    return ""


def get_all_text(data):
    """ Returns the text from all posts in the data. """
    text = ""
    for post in data:
        text += get_post_text(post)
    return text 


def is_ok_word(word):
    """ Returns whether the word is ok or should be filtered. """
    return word[-1] != '\\' and word not in FORBIDEN_WORDS


def text_to_words(text):
    """ Returns the set of words from given text, removing stopwords,
        and applying word stem.normalized words from a text. """
    stop = stopwords.words('english')
    porter = PorterStemmer()
    tokens = wordpunct_tokenize(text)
    words = set([porter.stem(w.lower()) for w in tokens if w.lower() not in stop])
    return words


def write_data(output_filename, data, words):
    """ Writes a .csv for each post, which words does it contain. """
    with open(output_filename, 'w') as output_file:
        writer = DictWriter(output_file, delimiter=' ', fieldnames=words)
        writer.writeheader()
        # Write a row for each data entry.
        for post in data:
            post_words = text_to_words(get_post_text(post))
            dict_contains = dict(map(lambda w : (w, int(w in post_words)), words))
            writer.writerow(dict_contains)


if __name__ == '__main__':
    data = load_data('train.json')
    words = text_to_words(get_all_text(data))
    write_data('output.csv', data, words)
