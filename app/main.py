from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash

from .extensions import db
from .models import User

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return 'ok'

@main.route('/health', methods=['GET'])
def health():
    return jsonify(status='ok'), 200


@main.route('/users/register', methods=['POST'])
def register():
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "Request body must be JSON.",
            }
        }), 400

    username = data.get("username")

    if not username:
        return jsonify({
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "Username is required.",
            }
        }), 400

    if len(username) < 3 or len(username) > 17:
        return jsonify({
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "Username must be between 3 and 17 characters.",
            }
        }), 400

    password = data.get("password")

    if not password:
        return jsonify({
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "Password is required.",
            }
        }), 400

    if len(password) < 7 or len(password) > 128:
        return jsonify({
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "Password must be between 7 and 128 characters.",
            }
        }), 400

    display_name = data.get("display_name")
    if display_name is not None and display_name != "":
        if len(display_name) > 17:
            return jsonify({
                "error": {
                    "code": "VALIDATION_ERROR",
                    "message": "Display name must be at most 17 characters.",
                }
            }), 400

    if User.query.filter_by(username=username).first() is not None:
        return jsonify({
            "error": {
                "code": "USERNAME_TAKEN",
                "message": "That username is already in use.",
            }
        }), 409

    user = User(
        username=username,
        password_hash=generate_password_hash(password),
    )
    db.session.add(user)
    db.session.commit()

    return jsonify({
        "id": user.id,
        "username": user.username,
    }), 201
