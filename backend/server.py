from flask import Flask
app = Flask(__name__)
import json
from watson_developer_cloud import ToneAnalyzerV3
from flask import Flask, render_template, request, url_for

THRESHOLD = 0.5
EXTREME_THRESHOLD = 0.9

tone_analyzer = ToneAnalyzerV3(
   username='<your username>',
   password='<your password>',
   version='2016-05-19')

@app.route('/')
def form():
    return render_template('form.html')

@app.route("/ishate", methods=['POST'])
def ishate():
    text = request.form["text"]
    extreme = ""
    tone = tone_analyzer.tone(text=text)
    anger_score = tone["document_tone"]["tone_categories"][0]["tones"][0]["score"]
    if anger_score > THRESHOLD:
        hate_sentences = []
        for sentence in tone["sentences_tone"]:
            categories = sentence["tone_categories"]
            if categories:
                if categories[0]["tones"][0]["score"] > THRESHOLD:
                    hate_sentences.append(sentence["text"])
                

        if anger_score > EXTREME_THRESHOLD:
            extreme = "EXTREME"
        return "WARNING: contains "+extreme+" hate!<br><br>"+"<br><br>".join(hate_sentences)
    else:
        return "no hate detected!"



if __name__ == "__main__":
    app.run(debug=True)