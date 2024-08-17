import os
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import redis

def create_app():
    app = Flask(__name__)
    CORS(app)

    # 秘密鍵の設定
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    jwt = JWTManager(app)
    
    # SQLAlchemyの設定
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    
    from .database import init_db
    init_db(app)
    
    with app.app_context():
        from .route import create_routes
        create_routes(app)
      
    return app

def init_redis():
    return redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)

app = create_app()
r = init_redis()

if __name__ == '__main__':
  app.run(host="0.0.0.0", port="5000")
