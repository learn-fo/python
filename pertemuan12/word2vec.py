import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import nltk
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec
import string
import seaborn as sns

# Download NLTK data
@st.cache_resource
def download_nltk_data():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
        nltk.download('punkt_tab')

download_nltk_data()

# Dataset bahasa Indonesia
@st.cache_data
def load_dataset():
    bahasa = [
        "Pemrograman komputer adalah keterampilan yang penting dalam era digital.",
        "Data digunakan untuk analisis dalam berbagai bidang seperti bisnis dan penelitian.",
        "Kecerdasan buatan membantu mengembangkan teknologi baru yang inovatif.",
        "Pembelajaran mesin adalah bagian penting dari kecerdasan buatan modern.",
        "Jaringan internet menghubungkan perangkat di seluruh dunia secara real-time.",
        "Perangkat keras dan perangkat lunak adalah komponen utama komputer.",
        "Sistem informasi mengelola data dan pengetahuan untuk pengambilan keputusan.",
        "Word2Vec adalah model untuk membuat word embedding dalam NLP.",
        "Deep learning memungkinkan komputer mengenali pola kompleks dalam data.",
        "Natural Language Processing membantu komputer memahami bahasa manusia.",
        "Data science menggabungkan statistik, pemrograman, dan pengetahuan bisnis.",
        "Cloud computing menyediakan sumber daya komputasi sesuai permintaan.",
        "Cyber security melindungi sistem dari serangan dan ancaman digital.",
        "Internet of Things menghubungkan perangkat fisik ke internet.",
        "Blockchain adalah teknologi untuk transaksi yang aman dan transparan.",
    ]
    return bahasa

# Training Word2Vec model
@st.cache_resource
def train_word2vec_model(bahasa):
    # Tokenisasi dan preprocessing
    tokenized_data = []
    for text in bahasa:
        tokens = word_tokenize(text.lower())
        # Hapus tanda baca
        tokens = [token for token in tokens if token not in string.punctuation]
        tokenized_data.append(tokens)
    
    # Train model
    model = Word2Vec(
        sentences=tokenized_data,
        vector_size=100,
        window=5,
        min_count=1,
        workers=4,
        sg=0,  # CBOW
        epochs=50
    )
    
    return model, tokenized_data

# Setup halaman
st.set_page_config(
    page_title="Word Vector Visualization",
    page_icon="🔤",
    layout="wide"
)

# Title
st.title("🔤 Word Vector Representations")
st.markdown("Visualisasi dan pencarian word embeddings menggunakan Word2Vec (CBOW)")

# Sidebar
with st.sidebar:
    st.header("⚙️ Informasi Model")
    st.markdown("""
    - **Arsitektur:** CBOW (Continuous Bag of Words)
    - **Dimensi Vektor:** 100
    - **Window Size:** 5
    - **Epochs:** 50
    """)
    
    st.header("📚 Dataset")
    st.markdown(f"**Jumlah kalimat:** 15 kalimat")
    st.markdown("**Topik:** AI, Data Science, Komputer, Teknologi")

# Load dan train model
with st.spinner("Melatih model Word2Vec..."):
    bahasa = load_dataset()
    model, tokenized_data = train_word2vec_model(bahasa)
    vocabulary = list(model.wv.index_to_key)
    # Hapus tanda baca dari vocabulary
    vocabulary = [word for word in vocabulary if word not in string.punctuation]

st.success(f"✅ Model berhasil dilatih! {len(vocabulary)} kata dalam vocabulary")

# Tampilkan vocabulary
with st.expander("📖 Lihat Semua Vocabulary"):
    st.write(f"**Total kata unik:** {len(vocabulary)}")
    cols = st.columns(5)
    for i, word in enumerate(vocabulary):
        cols[i % 5].markdown(f"- `{word}`")

# ==================== FITUR PENCARIAN ====================
st.header("🔍 Pencarian Kata")

col1, col2 = st.columns([2, 1])

with col1:
    search_word = st.text_input(
        "Masukkan kata yang ingin dicari:",
        placeholder="Contoh: komputer, data, ai, pembelajaran",
        value="komputer"
    )

