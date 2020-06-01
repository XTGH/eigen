"""
Contains functions used to construct a dictionary of words and sentences, given a set of files
"""
# standard library imports
import os
import string
from collections import defaultdict

# third party imports
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize


def get_docs():
    """
    Loads the documents from the resources directory, and stores the document name and its contents
    in a `defaultdict`

    :return: A list of dictionaries where keys are document names, and values are the contents of
    the document
    """
    docs = defaultdict(list)

    for file in os.listdir('enumerator/resources/'):
        with open(f'enumerator/resources/{file}', 'r') as document:
            content = document.read()
            docs[file].append(content)

    return docs


def tokenize_sentences(docs):
    """
    Uses nltk's `sent_tokenize` function to tokenize a paragraph or block of text in to a list of
    sentences

    :param docs: A `defaultdict` of documents and its contents
    :return: A `defaultdict` of tokenized sentences
    """
    tokenized_docs = defaultdict(list)

    for key, value in docs.items():
        t = sent_tokenize(value[0])
        tokenized_docs[key] = t

    return tokenized_docs


def tokenize_words(docs):
    """
    Uses nltk's `word_tokenize` function to tokenize a paragraph or block of text in to a list of
    words

    :param docs: A `defaultdict` of documents and its contents
    :return: A `dictionary` of tokenized words
    """
    tokenized_words = []

    for key, value in docs.items():
        for text in value:
            words = word_tokenize(text)
            tokenized_words = words

    return tokenized_words


def lemmatize_words(tokenized_words):
    """
    Uses nltk's lemmatizing function to reduce words variations down. Words are reduced down to
    their root vowels

    :param tokenized_words: A list of words to be lemmatized
    :return: A list of filtered words
    """
    lem = WordNetLemmatizer()
    filtered_words = []

    for word in tokenized_words:
        # lemmatize word to its root vowel
        filtered_words.append(lem.lemmatize(word.lower(), "v"))

    return filtered_words


def remove_stopwords(word_list):
    """
    Removes stop words and punctuation from a list of words

    :return: A list of filtered words
    """
    stop_words = stopwords.words("english")
    filtered_sent = []

    for w in word_list:
        if w.lower() not in stop_words and w not in string.punctuation:
            filtered_sent.append(w.lower())

    # remove duplicated words
    filtered_sent = list(set(filtered_sent))

    return filtered_sent


def get_processed_word_list():
    """
    Runs several functions used to tokenize, process and clean a word list

    :return: A list of words with punctuation and word variations removed
    """
    docs = get_docs()
    tokenized_words = tokenize_words(docs)
    # lemmed_words = lemmatize_words(tokenized_words)
    cleaned_words = remove_stopwords(tokenized_words)

    return cleaned_words


def get_processed_sentence_list():
    """
    Runs functions used to process and tokenize and process a list of sentences

    :return: A dictionary of documents and their processed sentences as a list.
    """
    docs = get_docs()
    tokenized_sentences = tokenize_sentences(docs)

    return tokenized_sentences


def evaluate_words():
    """
    Main function used to gather a clean list of words, and sentences from documents. The words
    are stored in the `result` dictionary with several keys that allow you to access information
    such as the word, sentences and documents it is used in, and the number of occurences.

    :return: A dictionary of words and data
    """
    word_list = get_processed_word_list()
    doc_sentences = get_processed_sentence_list()

    # for each word in the word list, create a dictionary with the word as the `word` key's value
    result = [
        {'word': word,
         'sentences': [],
         'documents': [],
         'occurences': ''
         } for word in word_list
    ]

    # define a string of punctuation without hyphens as we want to preserve them in the sentences
    custom_punc = '!"#$%&\()*+,./:;<=>?@[\\]^_`{|}~'

    # loop through each dictionary containing the list of tokenized sentences
    for doc, sentences in doc_sentences.items():

        # for each sentence in the list of tokenized sentences
        for sentence in sentences:
            # strip punctuation from the sentence
            sentence = sentence.translate(str.maketrans('', '', custom_punc))

            for item in result:
                # for each word in the dictionary, see if it is each word in the sentence
                if item['word'] in sentence.lower().split():
                    item['sentences'].append(sentence)

                    # add the document name to the document list
                    if doc not in item['documents']:
                        item['documents'].append(doc)

                # find total word occurences by counting the number of stored sentences
                item['occurences'] = len(item['sentences'])

    return result


