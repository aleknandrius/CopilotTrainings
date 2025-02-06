from flask import Blueprint, request, jsonify
from dto import UserDTO
from repository import UserRepository
from models import User  # Import the User model

user_routes = Blueprint('user_routes', __name__)
user_repository = UserRepository()

@user_routes.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    user_dto = UserDTO(username=data["username"], email=data["email"])
    user = user_repository.add_user(user_dto)
    return jsonify({"message": "User created", "user": {"username": user.username, "email": user.email}}), 201

@user_routes.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    users_list = [{"username": user.username, "email": user.email} for user in users]
    return jsonify(users_list), 200
