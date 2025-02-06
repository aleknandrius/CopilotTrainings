from flask import Flask
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI'])

from routes import user_routes

app.register_blueprint(user_routes, url_prefix='/api/users')

print("Blueprint registered")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Database tables created")
    app.run(debug=True)  # Set debug to False to disable the interactive debugger
    print("Flask app running")
