from flask import Flask
from config import Config
from models import db
from controllers import main
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()
    print("Database created at:", app.config['SQLALCHEMY_DATABASE_URI'])


app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
