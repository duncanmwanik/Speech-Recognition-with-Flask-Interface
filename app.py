from flask import Flask, render_template, request, redirect
import speech_recognition as sr


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    transcript =''
    if request.method == "POST":
        print("HELLO")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files("file")
        if file.filemame == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile =sr.Recognizer()
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)
            print(transcript)

    return render_template('index.html', transcript)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

