# TEXT PROCESSING
import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.corpus import wordnet

# Download required NLTK data (jalankan sekali)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('punkt_tab')
    nltk.download('punkt')

# ============================================================
# DATASET 500 KATA
# ============================================================

dataset_kalimat = [
    "Saya sangat suka belajar Python programming language hari ini!",
    "Dia tidak pernah datang ke tempat itu karena terlalu jauh sekali.",
    "Mereka sedang makan bakso dan minum es teh di warung favorit.",
    "Apakah kamu sudah mengerjakan tugas PR yang diberikan guru kemarin?",
    "Cuaca hari ini sangat panas, tetapi saya tetap pergi ke kantor.",
    "Buku itu sangat bagus dan menarik untuk dibaca oleh semua orang.",
    "Dia berlari sangat cepat sekali sehingga tidak ada yang bisa mengejarnya.",
    "Kami akan pergi ke pantai minggu depan bersama keluarga besar.",
    "Makanan di restoran ini enak-enak semua, terutama sambalnya pedas!",
    "Jangan pernah menyerah pada impianmu karena usaha tidak pernah mengkhianati hasil.",
    "Dia adalah seorang programmer yang sangat handal dan berpengalaman.",
    "Kucing itu tidur sepanjang hari di atas sofa kesayangannya.",
    "Mobil baru ayah sangat mahal dan mewah dengan fitur canggih.",
    "Saya tidak suka dengan perilakunya yang kasar dan tidak sopan.",
    "Mereka bertiga pergi ke bioskop untuk menonton film terbaru.",
    "Hujan turun sangat deras sejak tadi sore sampai malam hari.",
    "Dia memenangkan perlombaan lari setelah berlatih keras setiap hari.",
    "Kami sekeluarga sedang berlibur ke Bali selama satu minggu.",
    "Kue buatan ibu sangat lezat dan tidak pernah gagal membuat ketagihan.",
    "Dia selalu datang tepat waktu ke sekolah setiap pagi tanpa terlambat.",
    "Mereka sedang membangun rumah baru di dekat sungai yang indah.",
    "Saya harus segera menyelesaikan pekerjaan ini sebelum batas waktu.",
    "Anak-anak itu bermain bola di lapangan sampai sore menjelang.",
    "Dia sangat pandai bermain gitar dan suaranya merdu sekali.",
    "Kami akan mengadakan pesta ulang tahun di rumah minggu depan.",
    "Dia tidak pernah mengeluh meskipun pekerjaannya sangat berat sekali.",
    "Mereka berlima sedang belajar bersama untuk ujian besok pagi.",
    "Bunga-bunga di taman itu mekar sangat indah dan wangi.",
    "Saya membeli smartphone baru dengan kamera yang sangat jernih.",
    "Dia tersenyum bahagia ketika melihat hadiah kejutan dari sahabatnya.",
    "Kita harus selalu bersyukur atas nikmat yang diberikan Tuhan.",
    "Mereka sedang berdebat tentang topik yang sangat serius dan penting.",
    "Saya tidak pernah menyangka bahwa dia bisa berubah menjadi lebih baik.",
    "Dia berlari pagi setiap hari untuk menjaga kesehatan tubuhnya.",
    "Kami sekelas sedang membersihkan ruangan setelah pelajaran selesai.",
    "Dia jatuh cinta pada pandangan pertama dengan gadis itu.",
    "Mereka memutuskan untuk berhenti bekerja sama karena ada konflik.",
    "Saya sedang membaca novel karya Tere Liye yang sangat inspiratif.",
    "Dia selalu membantu orang lain tanpa mengharapkan imbalan apapun.",
    "Cuaca dingin membuat saya ingin minum kopi hangat sekaligus.",
    "Mereka sedang mempersiapkan acara pernikahan yang sangat meriah.",
    "Saya tidak bisa tidur semalaman karena memikirkan masalah itu.",
    "Dia sangat mahir dalam memasak berbagai masakan tradisional Indonesia.",
    "Kami pergi ke pasar tradisional untuk membeli sayur dan buah.",
    "Dia menangis tersedu-sedu setelah menonton film yang sangat mengharukan.",
    "Mereka berhasil mencapai puncak gunung setelah perjuangan yang panjang.",
    "Saya selalu mencuci tangan sebelum makan agar terhindar dari kuman.",
    "Dia sangat percaya diri saat presentasi di depan banyak orang.",
    "Kami akan merayakan tahun baru di rumah nenek di desa.",
    "Dia tidak pernah membuang sampah sembarangan karena peduli lingkungan.",
    "Mereka berteman sejak kecil dan sampai sekarang masih dekat sekali.",
    "Saya sedang belajar mengemudi mobil agar bisa mandiri nantinya.",
    "Dia selalu memakai helm ketika naik motor demi keselamatan.",
    "Kami sekeluarga sering berkumpul setiap malam minggu bersama-sama.",
    "Dia sangat menyukai musik klasik karena terasa menenangkan jiwa.",
    "Mereka sedang berlibur ke Jogja selama tiga hari dua malam.",
    "Saya harus membayar tagihan listrik sebelum tanggal 20 setiap bulan.",
    "Dia tidak sengaja menumpahkan kopi di atas meja kerja barunya.",
    "Kami berencana untuk membuka usaha kecil-kecilan tahun depan nanti.",
    "Dia sangat rajin menabung sejak dini untuk masa depan kelak.",
    "Mereka sedang menonton pertandingan sepak bola di televisi rumah.",
    "Saya selalu memeriksa ban mobil sebelum melakukan perjalanan jauh.",
    "Dia tidak pernah memakai gincu karena lebih suka tampil alami.",
    "Kami sedang menyusun rencana bisnis untuk perusahaan startup baru.",
    "Dia sangat suka berenang di kolam renang saat cuaca panas.",
    "Mereka harus segera menyelesaikan proyek ini sebelum deadline tiba.",
    "Saya tidak pernah lupa mengucapkan terima kasih atas bantuan yang diberikan.",
    "Dia sangat gemar mengoleksi perangko dari berbagai negara di dunia.",
    "Kami sekeluarga sedang menikmati makan malam di restoran mewah.",
    "Dia tidak suka dengan makanan pedas karena perutnya cepat sakit.",
    "Mereka sedang mendiskusikan ide-ide baru untuk pengembangan produk.",
    "Saya selalu menyiapkan bekal sebelum berangkat ke kantor pagi.",
    "Dia sangat cerdas dan selalu menjadi juara kelas setiap semester.",
    "Kami akan mengunjungi pameran teknologi di Jakarta bulan depan."
]

