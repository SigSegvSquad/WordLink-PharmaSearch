from flask import Flask
from flask import render_template
import asyncio
from gensim.models import Word2Vec
import numpy as np
import re
import nltk
from nltk import punkt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim.models import KeyedVectors

app = Flask(__name__)


def load_model():
    model = KeyedVectors.load_word2vec_format('../pubmed_model/pubmed2018_w2v_200D/pubmed2018_w2v_200D.bin',binary=True)
    print(model["carbon"])


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/get_results/<query>')
def get_results(query):
    return "none"


if __name__ == '__main__':
    app.run()
