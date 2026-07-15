import os
import uuid

from flask import request
from flask import jsonify

from flask_jwt_extended import get_jwt_identity

from tensorflow.keras.models import load_model

import numpy as np

from config import Config

from utils.image_utils import preprocess_image

from database.mongodb import prediction_collection


model = load_model(Config.MODEL_PATH)

CLASS_NAMES = [

    "Glioma",

    "Meningioma",

    "No Tumor",

    "Pituitary"

]


def predict_image():

    if "image" not in request.files:

        return jsonify({

            "status":False,

            "message":"Image Required"

        })


    file = request.files["image"]

    extension = file.filename.split(".")[-1]

    filename = str(uuid.uuid4()) + "." + extension

    filepath = os.path.join(

        Config.UPLOAD_FOLDER,

        filename

    )

    file.save(filepath)

    img = preprocess_image(filepath)

    prediction = model.predict(img)

    index = np.argmax(prediction)

    confidence = float(np.max(prediction) * 100)

    result = CLASS_NAMES[index]

    email = get_jwt_identity()

    prediction_collection.insert_one({

        "email":email,

        "filename":filename,

        "prediction":result,

        "confidence":round(confidence,2)

    })

    return jsonify({

        "status":True,

        "prediction":result,

        "confidence":round(confidence,2)

    })