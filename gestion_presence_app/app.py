from flask import Flask
from config import Config
from models import db
from routes.auth_routes import auth_bp
from routes.prof_routes import prof_bp
from routes.etudiant_routes import etudiant_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(prof_bp)
app.register_blueprint(etudiant_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)