from flask import Flask, request
from flask_cors import CORS
from word_translation import word_translate
from sentence_analysis import sentence_translate

app = Flask(__name__)
CORS(app)

@app.route('/wtran')
def w_translate():
    return {'key1' : [1, 2, 3]}
    #return word_translate()

@app.route('/stran', method=["POST"])
def s_translate():
    return sentence_translate(request.form["sentence"])

if __name__ == "__main__":
    app.run(debug=True)