from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/users", methods=["POST"])
def create_user():
    # We'll ask Copilot to fill this in
    return jsonify({"message": "User created"}), 201

if __name__ == "__main__":
    app.run(debug=True)
