import string
import re
import pandas as pd
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ==============================
# DOWNLOAD NLTK
# ==============================
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# ==============================
# DATA
# ==============================
sentences = [
    "Artificial intelligence is transforming technology and business",
    "Economic growth is affected by inflation and market conditions",
    "Healthcare systems are improving with modern technology",
    "Education systems are evolving with digital platforms",
    "Sports events are becoming more competitive globally"
]

# ==============================
# PREPROCESSING (DETAIL)
# ==============================
def preprocess_detail(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))

    tokens = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words and word.isalnum()]

    ps = PorterStemmer()
    stemmed_tokens = [ps.stem(word) for word in filtered_tokens]

    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

    pos_tag_stem = pos_tag(stemmed_tokens)
    pos_tag_lemma = pos_tag(lemmatized_tokens)

    return {
        "original_text": text,
        "tokens": tokens,
        "filtered_tokens": filtered_tokens,
        "stemmed_tokens": stemmed_tokens,
        "lemmatized_tokens": lemmatized_tokens,
        "pos_tag_stem": pos_tag_stem,
        "pos_tag_lemma": pos_tag_lemma
    }

# ==============================
# PREPROCESSING (FINAL TEXT)
# ==============================
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r'\W', ' ', text)

    words = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words and word.isalnum()]

    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]

    return ' '.join(words)

# ==============================
# APPLY PREPROCESS
# ==============================
print("\n=== DETAIL PREPROCESSING ===")
for s in sentences:
    result = preprocess_detail(s)
    print("\nText:", s)
    print("Tokens:", result["tokens"])
    print("Filtered:", result["filtered_tokens"])
    print("Stemmed:", result["stemmed_tokens"])
    print("Lemmatized:", result["lemmatized_tokens"])
    print("POS Stem:", result["pos_tag_stem"])

# Final text untuk vectorizer
preprocessed_sentences = [preprocess_text(s) for s in sentences]

print("\n=== PREPROCESSED SENTENCES ===")
print(preprocessed_sentences)

# ==============================
# BAG OF WORDS
# ==============================
vectorizer = CountVectorizer()
X_bow = vectorizer.fit_transform(preprocessed_sentences)

print("\n=== BAG OF WORDS ===")
print("Vocabulary:\n", vectorizer.get_feature_names_out())
print("\nVector vocabulary:\n", vectorizer.vocabulary_)
print("\nBoW Matrix:\n", X_bow.toarray())

# ==============================
# TF-IDF
# ==============================
tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(preprocessed_sentences)

print("\n=== TF-IDF ===")
print("Vocabulary:\n", tfidf_vectorizer.get_feature_names_out())
print("\nVector vocabulary:\n", tfidf_vectorizer.vocabulary_)
print("\nTF-IDF Matrix:\n", X_tfidf.toarray())

# ==============================
# TF-IDF DataFrame
# ==============================
tfidf_df = pd.DataFrame(
    X_tfidf.toarray(),
    columns=tfidf_vectorizer.get_feature_names_out()
)

print("\n=== TF-IDF DataFrame ===")
print(tfidf_df)

# ==============================
# COSINE SIMILARITY
# ==============================
query = "technology data"
query_preprocessed = preprocess_text(query)

query_vector = tfidf_vectorizer.transform([query_preprocessed])

cosine_similarities = cosine_similarity(query_vector, X_tfidf).flatten()

related_docs_indices = cosine_similarities.argsort()[::-1]

print("\n=== COSINE SIMILARITY ===")
print(f"\nQuery: '{query}'\n")

for i in related_docs_indices:
    print(f"Document {i + 1}: {sentences[i]}")
    print(f"Similarity Score: {cosine_similarities[i]:.4f}")
    print("-" * 30)