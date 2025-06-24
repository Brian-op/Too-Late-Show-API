from flask import Blueprint, request, jsonify
from server.models.user import User
from server.models import db
from  flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods= ['POST'])
def signup():
    data = request.get_json()
    username =data.get('username')
    email = data.get ('email')
    password = data.get('password')

    if User.query.filter((User.username ==username)| (User.eamil == email)).first():
        return jsonify({'error':'Either the Email or Username you have entered already exists. TRY AGAIN'})
    
    new_user = User(username= username, email = email)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message':'New User created successfully'})

@auth_bp.route('/login', methods=['POST'])
def login():
    data =request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return jsonify({'error':"Invalid credentials, Try again"})
    
    access_token = create_access_token(identify=user.id)
    return jsonify({'access_token': access_token, 'user_id':user.id})

