from flask import Blueprint, render_template
from openroad import app, db
from openroad.models import User, Triproute
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

@app.route("/")
def home():
    return render_template("layout.html")
