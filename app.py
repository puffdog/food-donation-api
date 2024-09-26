from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from mongoengine import connect
from models.user import User
from models.donation import Donation

app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret'  # Change this
jwt = JWTManager(app)
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'  # This is where the Swagger JSON file will be located

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Food Donation API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
# Connect to MongoDB (Use MongoDB Atlas URL if needed)
connect('food_donation_db')

# Root Route
@app.route('/')
def index():
    return jsonify(message="Welcome to the Food Donation API")

# User Registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    user = User(username=data['username'])
    user.set_password(data['password'])
    user.save()
    return jsonify(message='User created'), 201

# User Login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.objects(username=data['username']).first()

    if user and user.check_password(data['password']):
        token = create_access_token(identity=str(user.id))
        return jsonify(access_token=token)

    return jsonify(message='Invalid credentials'), 401

# Create Donation
@app.route('/donations', methods=['POST'])
@jwt_required()
def create_donation():
    data = request.json
    donation = Donation(**data)
    donation.save()
    return jsonify(donation), 201

# Get All Donations
@app.route('/donations', methods=['GET'])
def get_donations():
    location = request.args.get('location')
    if location:
        donations = Donation.objects(location=location)
    else:
        donations = Donation.objects()
    return jsonify(donations), 200

# Delete Donation
@app.route('/donations/<id>', methods=['DELETE'])
@jwt_required()
def delete_donation(id):
    donation = Donation.objects(id=id).first()
    if donation:
        donation.delete()
        return jsonify(message='Donation deleted'), 200
    return jsonify(message='Donation not found'), 404

if __name__ == '__main__':
    app.run(debug=True)
