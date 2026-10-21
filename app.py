from flask import Flask, render_template
from disease_database import DISEASES

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", diseases=DISEASES)

if __name__ == "__main__":
    app.run(debug=True)