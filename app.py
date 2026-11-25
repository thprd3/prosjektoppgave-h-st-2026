from flask import Flask, render_template
import mariadb

app = Flask(__name__)

@app.route("/")
def index():
    conn = mariadb.connect(
        username="november26",
        password="IMKuben1337!",
        host="localhost",
        database="skole",
    )
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM players")
    results = cursor.fetchall()
    print(results)
    
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run()