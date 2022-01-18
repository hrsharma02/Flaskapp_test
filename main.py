from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return "<h1> Hi this is first app </h>"


if __name__ == "__main__":
    app.run()
