```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)

# User Class/Model
class User(db.Model):
    userID = db.Column(db.String(100), primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))
    preferences = db.Column(db.String(200))

    def __init__(self, userID, username, email, password, preferences):
        self.userID = userID
        self.username = username
        self.email = email
        self.password = password
        self.preferences = preferences

# User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('userID', 'username', 'email', 'password', 'preferences')

# Init schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
```