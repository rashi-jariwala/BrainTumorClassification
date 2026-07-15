import bcrypt

from flask import request
from flask import jsonify

from flask_jwt_extended import create_access_token

from database.mongodb import users_collection


############################
# Register
############################

def register_user():

    data = request.json

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    user = users_collection.find_one(
        {
            "email": email
        }
    )

    if user:

        return jsonify(
            {
                "status": False,
                "message": "Email already exists."
            }
        )

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    users_collection.insert_one(

        {
            "username": username,
            "email": email,
            "password": hashed_password
        }

    )

    return jsonify(

        {
            "status": True,
            "message": "Registration Successful."
        }

    )


############################
# Login
############################

def login_user():

    data = request.json

    email = data.get("email")
    password = data.get("password")

    user = users_collection.find_one(

        {
            "email": email
        }

    )

    if not user:

        return jsonify(

            {
                "status": False,
                "message": "Email not found."
            }

        )

    if not bcrypt.checkpw(
            password.encode("utf-8"),
            user["password"]):

        return jsonify(

            {
                "status": False,
                "message": "Incorrect Password."
            }

        )

    token = create_access_token(
        identity=email
    )

    return jsonify(

        {
            "status": True,
            "message": "Login Successful.",
            "token": token
        }

    )

def forgot_password():

    data = request.json

    email = data.get("email")
    new_password = data.get("new_password")

    user = users_collection.find_one(
        {
            "email": email
        }
    )

    if not user:

        return jsonify(
            {
                "status": False,
                "message": "Email not found."
            }
        )

    hashed_password = bcrypt.hashpw(
        new_password.encode("utf-8"),
        bcrypt.gensalt()
    )

    users_collection.update_one(

        {
            "email": email
        },

        {
            "$set": {
                "password": hashed_password
            }
        }

    )

    return jsonify(
        {
            "status": True,
            "message": "Password Updated Successfully."
        }
    )