from flask import Blueprint

from flask_jwt_extended import jwt_required

from services.dashboard_service import get_dashboard

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/api/dashboard", methods=["GET"])
@jwt_required()
def dashboard():

    return get_dashboard()