# Hitung total kata dalam dataset
total_kata_awal = sum(len(kalimat.split()) for kalimat in dataset_kalimat)
print("=" * 80)
print("TEXT PROCESSING")
print("=" * 80)
print(f"\nDATASET:")
print(f"   - Jumlah kalimat: {len(dataset_kalimat)}")
print(f"   - Perkiraan jumlah kata: ±{total_kata_awal} kata")
print(f"   - Total karakter: {sum(len(k) for k in dataset_kalimat)}")

# Tampilkan 5 kalimat pertama
print("\n5 KALIMAT PERTAMA DATASET:")
print("-" * 50)
for i, kal in enumerate(dataset_kalimat[:5], 1):
    print(f"   {i}. {kal}")

print("\n" + "=" * 80)
print("PROSES TEXT PROCESSING DIMULAI")
print("=" * 80)

# Gabungkan semua kalimat menjadi satu teks
text = " ".join(dataset_kalimat)
print(f"\nTOTAL TEKS: {len(text)} karakter, {len(text.split())} kata")


# ============================================================
# 1. NORMALIZATION / LOWERCASING
# ============================================================
print("\n" + "=" * 80)
print("1. NORMALIZATION / LOWERCASING (Mengubah ke huruf kecil)")
print("=" * 80)

text_lower = text.lower()
print(f"Hasil Lowercasing (200 karakter pertama):")
print(f"   {text_lower[:200]}...")
print(f"\n   - Sebelum: BANYAK HURUF BESAR")
print(f"   - Sesudah: semua huruf menjadi kecil")


# ============================================================
# 2. PUNCTUATION REMOVAL (Menghapus tanda baca)
# ============================================================
print("\n" + "=" * 80)
print("2. PUNCTUATION REMOVAL (Menghapus tanda baca)")
print("=" * 80)

