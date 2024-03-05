from flask import  request, jsonify,Blueprint, session
from models import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash 

auth_BP = Blueprint('auth',__name__)


# signup route
@auth_BP.route('/signup', methods =['POST'])
def signup():
    data = request.get_json()
    name = data.get('name')
    password = data.get('password')
    
    if User.query.filter_by(name = name).first():
        return jsonify({'MSG':'USER ALREADY EXISTS'})

    hash_pass = generate_password_hash(password, method='pbkdf2:sha256')

    new_user = User(name =name , password = hash_pass)
    
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'MSG':'REGISTERED'})


@auth_BP.route('/login', methods =['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        name  = data.get('name')
        password = data.get('password')

        user = User.query.filter_by(name = name).first()

        if user and check_password_hash(user.password, password):
            # session.permanent = True
            session['name']=name
            return jsonify({'MSG':'LOGGED IN '})
        
        else:
            
            return ("invalid credentials")


@auth_BP.route('/logout')
def logout():
    session.pop('name', None)
    return jsonify({'message': 'Logout successful'})