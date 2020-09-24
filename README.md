![TitleBanner](https://github.com/OverPoweredDev/Pharma_NLPSearch/blob/master/images/EDI_banner3.png)

## Introduction

![Python-3.8](https://img.shields.io/badge/Python-3.8-green?style=for-the-badge)
![gensim-3.8.3](https://img.shields.io/badge/gensim-3.8.3-blue?style=for-the-badge)
![NLTK](https://img.shields.io/badge/NLTK-3.5-purple?style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-1.1.5-lightblue?style=for-the-badge)
![PR](https://img.shields.io/badge/PRs-welcome-red?style=for-the-badge)
![PR](https://img.shields.io/badge/%20-Open%20Source-blueviolet?style=for-the-badge)


## Dataset

Research articles from various journals like World journal of pharmaceuticals, international journal of pharmaceuticals, journal of biomedicine and pharmacotherapy etc. Also there are plenty of research articles by scientists. Also some drugs related stuff is also there.

## Approach

- Create shared vector space among word2vec representations of articles and search phrases
- Make a seq2seq model to summarize and encode Research text documents
- Find way to map research paper vectors to search phrase vectors
- Create search engine using 1, 2 and 3
- Build UI to house the search engine


r   

## Technology Used

- Python
- gensim
- NLTK
- PyTorch: Pytorch is a machine learning library we're using to gain better insights into the way the models will work. With a standard seq2seq keras model it's just a black box but Pytorch allows for higher customisation and is more suited for academic use like this project.
- Gensim: Gensim is a library used to develop scalable word2vec or doc2vec models which we would need to create a shared vector space for the input strings as well as the documents fed to it. It also comes packaged with several standard word2vec models which we would need for general vocabulary in our search.


## About Us

- Omkar Prabhune
- Prabhav Pandya
- Pritesh Pawar
- Pranav Tambaku
- Vaidehi Patil
