from flask import Flask
from flask_cors import CORS
from translate.word_translation import word_translate
from translate.sentence_analysis import sentence_translate

app = Flask(__name__)
CORS(app)

@app.route('/wtran')
def w_translate():
    return {'key1' : [1, 2, 3]}
    return word_translate()

@app.route('/stran')
def s_translate():
    return {'key2' : [1, 2, 3]}
    return sentence_translate()

if __name__ == "__main__":
    app.run(debug=True)