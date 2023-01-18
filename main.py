from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World! New Release 2.0!"
# run the app.
if __name__ == "__main__":
    app.run()
