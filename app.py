from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    h1_text = "Hello profitable python programmers!"
    return "<h1>{}</h1>".format(h1_text)

if __name__ == "__main__":
    app.run(debug=True)
