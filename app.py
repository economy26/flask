from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import User, Order, Product, Order_Product,db
from flask_marshmallow import Marshmallow


ma = Marshmallow()

def create_app():
    
    app = Flask(__name__)

    # Configure the MySQL database connection
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:6521@localhost/ecommerce_api'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # connects or initialize SQLAlchemy with the app
    db.init_app(app)
    # connects or initiallise Marshmellow
    ma.init_app(app)

    # Import models (after app context is set up)
    with app.app_context(): 
        db.create_all()
    from routes import api
    app.register_blueprint(api, url_prefix="/api")
    
    return app



if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
