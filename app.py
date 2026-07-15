from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from config import Config
from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
from routes.prediction_routes import prediction_bp

app = Flask(__name__)

app.config["SECRET_KEY"] = Config.SECRET_KEY
app.config["JWT_SECRET_KEY"] = Config.JWT_SECRET_KEY

CORS(app)

jwt = JWTManager(app)

app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(prediction_bp)
if __name__ == "__main__":
    app.run(debug=True)