# Tanda baca yang akan dihapus
punctuation = r'[^\w\s]'

# Hapus semua tanda baca (.,!?;:()[]{}'"<>/@#$%^&*)
text_no_punct = re.sub(punctuation, '', text_lower)
print(" Tanda baca yang dihapus: .,!?;:()[]{}'\"<>/@#$%^&*")
print(f"\n   Hasil (200 karakter pertama):")
print(f"   {text_no_punct[:200]}...")
print(f"\n   - Sebelum: Python programming language hari ini!")
print(f"   - Sesudah: python programming language hari ini")


# ============================================================
# 3. SEGMENTATION / TOKENIZATION (Memecah kata per kata)
# ============================================================
print("\n" + "=" * 80)
print("3. SEGMENTATION / TOKENIZATION (Memecah menjadi token/kata)")
print("=" * 80)

tokens = word_tokenize(text_no_punct)
print(f"Jumlah token/kata: {len(tokens)}")
print(f"\n   30 token pertama:")
print(f"   {tokens[:30]}")
print(f"\n   30 token terakhir:")
print(f"   {tokens[-30:]}")


# ============================================================
# 4. STOPWORD REMOVAL (Menghapus kata umum)
# ============================================================
print("\n" + "=" * 80)
print("4. STOPWORD REMOVAL (Menghapus kata umum)")
print("=" * 80)

# Daftar stopword bahasa Indonesia (manual)
stopwords_id = {
    'saya', 'anda', 'kamu', 'dia', 'mereka', 'kami', 'kita', 'aku', 'ia',
    'ini', 'itu', 'tersebut', 'yang', 'dan', 'atau', 'tetapi', 'namun',
    'sedangkan', 'karena', 'sehingga', 'maka', 'jika', 'kalau', 'bahwa',
    'adalah', 'ialah', 'untuk', 'dari', 'ke', 'di', 'pada', 'dengan',
    'oleh', 'sebagai', 'dalam', 'kepada', 'sangat', 'sekali', 'begitu',
    'saja', 'pun', 'juga', 'sudah', 'telah', 'sedang', 'masih', 'akan',
    'bisa', 'dapat', 'boleh', 'harus', 'perlu', 'tidak', 'tak', 'bukan',
    'belum', 'pernah', 'selalu', 'sering', 'kadang', 'kadang-kadang',
    'apakah', 'ya', 'tentu', 'tentunya', 'sebenarnya', 'terlalu', 'sangat',
    'tadi', 'kemarin', 'hari', 'kemudian', 'lalu', 'sekarang', 'besok',
    'dulu', 'telah', 'baru', 'lagi', 'terus', 'sebelum', 'sesudah',
    'saat', 'ketika', 'sementara', 'selama', 'hingga', 'sampai', 'semenjak'
}

tokens_no_stopwords = [word for word in tokens if word not in stopwords_id]
print(f"Jumlah stopword yang dihapus: {len(tokens) - len(tokens_no_stopwords)}")
print(f"Jumlah token setelah stopword removal: {len(tokens_no_stopwords)}")
print(f"\n   Contoh stopword yang dihapus: 'saya', 'dan', 'di', 'ke', 'yang', 'ini', 'itu'")
print(f"\n   30 token pertama tanpa stopword:")
print(f"   {tokens_no_stopwords[:30]}")


# ============================================================
# 5. STEMMING (Mengubah kata berimbuhan ke kata dasar - bahasa Indonesia)
# ============================================================
print("\n" + "=" * 80)
print("5. STEMMING (Mengubah kata berimbuhan ke bentuk dasar)")
print("=" * 80)