# Cek apakah kata ada di vocabulary
if search_word:
    search_word_lower = search_word.lower()
    
    if search_word_lower in vocabulary:
        st.success(f"✅ Kata '{search_word}' ditemukan dalam vocabulary!")
        
        # Mendapatkan vektor
        vector = model.wv[search_word_lower]
        
        # Menampilkan vektor
        with st.expander(f"📊 Vektor untuk kata '{search_word}' (100 dimensi)", expanded=True):
            st.write(f"**Vektor berdimensi {len(vector)}:**")
            
            # Tampilkan 20 dimensi pertama
            df_vector = pd.DataFrame({
                "Dimensi": [f"d{i+1}" for i in range(20)],
                "Nilai": vector[:20]
            })
            st.dataframe(df_vector, use_container_width=True)
            
            st.caption(f"*Menampilkan 20 dari {len(vector)} dimensi*")
        
        # ==================== KATA YANG MIRIP ====================
        st.subheader(f"🔗 Kata yang mirip dengan '{search_word}'")
        
        similar_words = model.wv.most_similar(search_word_lower, topn=10)
        
        # Tampilkan dalam tabel
        df_similar = pd.DataFrame(similar_words, columns=["Kata", "Similarity Score"])
        df_similar["Similarity Score"] = df_similar["Similarity Score"].apply(lambda x: f"{x:.4f}")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            st.dataframe(df_similar, use_container_width=True, hide_index=True)
        
        with col2:
            # Bar chart untuk skor similarity
            fig, ax = plt.subplots(figsize=(6, 4))
            words = [w[0] for w in similar_words[:5]]
            scores = [w[1] for w in similar_words[:5]]
            colors = plt.cm.Blues(np.linspace(0.4, 0.9, 5))
            ax.barh(words, scores, color=colors)
            ax.set_xlabel("Cosine Similarity Score")
            ax.set_title(f"Top 5 kata mirip dengan '{search_word}'")
            ax.set_xlim(0, 1)
            st.pyplot(fig)
        
    else:
        st.error(f"❌ Kata '{search_word}' tidak ditemukan dalam vocabulary!")
        st.info(f"Kata yang tersedia: {', '.join(vocabulary[:20])}...")

# ==================== VISUALISASI PCA ====================
st.header("📈 Visualisasi Word Vectors (PCA 2D)")

# Pilih kata untuk divisualisasikan
selected_words = st.multiselect(
    "Pilih kata untuk divisualisasikan dalam ruang 2D:",
    vocabulary,
    default=vocabulary[:6] if len(vocabulary) >= 6 else vocabulary
)

if len(selected_words) >= 2:
    # Ambil vektor untuk kata-kata yang dipilih
    vectors = [model.wv[word] for word in selected_words]
    
    # PCA untuk reduksi ke 2D
    pca = PCA(n_components=2)
    vectors_2d = pca.fit_transform(vectors)
    
    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    for i, word in enumerate(selected_words):
        x, y = vectors_2d[i, 0], vectors_2d[i, 1]
        ax.scatter(x, y, s=100, c='blue', alpha=0.7)
        ax.annotate(word, (x, y), fontsize=12, ha='right', va='bottom')
    
    ax.set_title("Visualisasi Word Vectors dengan PCA (Proyeksi 2D)")
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.grid(True, alpha=0.3)
    
    st.pyplot(fig)
    
    # Informasi variance
    st.caption(f"Variance explained: PC1 = {pca.explained_variance_ratio_[0]:.2%}, PC2 = {pca.explained_variance_ratio_[1]:.2%}")
    
elif len(selected_words) == 1:
    st.info("Pilih minimal 2 kata untuk visualisasi PCA")
else:
    st.info("Pilih kata dari daftar di atas untuk memulai visualisasi")

# ==================== MATRIKS SIMILARITAS ====================
st.header("📊 Matriks Similaritas")

# Pilih kata untuk matriks similaritas
matrix_words = st.multiselect(
    "Pilih kata untuk matriks similaritas (max 6 kata):",
    vocabulary,
    default=vocabulary[:4] if len(vocabulary) >= 4 else vocabulary,
    key="matrix_select"
)

if len(matrix_words) >= 2:
    # Hitung matriks similaritas
    n_words = len(matrix_words)
    similarity_matrix = np.zeros((n_words, n_words))
    
    for i, word1 in enumerate(matrix_words):
        for j, word2 in enumerate(matrix_words):
            similarity_matrix[i, j] = model.wv.similarity(word1, word2)
    
    # Tampilkan heatmap
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(similarity_matrix, 
                annot=True, 
                fmt='.3f', 
                xticklabels=matrix_words, 
                yticklabels=matrix_words,
                cmap='coolwarm', 
                vmin=0, 
                vmax=1,
                ax=ax)
    ax.set_title("Cosine Similarity antar Kata")
    st.pyplot(fig)

# ==================== FITUR ANALOGI ====================
with st.expander("🧩 Fitur Analogi Kata (a : b = c : ?)"):
    st.markdown("Cari hubungan analogi kata, contoh: `komputer : pemrograman = data : ?`")
    
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        word_a = st.selectbox("Kata a:", vocabulary, key="analogy_a")
    with col_b:
        word_b = st.selectbox("Kata b:", vocabulary, key="analogy_b")
    with col_c:
        word_c = st.selectbox("Kata c:", vocabulary, key="analogy_c")
    
    if st.button("Cari Analogi"):
        try:
            result = model.wv.most_similar(positive=[word_b, word_c], negative=[word_a], topn=5)
            st.write(f"**{word_a} : {word_b} = {word_c} : ?**")
            st.write("Hasil prediksi:")
            df_result = pd.DataFrame(result, columns=["Kata", "Skor"])
            df_result["Skor"] = df_result["Skor"].apply(lambda x: f"{x:.4f}")
            st.dataframe(df_result, hide_index=True)
        except:
            st.error("Tidak dapat menemukan analogi untuk kata-kata tersebut")

# Footer
st.markdown("---")
st.caption("Aplikasi Word Vector Representations | Menggunakan Word2Vec (CBOW) | Dataset: 15 kalimat tentang teknologi")