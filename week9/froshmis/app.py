from flask import Flask, render_template, request, redirect


app = Flask(__name__)


REGISTRANTS = {}

SPORTS = ["Basketball","Soccer", "Ultimate fris bee"]


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])

def register():

    # Validate name

    name = request.form.get("name")

    if not name:
        return render_template("error.html", message="Missing name")

    #validate sport

    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")

    # Remember registrant

    REGISTRANTS[name] = sport

    # Confirm registration

    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    return render_template("registrants.html",registrants=REGISTRANTS)






    #validate submission or # checking acutal submitting input or unintended forms

    if not request.form.get("name") or request.form.get("sport") not in SPORTS:
        return render_template("failure.html")

    # confirm registration

    return render_template("success.html")