from flask import Blueprint, request, jsonify
from dto import UserDTO
from repository import UserRepository
from models import User  # Import the User model

user_routes = Blueprint('user_routes', __name__)
user_repository = UserRepository()

@user_routes.route("/", methods=["POST"])
@user_routes.route("", methods=["POST"])
def create_user():
    data = request.get_json()
    user_dto = UserDTO(username=data["username"], email=data["email"])
    user = user_repository.add_user(user_dto)
    return jsonify({"message": "User created", "user": {"username": user.username, "email": user.email}}), 201

@user_routes.route("/", methods=["GET"])
@user_routes.route("", methods=["GET"])
def get_users():
    page = request.args.get('page', 1, type=int)
    size = request.args.get('size', 10, type=int)
    users_query = User.query.paginate(page=page + 1, per_page=size, error_out=False)
    users_list = [{"username": user.username, "email": user.email} for user in users_query.items]
    return jsonify({
        "users": users_list,
        "total": users_query.total,
        "pages": users_query.pages,
        "current_page": users_query.page,
        "next_page": users_query.next_num,
        "prev_page": users_query.prev_num
    }), 200
