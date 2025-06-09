from flask import Flask
from config import Config
from models import db
from controllers import main
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
