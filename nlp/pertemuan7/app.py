import re
import random
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import joblib

from wordcloud import WordCloud

# NLP
from sklearn.feature_extraction.text import CountVectorizer

# Sastrawi
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import (
    StopWordRemoverFactory
)

# BERTopic
from bertopic import BERTopic
from umap import UMAP
import hdbscan

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="BERTopic Offline Dashboard",
    layout="wide"
)

# =========================================================
# SESSION STATE
# =========================================================
if "data" not in st.session_state:
    st.session_state.data = None

if "model" not in st.session_state:
    st.session_state.model = None

if "topics" not in st.session_state:
    st.session_state.topics = None

# =========================================================
# TITLE
# =========================================================
st.title("📊 BERTopic NLP")

# =========================================================
# DATASET
# =========================================================
TOPICS = {

    "Teknologi": [
        "AI mengubah industri digital",
        "machine learning membantu bisnis",
        "cloud computing modern",
        "perkembangan sistem informasi",
        "robotika meningkatkan otomatisasi",
        "big data membantu analisis"
    ],

    "Ekonomi": [
        "inflasi global meningkat",
        "investasi saham berkembang",
        "krisis ekonomi dunia",
        "pertumbuhan ekonomi stabil",
        "pasar modal berkembang",
        "nilai tukar mata uang berubah"
    ],

    "Kesehatan": [
        "vaksin meningkatkan imun tubuh",
        "gaya hidup sehat penting",
        "olahraga membantu kesehatan",
        "penyakit virus menyebar cepat",
        "nutrisi seimbang penting",
        "rumah sakit meningkatkan layanan"
    ],

    "Pendidikan": [
        "e learning berkembang pesat",
        "kurikulum digital modern",
        "platform belajar online",
        "teknologi pendidikan sekolah",
        "mahasiswa belajar pemrograman",
        "universitas mengembangkan riset"
    ],

    "Lingkungan": [
        "perubahan iklim global",
        "polusi udara meningkat",
        "energi terbarukan penting",
        "deforestasi hutan terjadi",
        "sampah plastik mencemari laut",
        "pemanasan global meningkat"
    ]
}

NOISE = [
    "@@@",
    "###",
    "$$$",
    "!!!",
    "???",
    "***",
    "%%%"
]

# =========================================================
# ADD NOISE
# =========================================================
def add_noise(text):

    noise_text = " ".join(
        random.choices(
            NOISE,
            k=random.randint(1, 3)
        )
    )

    return f"{text} {noise_text}"

# =========================================================
# GENERATE DATASET
# =========================================================
def generate_dataset(n=50):

    docs = []
    labels = []

    topic_names = list(TOPICS.keys())

    for _ in range(n):

        topic = random.choice(topic_names)

        sentence = random.choice(
            TOPICS[topic]
        )

        noisy_sentence = add_noise(sentence)

        docs.append(noisy_sentence)

        labels.append(topic)

    return pd.DataFrame({
        "text": docs,
        "label": labels
    })

# =========================================================
# SASTRAWI PREPROCESSING
# =========================================================

# stemmer
stemmer_factory = StemmerFactory()
stemmer = stemmer_factory.create_stemmer()

# stopword
stop_factory = StopWordRemoverFactory()
stopwords = stop_factory.get_stop_words()

# custom stopwords
custom_stopwords = set(stopwords).union({

    "dan",
    "yang",
    "di",
    "ke",
    "dari",
    "untuk",
    "pada",
    "dengan"

})

# =========================================================
# CLEAN TEXT
# =========================================================
def clean_text(text):

    # lowercase
    text = text.lower()

    # remove special characters
    text = re.sub(
        r"[^a-zA-Z0-9\s]",
        " ",
        text
    )

    # remove number
    text = re.sub(
        r"\d+",
        " ",
        text
    )

    # remove extra spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    # tokenization
    tokens = text.split()

    # stopword removal
    tokens = [
        word
        for word in tokens
        if word not in custom_stopwords
    ]

    # join text
    text = " ".join(tokens)

    # stemming
    text = stemmer.stem(text)

    return text

# =========================================================
# WORD CLOUD
# =========================================================
def create_wordcloud(model, topic_id):

    words = dict(
        model.get_topic(topic_id)
    )

    wc = WordCloud(
        width=800,
        height=400,
        background_color="white"
    ).generate_from_frequencies(words)

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.imshow(
        wc,
        interpolation="bilinear"
    )

    ax.axis("off")

    return fig

# =========================================================
# TRAIN MODEL
# =========================================================
@st.cache_resource
def train_model(docs):

    # preprocessing
    cleaned_docs = [
        clean_text(doc)
        for doc in docs
    ]

    # =====================================================
    # TOKENIZER / EMBEDDING
    # =====================================================
    vectorizer_model = CountVectorizer()

    # =====================================================
    # DIMENSIONALITY REDUCTION
    # =====================================================
    umap_model = UMAP(
        n_neighbors=10,
        n_components=5,
        min_dist=0.0,
        metric="cosine",
        random_state=42
    )

    # =====================================================
    # CLUSTERING
    # =====================================================
    hdbscan_model = hdbscan.HDBSCAN(
        min_cluster_size=2,
        metric="euclidean",
        cluster_selection_method="eom",
        prediction_data=True
    )

    # =====================================================
    # BERTopic
    # =====================================================
    topic_model = BERTopic(

        vectorizer_model=vectorizer_model,

        umap_model=umap_model,

        hdbscan_model=hdbscan_model,

        calculate_probabilities=False,

        verbose=False
    )

    topics, probs = topic_model.fit_transform(
        cleaned_docs
    )

    return (
        topic_model,
        topics,
        probs,
        cleaned_docs
    )

