import pandas as pd
import numpy as np
import re
import nltk
import matplotlib.pyplot as plt
import seaborn as sns

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from wordcloud import WordCloud
from gensim.models import Word2Vec

# ==============================
# DOWNLOAD NLTK RESOURCE
# ==============================
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# ==============================
# LOAD DATA
# ==============================
df = pd.read_csv("data.csv")
texts = df['text'].astype(str)

# ==============================
# PREPROCESSING FUNCTION
# ==============================
stop_words = set(stopwords.words('indonesian'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    # lowercase
    text = text.lower()

    # remove angka & simbol
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # tokenizing
    tokens = word_tokenize(text)

    # stopwords removal
    filtered_tokens = [w for w in tokens if w not in stop_words]

    # stemming
    stemmed_tokens = [stemmer.stem(w) for w in filtered_tokens]

    # lemmatization
    lemmatized_tokens = [lemmatizer.lemmatize(w) for w in stemmed_tokens]

    return tokens, filtered_tokens, stemmed_tokens, lemmatized_tokens

# ==============================
# APPLY PREPROCESSING
# ==============================
all_tokens = []
processed_texts = []

for text in texts:
    tokens, filtered, stemmed, lemmatized = preprocess(text)

    print("\nTEXT:", text)
    print("Token:", tokens)
    print("Filtered:", filtered)
    print("Stemmed:", stemmed)
    print("Lemmatized:", lemmatized)

    # POS Tagging
    print("POS Tag:", pos_tag(filtered))

    all_tokens.extend(filtered)
    processed_texts.append(" ".join(lemmatized))

# ==============================
# BAG OF WORDS
# ==============================
cv = CountVectorizer()
bow = cv.fit_transform(processed_texts)

print("\n=== Bag of Words ===")
print(cv.get_feature_names_out())
print(bow.toarray())

# ==============================
# TF-IDF
# ==============================
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(processed_texts)

print("\n=== TF-IDF ===")
print(tfidf.get_feature_names_out())
print(tfidf_matrix.toarray())

# ==============================
# COSINE SIMILARITY
# ==============================
cos_sim = cosine_similarity(tfidf_matrix)
print("\n=== Cosine Similarity ===")
print(cos_sim)

# ==============================
# VISUALISASI BAG OF WORDS
# ==============================
word_counts = np.sum(bow.toarray(), axis=0)

plt.figure()
sns.barplot(x=cv.get_feature_names_out(), y=word_counts)
plt.title("Bag of Words")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==============================
# VISUALISASI TF-IDF
# ==============================
tfidf_scores = np.mean(tfidf_matrix.toarray(), axis=0)

plt.figure()
sns.barplot(x=tfidf.get_feature_names_out(), y=tfidf_scores)
plt.title("TF-IDF")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==============================
# WORDCLOUD
# ==============================
wordcloud = WordCloud(width=800, height=400).generate(" ".join(all_tokens))

plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("WordCloud")
plt.show()

# ==============================
# WORD EMBEDDINGS (Word2Vec)
# ==============================
sentences = [text.split() for text in processed_texts]

model = Word2Vec(sentences, vector_size=100, window=5, min_count=1)

print("\n=== Word Embedding ===")
print("Vector kata 'teknologi':")
if "teknologi" in model.wv:
    print(model.wv["teknologi"])

# Similar words
print("\nKata mirip 'teknologi':")
if "teknologi" in model.wv:
    print(model.wv.most_similar("teknologi"))