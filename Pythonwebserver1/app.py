from flask import request, Flask

app = Flask(__name__)


@app.route("/")
def hello():
    name = request.args.get("name", "World")
    return f"Hello, {name}!"

@app.route("/info")
def hello():
    return """
<h1>Info Page</h1>
<p>I am Groot</p>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)