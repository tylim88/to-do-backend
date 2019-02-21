# save it for later

from src import app
from os import environ
from flask import render_template
from flask_dance.contrib.google import make_google_blueprint, google

# set environment variable for google
environ["OAUTHLIB_INSECURE_TRANSPORT"] = app.config["OAUTHLIB_INSECURE_TRANSPORT"]
environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = '1'

# setup google blueprint
blueprint = make_google_blueprint(
    client_id=app.config['GOOGLE_CLIENT_ID'],
    client_secret=app.config['GOOGLE_SECRET'],
    # reprompt_consent=True,
    offline=True,
    scope=["profile", "email"]
)

# register google blueprint
app.register_blueprint(blueprint, url_prefix="/loginGoogle")
app.register_blueprint(blueprint, url_prefix="/signUpGoogle")

@app.route("/login/google")
def loginGoogle():
    if not google.authorized:
        return render_template(url_for("google.login"))

    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email=resp.json()["email"]

    return render_template("welcome.html",email=email)

@app.route("/signUp/google")
def signUpGoogle():
    if not google.authorized:
        return render_template(url_for("google.login"))

    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email=resp.json()["email"]

    return render_template("welcome.html",email=email)

@app.route("/logout/google")
def logout():
    token = blueprint.token["access_token"]
    resp = google.post(
        "https://accounts.google.com/o/oauth2/revoke",
        params={"token": token},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert resp.ok, resp.text
    return render_template("welcome.html")