# =========================================================
# GENERATE DATA
# =========================================================
if st.button("🎲 Generate 50 Documents"):

    st.session_state.data = generate_dataset(50)

# first load
if st.session_state.data is None:

    st.session_state.data = generate_dataset(50)

# =========================================================
# SHOW RAW DATASET
# =========================================================
st.header("📄 Raw Dataset")

st.dataframe(
    st.session_state.data,
    use_container_width=True
)

# =========================================================
# PREPROCESSING RESULT
# =========================================================
st.header("🧹 Preprocessing Result")

preview_df = st.session_state.data.copy()

preview_df["Before"] = preview_df["text"]

preview_df["After"] = preview_df["text"].apply(
    clean_text
)

preview_df = preview_df[
    [
        "label",
        "Before",
        "After"
    ]
]

st.dataframe(
    preview_df.head(15),
    use_container_width=True
)

# =========================================================
# PREPROCESSING STATS
# =========================================================
st.subheader("📊 Statistik Preprocessing")

col1, col2, col3 = st.columns(3)

before_chars = preview_df[
    "Before"
].str.len().mean()

after_chars = preview_df[
    "After"
].str.len().mean()

noise_removed = before_chars - after_chars

col1.metric(
    "Avg Char Before",
    round(before_chars, 2)
)

col2.metric(
    "Avg Char After",
    round(after_chars, 2)
)

col3.metric(
    "Noise Removed",
    round(noise_removed, 2)
)

# =========================================================
# TRAIN MODEL
# =========================================================
if st.button("🚀 Train BERTopic Model"):

    with st.spinner("Training BERTopic..."):

        (
            model,
            topics,
            probs,
            cleaned_docs
        ) = train_model(
            st.session_state.data["text"].tolist()
        )

        st.session_state.model = model
        st.session_state.topics = topics

        # save model
        joblib.dump(
            model,
            "bertopic_model.pkl"
        )

    st.success(
        "✅ Model berhasil dilatih & disimpan!"
    )

# =========================================================
# CHECK MODEL
# =========================================================
if st.session_state.model is None:

    st.warning(
        "⚠ Klik tombol TRAIN BERTopic MODEL terlebih dahulu."
    )

    st.stop()

# =========================================================
# MODEL
# =========================================================
model = st.session_state.model

# =========================================================
# VISUALIZATION DASHBOARD
# =========================================================
st.header("📊 Topic Visualization Dashboard")

col1, col2 = st.columns([2, 1])

# =========================================================
# INTERTOPIC MAP
# =========================================================
with col1:

    st.subheader("📌 Intertopic Distance Map")

    fig_topics = model.visualize_topics()

    st.plotly_chart(
        fig_topics,
        use_container_width=True
    )

# =========================================================
# WORD CLOUD
# =========================================================
with col2:

    st.subheader("☁ WordCloud")

    topic_ids = [

        topic
        for topic in model.get_topics().keys()

        if topic != -1
    ]

    selected_topic = st.selectbox(
        "Pilih Topic",
        topic_ids
    )

    fig_wc = create_wordcloud(
        model,
        selected_topic
    )

    st.pyplot(fig_wc)

# =========================================================
# TOPIC WORD SCORES
# =========================================================
st.header("📊 Topic Word Scores")

fig_bar = model.visualize_barchart(
    top_n_topics=5
)

st.plotly_chart(
    fig_bar,
    use_container_width=True
)

# =========================================================
# TOPIC INFO
# =========================================================
st.header("📑 Topic Information")

topic_info = model.get_topic_info()

st.dataframe(
    topic_info,
    use_container_width=True
)

# =========================================================
# INFERENCING
# =========================================================
st.header("🔎 Inferencing")

query = st.text_input(
    "Masukkan teks untuk prediksi topic"
)

if query:

    cleaned_query = clean_text(query)

    topics, probs = model.transform(
        [cleaned_query]
    )

    predicted_topic = int(
        topics[0]
    )

    st.subheader("📌 Hasil Prediksi")

    st.write(
        "Predicted Topic ID:",
        predicted_topic
    )

    # =====================================================
    # TOP WORDS
    # =====================================================
    if predicted_topic != -1:

        topic_words = model.get_topic(
            predicted_topic
        )

        st.subheader("🔑 Top Words")

        filtered_words = [

            (word, score)

            for word, score in topic_words

            if (
                str(word).strip() != ""
                and word.isalpha()
                and len(word) > 2
            )
        ]

        words_df = pd.DataFrame(
            filtered_words,
            columns=["Word", "Score"]
        )

        st.dataframe(
            words_df,
            use_container_width=True
        )

        # =================================================
        # WORD CLOUD INFERENCE
        # =================================================
        st.subheader("☁ WordCloud Prediction")

        fig_pred_wc = create_wordcloud(
            model,
            predicted_topic
        )

        st.pyplot(fig_pred_wc)

    else:

        st.warning(
            "Dokumen dianggap noise/outlier."
        )

# =========================================================
# FOOTER
# =========================================================
st.markdown("---")
