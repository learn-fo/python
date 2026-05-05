from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

# =========================
# CONFIG MYSQL
# =========================
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",   # sesuaikan
    "database": "flask_crud",
    "cursorclass": pymysql.cursors.DictCursor
}

def get_connection():
    return pymysql.connect(**db_config)

# =========================
# READ
# =========================
@app.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()

    db_info = {
        "host": db_config["host"],
        "database": db_config["database"]
    }
    return render_template("index.html", users=users, db_info=db_info)

# =========================
# CREATE
# =========================
@app.route("/tambah", methods=["GET", "POST"])
def tambah():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("tambah.html")

# =========================
# UPDATE
# =========================
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (name, email, id))
        conn.commit()
        conn.close()

    return redirect("/")

    cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
    user = cursor.fetchone()
    conn.close()

    return render_template("edit.html", user=user)

# =========================
# DELETE
# =========================
@app.route("/hapus/<int:id>")
def hapus(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    conn.commit()
    conn.close()

    return redirect("/")

# =========================
# RUN
# =========================
if __name__ == "__main__":
    app.run(debug=True)