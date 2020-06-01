from django.test import TestCase

from enumerator.utils import *


class TestProcessWordList(TestCase):
    """
    Tests Case for functions used in view that produces a table of words/sentences/occurences
    """
    @classmethod
    def setUpTestData(cls):

        cls.docs = get_docs()
        cls.word_list = tokenize_words(cls.docs)

    def test_get_docs(self):
        """
        Test to see if loaded docs contain at least one string

        :return: True or False
        """
        for key, value in self.docs.items():
            self.assertTrue(len(value) >= 1)

    def test_tokenize_sentences(self):
        """
        Test to see if the output of `tokenize_sentences` is as expected

        :return: True or False
        """
        tok = tokenize_sentences(self.docs)
        dd = defaultdict(list)

        self.assertEqual(type(tok), type(dd))

        for doc_key, value in self.docs.items():
            self.assertTrue(doc_key in key for key, value in tok.items())

    def test_tokenize_words(self):
        """
        Test to see if output of `tokenize_words` is as expected

        :return: True or False
        """
        tok = tokenize_words(self.docs)
        l = list()

        self.assertEqual(type(tok), type(l))

    def test_remove_stopwords(self):
        """
        Test to see if stopwords have been removed from word list

        :return: True or False
        """
        clean = remove_stopwords(self.word_list)
        stop_words = stopwords.words("english")

        for word in clean:
            self.assertTrue(word not in stop_words)
