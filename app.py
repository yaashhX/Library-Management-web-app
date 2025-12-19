from flask import Flask
import sqlite3



def get_db_connection():
    cnx = sqlite3.connect("library.db")
    cnx.row_factory = sqlite3.Row
    return cnx

cnx = get_db_connection()
cnx.execute("""
CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            quantity INTEGER NOT NULL
)
""")
cnx.commit()
cnx.close()



app = Flask(__name__)

@app.route("/")
def home():
    return "Library app running"

@app.route("/books")
def books():
    cnx = get_db_connection()
    books = cnx.execute("SELECT * FROM books").fetchall()
    cnx.close()
    return {"books": [dict[book] for book in books]}

if __name__ == "__main__":
    app.run(debug=True, port=16080)