# Fungsi stemming sederhana untuk bahasa Indonesia
def stem_bahasa_indonesia(word):
    """Stemming sederhana untuk bahasa Indonesia"""
    # Awalan (prefixes)
    prefixes = ['meng', 'meny', 'men', 'mem', 'me', 'ber', 'belajar', 'di', 'ke', 'se', 'ter', 'per']
    # Akhiran (suffixes)
    suffixes = ['kan', 'an', 'i', 'lah', 'pun', 'nya']
    
    stemmed = word
    
    # Hapus akhiran
    for suffix in suffixes:
        if stemmed.endswith(suffix) and len(stemmed) > len(suffix) + 2:
            stemmed = stemmed[:-len(suffix)]
            break
    
    # Hapus awalan
    for prefix in prefixes:
        if stemmed.startswith(prefix) and len(stemmed) > len(prefix) + 2:
            stemmed = stemmed[len(prefix):]
            break
    
    # Aturan khusus untuk kata yang mulai dengan 'pe' atau 'se'
    if stemmed.startswith('pe') and len(stemmed) > 4:
        if stemmed[2] not in 'aeiou':
            stemmed = stemmed[2:]
    
    return stemmed if len(stemmed) > 1 else word

# Stemming untuk semua token
stemmed_tokens = [stem_bahasa_indonesia(word) for word in tokens_no_stopwords]

print(f"Contoh stemming kata bahasa Indonesia:")
print(f"   'belajar'      → {stem_bahasa_indonesia('belajar')}")
print(f"   'pergi'        → {stem_bahasa_indonesia('pergi')}")
print(f"   'makanan'      → {stem_bahasa_indonesia('makanan')}")
print(f"   'menulis'      → {stem_bahasa_indonesia('menulis')}")
print(f"   'permainan'    → {stem_bahasa_indonesia('permainan')}")
print(f"   'kegiatan'     → {stem_bahasa_indonesia('kegiatan')}")
print(f"   'sebenarnya'   → {stem_bahasa_indonesia('sebenarnya')}")

print(f"\n   30 token setelah stemming:")
print(f"   {stemmed_tokens[:30]}")


# ============================================================
# 6. LEMMATIZATION (Mengubah ke bentuk kata dasar/dictionary form)
# ============================================================
print("\n" + "=" * 80)
print("6. LEMMATIZATION (Mengubah ke kata dasar - kamus)")
print("=" * 80)

# Inisialisasi lemmatizer (untuk bahasa Inggris, contoh demonstrasi)
lemmatizer = WordNetLemmatizer()

# Fungsi untuk menentukan POS tag WordNet
def get_wordnet_pos(word):
    """Convert NLTK POS tag to WordNet POS tag"""
    tag = pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

# Lemmatization untuk token yang sudah di-stem
lemmatized_tokens = []
for word in stemmed_tokens[:100]:  # Contoh 100 kata pertama
    if len(word) > 2:
        pos = get_wordnet_pos(word)
        lemmatized = lemmatizer.lemmatize(word, pos=pos)
        lemmatized_tokens.append(lemmatized)
    else:
        lemmatized_tokens.append(word)

print(f"Contoh lemmatization (bahasa Inggris - demonstrasi):")
print(f"   'running'  → {lemmatizer.lemmatize('running', pos=wordnet.VERB)}")
print(f"   'better'   → {lemmatizer.lemmatize('better', pos=wordnet.ADJ)}")
print(f"   'geese'    → {lemmatizer.lemmatize('geese', pos=wordnet.NOUN)}")

print(f"\n Catatan: Lemmatization penuh memerlukan resource bahasa Indonesia")
print(f"   Hasil lemmatization untuk 100 kata pertama (menggunakan WordNet):")
print(f"   {lemmatized_tokens[:30]}")


# ============================================================
# 7. PART-OF-SPEECH TAGGING (Menandai jenis kata)
# ============================================================
print("\n" + "=" * 80)
print("7. PART-OF-SPEECH TAGGING (Menandai jenis kata)")
print("=" * 80)

# POS Tagging pada token asli (sebelum stopword removal)
pos_tags = pos_tag(tokens[:100])  # 100 kata pertama

print(f"Keterangan POS Tag (Universal POS Tags):")
print(f"   CC  - Conjunction (kata sambung: dan, atau)")
print(f"   CD  - Cardinal number (angka: satu, dua, 10)")
print(f"   DT  - Determiner (kata penentu: ini, itu, tersebut)")
print(f"   IN  - Preposition (kata depan: di, ke, dari)")
print(f"   JJ  - Adjective (kata sifat: baik, cantik, besar)")
print(f"   NN  - Noun (kata benda: buku, rumah, mobil)")
print(f"   RB  - Adverb (kata keterangan: sangat, cepat, disana)")
print(f"   VB  - Verb (kata kerja: makan, lari, tidur)")
print(f"   PRP - Pronoun (kata ganti: saya, kamu, dia)")
print(f"   UH  - Interjection (kata seru: wah, aduh)")

