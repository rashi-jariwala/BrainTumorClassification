from flask import jsonify
from flask_jwt_extended import get_jwt_identity

from database.mongodb import prediction_collection


def get_dashboard():

    email = get_jwt_identity()

    total_prediction = prediction_collection.count_documents(
        {
            "email": email
        }
    )

    return jsonify(
        {
            "status": True,
            "total_prediction": total_prediction
        }
    )