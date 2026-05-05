from flask import Flask, render_template, request, flash
import string
import re
import nltk
import os
import numpy as np

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from wordcloud import WordCloud

app = Flask(__name__)
app.secret_key = "secret123"

nltk.download('punkt')
nltk.download('stopwords')

# ======================
# PREPROCESS
# ======================
def preprocess_text(text, custom_stopwords):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r'\W', ' ', text)

    words = word_tokenize(text)

    stop_words = set(stopwords.words('indonesian'))
    stop_words.update(custom_stopwords)

    words = [w for w in words if w not in stop_words and w.isalnum()]

    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    # ✅ STEMMING INDONESIA
    words = [stemmer.stem(w) for w in words]

    return ' '.join(words)

# ======================
# ROUTE
# ======================
@app.route("/", methods=["GET", "POST"])
def index():
    results = None

    if request.method == "POST":
        text_input = request.form.get("text", "")  # ✅ FIX
        stopword_input = request.form.get("stopwords", "")

        custom_stopwords = [w.strip().lower() for w in stopword_input.split(",") if w.strip()]

        if not text_input:
            flash("Input tidak boleh kosong!", "danger")
            return render_template("index.html")

        sentences = text_input.split("\n")

        # ✅ FIX: kirim custom_stopwords
        preprocessed = [preprocess_text(s, custom_stopwords) for s in sentences]

        # ======================
        # BoW
        # ======================
        vectorizer = CountVectorizer()
        X_bow = vectorizer.fit_transform(preprocessed)

        features = vectorizer.get_feature_names_out()

        bow_list = []
        for i, row in enumerate(X_bow.toarray()):
            word_counts = {
                features[j]: int(row[j])
                for j in range(len(features)) if row[j] > 0
            }
            bow_list.append({"doc": i+1, "words": word_counts})

        # ======================
        # TF-IDF
        # ======================
        tfidf_vectorizer = TfidfVectorizer()
        X_tfidf = tfidf_vectorizer.fit_transform(preprocessed)
        tfidf_features = tfidf_vectorizer.get_feature_names_out()

        # ======================
        # WORDCLOUD
        # ======================
        os.makedirs("static", exist_ok=True)  # ✅ FIX

        all_text = " ".join(preprocessed)
        wc = WordCloud(width=800, height=400, background_color='white').generate(all_text)
        wc.to_file("static/wordcloud.png")

        # ======================
        # TOP 10 TF-IDF
        # ======================
        tfidf_array = X_tfidf.toarray()
        mean_tfidf = np.mean(tfidf_array, axis=0)

        top_indices = mean_tfidf.argsort()[::-1][:10]

        top_tfidf = [
            {
                "word": tfidf_features[i],
                "score": round(float(mean_tfidf[i]), 4)
            }
            for i in top_indices
        ]

        flash("Analisis berhasil dilakukan!", "success")

        results = {
            "sentences": sentences,
            "preprocessed": preprocessed,
            "bow_list": bow_list,
            "tfidf": X_tfidf.toarray().tolist(),
            "tfidf_features": tfidf_features.tolist(),
            "top_tfidf": top_tfidf,
            "custom_stopwords": custom_stopwords  # ✅ tampilkan
        }

    return render_template("index.html", results=results)

# ======================
# SEARCH COSINE ROUTE
# ======================
@app.route("/search", methods=["POST"])
def search():
    query = request.form.get("query")
    sentences = request.form.getlist("sentences[]")
    stopwords_input = request.form.getlist("stopwords[]")

    custom_stopwords = [w.strip().lower() for w in stopwords_input if w.strip()]

    if not query:
        return {"error": "Query kosong"}

    # ✅ FIX: kirim stopword
    preprocessed_sentences = [
        preprocess_text(s, custom_stopwords) for s in sentences
    ]

    tfidf_vectorizer = TfidfVectorizer()
    X_tfidf = tfidf_vectorizer.fit_transform(preprocessed_sentences)

    query_vec = tfidf_vectorizer.transform([
        preprocess_text(query, custom_stopwords)
    ])

    cosine_sim = cosine_similarity(query_vec, X_tfidf).flatten()

    results = []
    for i, score in enumerate(cosine_sim):
        results.append({
            "doc": i+1,
            "text": sentences[i],
            "score": round(float(score), 4)
        })

    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return {"results": results}

if __name__ == "__main__":
    app.run(debug=True)