print(f"\nContoh POS Tagging untuk 50 kata pertama:")
print("-" * 70)
print(f"{'Kata':<20} {'POS Tag':<12} {'Jenis Kata':<30}")
print("-" * 70)

pos_descriptions = {
    'CC': 'Conjunction', 'CD': 'Number', 'DT': 'Determiner', 'EX': 'Existential',
    'FW': 'Foreign', 'IN': 'Preposition', 'JJ': 'Adjective', 'JJR': 'Comparative',
    'JJS': 'Superlative', 'LS': 'List', 'MD': 'Modal', 'NN': 'Noun', 'NNS': 'Plural Noun',
    'NNP': 'Proper Noun', 'NNPS': 'Plural Proper', 'PDT': 'Predeterminer',
    'POS': 'Possessive', 'PRP': 'Pronoun', 'PRP$': 'Possessive Pronoun',
    'RB': 'Adverb', 'RBR': 'Comparative Adv', 'RBS': 'Superlative Adv',
    'RP': 'Particle', 'SYM': 'Symbol', 'TO': 'to', 'UH': 'Interjection',
    'VB': 'Verb', 'VBD': 'Past Verb', 'VBG': 'Gerund', 'VBN': 'Past Participle',
    'VBP': 'Present Verb', 'VBZ': '3rd Person Singular', 'WDT': 'Wh-determiner',
    'WP': 'Wh-pronoun', 'WP$': 'Possessive Wh', 'WRB': 'Wh-adverb'
}

for word, tag in pos_tags[:50]:
    desc = pos_descriptions.get(tag, 'Other')
    print(f"{word:<20} {tag:<12} {desc:<30}")


# ============================================================
# FREKUENSI KATA SETELAH CLEANING
# ============================================================
print("\n" + "=" * 80)
print("FREKUENSI KATA (Setelah Stopword Removal)")
print("=" * 80)

from collections import Counter

word_freq = Counter(tokens_no_stopwords)
print(f"\n10 Kata Paling Sering Muncul:")
print("-" * 40)
for word, count in word_freq.most_common(10):
    print(f"   {word:<15} → {count} kali")


# ============================================================
# SIMPAN HASIL KE FILE
# ============================================================
print("\n" + "=" * 80)
print("MENYIMPAN HASIL TEXT PROCESSING")
print("=" * 80)

# Simpan hasil processing ke file
with open('pertemuan3\hasil_text_processing.txt', 'w', encoding='utf-8') as f:
    f.write("=" * 60 + "\n")
    f.write("HASIL TEXT PROCESSING\n")
    f.write("=" * 60 + "\n\n")
    
    f.write("1. DATA AWAL:\n")
    f.write(f"   {text[:500]}...\n\n")
    
    f.write("2. SETELAH LOWERCASING:\n")
    f.write(f"   {text_lower[:500]}...\n\n")
    
    f.write("3. SETELAH PUNCTUATION REMOVAL:\n")
    f.write(f"   {text_no_punct[:500]}...\n\n")
    
    f.write("4. TOKENS (100 pertama):\n")
    f.write(f"   {tokens[:100]}\n\n")
    
    f.write("5. TOKENS TANPA STOPWORD (100 pertama):\n")
    f.write(f"   {tokens_no_stopwords[:100]}\n\n")
    
    f.write("6. HASIL STEMMING (100 pertama):\n")
    f.write(f"   {stemmed_tokens[:100]}\n\n")
    
    f.write("7. HASIL LEMMATIZATION (100 pertama):\n")
    f.write(f"   {lemmatized_tokens[:100]}\n\n")
    
    f.write("8. POS TAGGING (50 kata):\n")
    for word, tag in pos_tags[:50]:
        f.write(f"   {word} -> {tag}\n")

print(" Hasil disimpan ke file: pertemuan3\hasil_text_processing.txt")