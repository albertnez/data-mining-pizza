#! /usr/bin/env python3
import re
import json
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from collections import Counter

TEXT_KEY = 'request_text'
EDIT_KEY = 'request_text_edit_aware'
PIZZA_KEY = 'requester_received_pizza'
PIZZA_FIELD = '@@requester_received_pizza@@'  # Make sure this is not a word contained in dataset.
LETTERS_RE = re.compile(r'[^a-z]')


def load_data(filename):
    """ Returns the json data from a filename. """
    with open(filename, 'r') as data_file:
        return json.load(data_file)


def get_post_text(post):
    """ Returns the text from a post. """
    if TEXT_KEY in post:
        return post[TEXT_KEY]
    elif EDIT_KEY in post:
        return post[EDIT_KEY]
    return ""


def get_all_text(data):
    """ Returns the text from all posts in the data. """
    text = ""
    for post in data:
        text += get_post_text(post)
    return text


def is_ok_word(word):
    """ Returns whether the word is ok or should be filtered.
        Filters words that are commas, points, or contain digits """
    return not LETTERS_RE.search(word)


def text_to_words(text, as_set=True):
    """ Returns the set of words from given text, removing stopwords,
        and applying word stem.normalized words from a text. """
    stop = stopwords.words('english')
    porter = PorterStemmer()
    tokens = wordpunct_tokenize(text)
    words = [porter.stem(w.lower()) for w in tokens if is_ok_word(w) and w.lower() not in stop]
    if as_set is True:
        words = set(words)
    return words


def post_got_pizza(post):
    """ Returns whether a post was given pizza. If there is no field, returns false. """
    if PIZZA_KEY in post:
        return post[PIZZA_KEY]
    return false


def write_data(output_filename, data, words):
    """ Writes a .csv for each post, which words does it contain. """
    with open(output_filename, 'w') as output_file:
        fieldnames = sorted(words) + [PIZZA_FIELD]
        # Write fields
        output_file.write(' '.join(fieldnames) + '\n')
        for post in data:
            post_words = text_to_words(get_post_text(post))
            # Create a dictionary with each word, indicating if it is contained or not
            dict_contains = dict(map(lambda w : (w, int(w in post_words)), words))
            # Add the field indicating if the post received the pizza.
            dict_contains[PIZZA_FIELD] = int(post_got_pizza(post))
            output_file.write(' '.join([str(dict_contains.get(k, 0)) for k in fieldnames]) + '\n')


if __name__ == '__main__':
    data = load_data('train.json')
    words = text_to_words(get_all_text(data))
    write_data('output.csv', data, words)
