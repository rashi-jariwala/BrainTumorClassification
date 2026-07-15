from flask import Blueprint
from flask_jwt_extended import jwt_required

from services.prediction_service import predict_image

prediction_bp = Blueprint("prediction", __name__)

@prediction_bp.route("/api/predict", methods=["POST"])
@jwt_required()
def predict():

    return predict_image()