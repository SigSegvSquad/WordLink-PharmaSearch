import os
import json
from glob import glob
from random import randint, choices


class Corpus:
    def __init__(self, dir_path):
        self.dir_path = dir_path
        self.txt_list = [f for f in glob(dir_path + "*.txt")]
        self.tit_list = [fil.title for fil in self.txt_list]
        self.doc_list = [Document(f) for f in self.txt_list]

    def split_sections(self, key='all'):
        return [file.document[key] for file in self.doc_list]

    def split_sentences(self, key='all'):
        return [file.split_sentences(key) for file in self.doc_list]

    def split_words(self, key='all'):
        return [file.split_words(key) for file in self.doc_list]

    # use try-catch for this one, random.choices fucks up sometimes
    def generate_queries(self, key='all', num_docs=10, num_queries=1, method='random_phrases'):
        return {i.title:(i.generate_queries(num_queries, method, key)) for i in choices(self.doc_list, k=num_docs)}


class Document:
    def __init__(self, filepath):
        # init file attributes
        self.filepath = filepath
        self.extension = os.path.splitext(filepath)[-1]
        self.title = os.path.basename(filepath).replace(self.extension, '')
        # init empty headings
        self.document = {'start': '', 'abstract': '', 'keywords': '',
                         'introduction': '', 'main': '', 'conclusion': '',
                         'acknowledgements': '', 'references': '', 'end': ''}

        # read file
        self.read()

    # Basic Input/Output Operations
    def read(self):
        # json file
        if self.extension == '.json':
            self.read_json(self.filepath)

        # txt file
        elif self.extension == '.txt':
            self.read_txt(self.filepath)

        # user's a retard
        else:
            print("Unsupported file format")

    def read_txt(self, filepath):
        curr_heading = 'start'
        contents = ''
        with open(filepath, 'r') as f:
            for line in f.readlines():
                line = line.lower()
                line = line.replace('\n', '')

                # new heading
                if line in self.document.keys():
                    self.document[curr_heading] = contents
                    contents = ''
                    curr_heading = line

                # same heading as before
                else:
                    line = line.replace('\n', ' ')
                    contents += ''.join(e for e in line if (e.isalnum() or e == ' ' or e == '.'))

    def read_json(self, filepath):
        self.document = json.load(filepath)

    def save_json(self, directory):
        with open(directory + self.title + '.json', "w+") as outfile:
            json.dump(self.document, outfile)

    # Utility functions
    def count_words(self, key='all'):
        return len(self.split_words(key))

    def split_words(self, key='all'):
        words = []
        if key == 'all':
            for key, item in self.document.items():
                words += item.split()

        elif key in self.document.keys():
            words = self.document[key].split()

        else:
            print('wrong key, retard')

        return words

    def split_sentences(self, key='all'):
        sentences = []
        if key == 'all':
            for key, item in self.document.items():
                sentences += item.split('.')

        elif key in self.document.keys():
            sentences = self.document[key].split('.')

        else:
            print('wrong key, retard')

        return sentences

    def generate_queries(self, number=1, method='random_phrases', key='all'):
        queries = []

        # generate queries using the random module
        if method == 'random_phrases':
            for i in range(number):
                try:
                    word_list = self.split_words(key)
                    word_no = randint(1, 10)
                    start_pos = randint(1, len(word_list) - word_no)
                    queries.append(' '.join(word_list[start_pos: start_pos + word_no]))
                except:
                    print('issue in document: ', self.title)

        elif method == 'summarisation':
            pass

        else:
            print('no such method, dumbass')

        return queries
