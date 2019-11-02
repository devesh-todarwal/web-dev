from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils.types.password import PasswordType

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    uname = db.Column(db.String, nullable=False)
    password = db.Column(PasswordType(
            schemes=[
                'pbkdf2_sha512',
                'md5_crypt'
            ],
            deprecated=['md5_crypt']
        ),
        nullable=False)

    def verify_pass(self,password):
        return self.password == password

    def __str__(self):
        return f'{self.id} - {self.fname} {self.lname}: {self.uname}'

class Review(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String, db.ForeignKey("users.id"), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
