from flask import Flask
from flask import render_template
from flask import jsonify

from gensim.models import KeyedVectors

from SearchEngine import Engine

import json


app = Flask(__name__)


def load_res():
    print(" * Loading model...")
    global doc2vec, model
    with open('doc2vec.txt') as f:
        doc2vec = json.load(f)

    model = KeyedVectors.load_word2vec_format('../pubmed_model/pubmed2018_w2v_200D/pubmed2018_w2v_200D.bin',
                                              binary=True)


@app.route('/')
def index():
    load_res()
    return render_template("index.html")


@app.route('/get_results/<query>')
def get_results(query):
    global doc2vec, model
    results = Engine.search(query,model,doc2vec)
    return jsonify(results)


if __name__ == '__main__':
    app.run()
