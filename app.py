from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "<h1>Hello world from Utibeabasi Umanah</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")