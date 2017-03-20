from flask import Flask, render_template, request
import jinja2
import re

app = Flask(__name__)

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile("^.{3,20}$")
def valide_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile("^[\S]+@[\S]+.[\S]+$")
def valide_email(email):
    return not email or EMAIL_RE.match(email)

@app.route('/signup', methods=['GET', 'POST'])
def get():
    return render_template("signup.html")

def post():
    have_error = False
    username = request.args.get("username")
    password = request.args.get("password")
    verify   = request.args.get("verify")
    email    = request.args.get("email")

    params = dict(username = username,
                  email = email)

    if not valid_username(username):
        params["error_username"] = "That was an invalid username"
        have_error = True

    if not valid_password(password):
        params["error_password"] = "That was an invalid password"
        have_error = True
    elif password != verify:
        params["error_verify"] = "Passwords don't match"
        have_error = True

    if not valid_email(email):
        params["error_email"] = "That was an invalid email"
        have_error = True

    if have_error:
        return render_template("signup.html", **params)
    else:
        return redirect("/welcome?username=" + username)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
