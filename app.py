from flask import Flask, render_template

app = Flask(__name__)
# create an app instance

# Home Page


@app.route('/')
def home():
    """ Main Page"""
    return render_template("index.html")


if __name__ == "__main__":
    # on running python app.py
    app.run(debug=True)
