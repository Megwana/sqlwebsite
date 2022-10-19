from flask import render_template
from openroad import app, db
from openroad.models import Category, Triproute


@app.route("/")
def home():
    return render_template("layout.html")