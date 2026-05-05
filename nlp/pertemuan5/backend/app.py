from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(
    __name__,
    template_folder="../frontend",
    static_folder="../frontend/static")

# 10 dokumen contoh
documents = {
    "Doc1": "Pemerintah Indonesia secara resmi meluncurkan program Makan Bergizi Gratis atau MBG pada awal tahun 2026 sebagai langkah strategis untuk meningkatkan kualitas gizi masyarakat serta menurunkan angka stunting di berbagai daerah yang masih tinggi.",
    "Doc2": "Pelaksanaan program MBG dilakukan oleh Badan Gizi Nasional dengan melibatkan berbagai pihak termasuk sekolah, tenaga kesehatan, dan pemerintah daerah guna memastikan distribusi makanan bergizi berjalan secara merata dan tepat sasaran.",
    "Doc3": "Selama periode libur Lebaran tahun 2026, program MBG dihentikan sementara untuk menyesuaikan kondisi operasional di lapangan, namun pemerintah memastikan program akan kembali berjalan normal setelah aktivitas sekolah dimulai kembali.",
    "Doc4": "Kebijakan pemerintah menetapkan bahwa program MBG difokuskan pada hari sekolah agar distribusi makanan lebih efektif, terukur, dan dapat langsung dirasakan manfaatnya oleh siswa sebagai salah satu kelompok prioritas utama.",
    "Doc5": "Program MBG menargetkan kelompok rentan seperti siswa sekolah dasar, ibu hamil, ibu menyusui, serta balita dengan tujuan meningkatkan asupan gizi harian dan mendukung pertumbuhan serta perkembangan yang optimal.",
    "Doc6": "Sejumlah daerah menghadapi tantangan dalam implementasi program MBG terutama terkait distribusi logistik, keterbatasan infrastruktur dapur, serta koordinasi antar lembaga yang masih perlu ditingkatkan agar program berjalan lebih efektif.",
    "Doc7": "Kasus keracunan makanan yang terjadi dalam pelaksanaan program MBG menjadi perhatian serius pemerintah sehingga dilakukan evaluasi menyeluruh terhadap standar kebersihan, proses pengolahan makanan, dan pengawasan distribusi di lapangan.",
    "Doc8": "Pemerintah kemudian memperketat standar operasional program MBG dengan menambahkan prosedur keamanan pangan, pelatihan bagi petugas dapur, serta sistem monitoring yang lebih ketat untuk memastikan kualitas makanan tetap terjaga.",
    "Doc9": "Program MBG dinilai sebagai salah satu kebijakan penting dalam meningkatkan kualitas sumber daya manusia Indonesia karena berfokus pada pemenuhan gizi sejak usia dini yang berdampak pada kesehatan dan produktivitas jangka panjang.",
    "Doc10": "Masyarakat memberikan berbagai tanggapan terhadap program MBG, mulai dari dukungan karena manfaatnya yang besar hingga kritik terkait pelaksanaan di lapangan, transparansi anggaran, serta konsistensi kualitas makanan yang diberikan."
}

doc_names = list(documents.keys())
doc_texts = list(documents.values())

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(doc_texts)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    query = ""
    method = "cosine"
    analysis = ""
    
    if request.method == "POST":
        query = request.form["query"]
        method = request.form["method"]

        query_vec = vectorizer.transform([query])

        if method == "cosine":
            scores = cosine_similarity(query_vec, tfidf_matrix)[0]
        else:
            # TF-IDF (dot product sederhana)
            scores = (query_vec * tfidf_matrix.T).toarray()[0]

        # Gabungkan hasil
        for i in range(len(scores)):
            results.append({
                "doc": doc_names[i],
                "score": round(scores[i], 4),
                "text": doc_texts[i]
            })

        # Urutkan berdasarkan skor tertinggi
        results = sorted(results, key=lambda x: x["score"], reverse=True)
    
        

    if results:
        top_doc = results[0]
        avg_score = sum(r["score"] for r in results) / len(results)

        if top_doc["score"] > 0.7:
            relevance = "sangat relevan"
        elif top_doc["score"] > 0.4:
            relevance = "cukup relevan"
        else:
            relevance = "kurang relevan"

        analysis = f"""
        Dokumen paling relevan adalah {top_doc['doc']} dengan skor {top_doc['score']}.
        Secara keseluruhan, tingkat kemiripan query terhadap dokumen termasuk {relevance}.
        Rata-rata skor kemiripan adalah {round(avg_score, 4)}.
        """

    return render_template("index.html", results=results, query=query, method=method, analysis=analysis)

if __name__ == "__main__":
    app.run(debug=True)