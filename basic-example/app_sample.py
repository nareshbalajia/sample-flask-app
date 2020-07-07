from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hey, Welcome!"


app.run(port=5000)
