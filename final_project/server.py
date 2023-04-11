from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/englishToFrench",methods=["GET"])
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translatedText = translator.english_to_french(textToTranslate)
    print(translatedText)
    return translatedText["translations"][0]["translation"]


@app.route("/frenchToEnglish",methods=["GET"])
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translatedText = translator.french_to_english(textToTranslate)
    print(translatedText)
    return translatedText["translations"][0]["translation"]

@app.route("/")
def renderIndexPage():
    return render_template('index.html')
   

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
