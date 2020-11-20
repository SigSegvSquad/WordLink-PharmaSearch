from utility import SearchEngine, Evaluator

import numpy as np
import re

# nltk imports
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class Engine(SearchEngine):

    def search(query, model, doc2vec):

        query_len = 0
        query_vec = np.zeros((200,))
        result_list = dict()

        # preprocess the query
        query = re.sub('[^A-Za-z]+', ' ', query).lower()

        stop_words = set(stopwords.words('english'))

        for word in word_tokenize(query):
            if word not in stop_words:
                try:
                    query_vec += model[word]
                    query_len += 1
                except:
                    pass

        query_vec /= query_len

        for key, vectors in doc2vec.items():
            result_list[key] = 0
            for vector in vectors:
                if np.isnan(vector).any():
                    pass
                else:
                    cos_sim = np.dot(vector, query_vec) / (np.linalg.norm(vector) * np.linalg.norm(query_vec))
                    if result_list[key] < cos_sim:
                        result_list[key] = cos_sim
        return {k: v for k, v in sorted(result_list.items(), key=lambda item: item[1], reverse=True)}

