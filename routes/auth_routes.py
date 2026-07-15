from flask import Blueprint, render_template
from services.auth_service import register_user, login_user, forgot_password

auth_bp = Blueprint("auth", __name__)

# -------------------- Pages --------------------

@auth_bp.route("/")
def home():
    return render_template("login.html")


@auth_bp.route("/login")
def login():
    return render_template("login.html")


@auth_bp.route("/register")
def register():
    return render_template("register.html")


@auth_bp.route("/forgot-password")
def forgot_password_page():
    return render_template("forgot_password.html")


@auth_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# -------------------- APIs --------------------

@auth_bp.route("/api/register", methods=["POST"])
def register_api():
    return register_user()


@auth_bp.route("/api/login", methods=["POST"])
def login_api():
    return login_user()


@auth_bp.route("/api/forgot-password", methods=["PUT"])
def forgot_password_api():
    return forgot_password()

@auth_bp.route("/prediction")
def prediction():

    return render_template("prediction.html")