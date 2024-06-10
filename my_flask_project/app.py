from flask import Flask, render_template, request
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer

app = Flask(__name__)

tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())


@app.route('/', methods=["GET", "POST"])
def main():
    message = ""
    if request.method == "POST":
        inp = request.form.get("inp")
        if inp == "":
            message = ""
        else:
            blob = tb(inp)
            sentiment = blob.sentiment[0]  # Sentiment polarity
            if sentiment < 0:
                message = "Négatif 😠😠"
            else:
                message = "Positif 🙂🙂"
    return render_template('home.html', message=message)


if __name__ == '__main__':
    app.run()
