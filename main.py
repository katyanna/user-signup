from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
