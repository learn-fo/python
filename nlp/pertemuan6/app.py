from flask import Flask, render_template, request, jsonify
import os, re, nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

from gensim import corpora, models
from wordcloud import WordCloud

app = Flask(__name__)

nltk.download('punkt')
nltk.download('stopwords')

# ======================
# SETUP
# ======================
os.makedirs("lda_model", exist_ok=True)
os.makedirs("static", exist_ok=True)

DICT_PATH = "lda_model/dict.dict"
MODEL_PATH = "lda_model/model.model"

# ======================
# DATASET
# ======================
documents = [
    # Teknologi
    "Transformasi digital mengubah bisnis global",
    "Teknologi membantu perkembangan pasar digital",
    "Startup menciptakan inovasi teknologi modern",
    "Sistem digital meningkatkan efisiensi bisnis",

    # Ekonomi
    "Ekonomi nasional dipengaruhi inflasi dan pasar",
    "Bisnis berkembang melalui investasi",
    "Pemerintah mengatur kebijakan ekonomi",
    "Pasar global meningkatkan pertumbuhan ekonomi",

    # Kesehatan
    "Rumah sakit melayani pasien",
    "Dokter menangani penyakit",
    "Kesehatan masyarakat penting",
    "Obat membantu penyembuhan",

    # Pendidikan
    "Sekolah meningkatkan kualitas pendidikan",
    "Guru mengajar siswa",
    "Mahasiswa belajar di universitas",
    "Kurikulum membantu pembelajaran"
]

# ======================
# PREPROCESS
# ======================
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)

    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('indonesian'))

    tokens = [t for t in tokens if t not in stop_words]
    tokens = [stemmer.stem(t) for t in tokens]

    return tokens

texts = [preprocess(d) for d in documents]

# ======================
# LDA MODEL
# ======================
if not os.path.exists(MODEL_PATH):
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(t) for t in texts]

    lda_model = models.LdaModel(
        corpus=corpus,
        num_topics=4,
        id2word=dictionary,
        passes=30,
        random_state=42
    )

    dictionary.save(DICT_PATH)
    lda_model.save(MODEL_PATH)
else:
    dictionary = corpora.Dictionary.load(DICT_PATH)
    lda_model = models.LdaModel.load(MODEL_PATH)
    corpus = [dictionary.doc2bow(t) for t in texts]

# ======================
# WORDCLOUD
# ======================
def generate_wc():
    text = " ".join([" ".join(t) for t in texts])
    wc = WordCloud(width=800, height=400, background_color="white").generate(text)
    wc.to_file("static/global_wc.png")

generate_wc()

# ======================
# LABEL TOPIK
# ======================
topic_names = {
    0: "Teknologi",
    1: "Ekonomi",
    2: "Kesehatan",
    3: "Pendidikan"
}

# ======================
# HOME
# ======================
@app.route("/")
def index():
    topics = [{"id": i, "name": topic_names[i]} for i in range(4)]
    return render_template("index.html", topics=topics, documents=documents)

# ======================
# DETAIL TOPIK
# ======================
@app.route("/topic/<int:id>")
def topic_detail(id):
    words = lda_model.show_topic(id, topn=10)

    return jsonify({
        "topic": topic_names[id],
        "words": [{"word": w, "score": float(round(s,4))} for w,s in words]
    })

# ======================
# SEARCH (INFERENCING)
# ======================
@app.route("/search", methods=["POST"])
def search():
    query = request.form.get("query")

    tokens = preprocess(query)
    bow = dictionary.doc2bow(tokens)

    query_topics = lda_model.get_document_topics(bow)

    def vec(topics):
        v = [0]*lda_model.num_topics
        for t,s in topics:
            v[t] = s
        return v

    q_vec = vec(query_topics)

    results = []

    for i, doc_bow in enumerate(corpus):

        d_topics = lda_model.get_document_topics(doc_bow)
        d_vec = vec(d_topics)

        # cosine similarity
        dot = sum(q*d for q,d in zip(q_vec, d_vec))
        norm_q = sum(q*q for q in q_vec) ** 0.5
        norm_d = sum(d*d for d in d_vec) ** 0.5

        score = dot/(norm_q*norm_d) if norm_q and norm_d else 0

        # ======================
        # FIX MATCH WORD (PENTING)
        # ======================
        doc_tokens = texts[i]
        matched_words = [w for w in tokens if w in doc_tokens]

        # ======================
        # SEMUA TOPIK
        # ======================
        topics_detail = [
            {
                "name": topic_names.get(t),
                "score": round(float(s),4)
            }
            for t, s in d_topics
        ]

        results.append({
            "doc_id": i + 1,
            "doc": documents[i],
            "score": float(round(score,4)),
            "reason": {
                "topics": topics_detail,
                "matched_words": matched_words
            }
        })

    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return jsonify({
        "query_tokens": tokens,
        "documents": results
    })

# ======================
# RUN
# ======================
if __name__ == "__main__":
    app.run(debug=True)