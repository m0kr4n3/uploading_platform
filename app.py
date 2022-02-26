#!/usr/bin/python3

from flask import Flask, request, render_template

app = Flask(__name__)

UPLOAD_FOLDER = "./uploads/"


@app.route("/", methods=["GET", "POST"])
def root():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    f = request.files.getlist("files")
    for file in f:
        if file.read() == b"":
            return render_template("fail.html")

        file_location = UPLOAD_FOLDER + file.filename
        file.save(file_location)

    return render_template("success.html")


if __name__ == "__main__":
    app.run()
