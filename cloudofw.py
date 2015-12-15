from text_to_word_cloud import *
from collections import Counter
from preprocess import *


if __name__ == '__main__':
    data = load_data('train.json')
    words = text_to_words(get_all_text(data), as_set=False)
    cnt = Counter(words)
    save_il_to_word_cloud_file("cloudofw.txt",cnt,len(words),call_R=True)
