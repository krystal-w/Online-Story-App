import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt

# Initialize app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'story.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# User class, linked to stories user has created
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.Integer, unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    # admin = db.Column(db.Boolean)
    stories = db.relationship('Story', backref='author')

    def __init__(self, username, password):
        self.username = username
        self.password = password

# Story class, linked to author and the chapters of the story
class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(80))
    genre = db.Column(db.String)
    summary = db.Column(db.String)
    chapters = db.relationship('Chapter', backref='story')
    num_chapters = db.Column(db.Integer)
    completed = db.Column(db.Boolean)

    def __init__(self, author_id, title, genre):
        self.author_id = author_id
        self.title = title
        self.genre = genre
        self.completed = False
        self.num_chapters = 0

# Chapter class, linked to story it is from
class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'))
    title = db.Column(db.String(80))
    number = db.Column(db.Integer)
    text = db.Column(db.String)

    def __init__(self, story_id, title, number, text):
        self.story_id = story_id
        self.title = title
        self.number = number
        self.text = text

# Create a user
@app.route('/user', methods=['POST'])
def create_user():
    return ''

# Update user
@app.route('/user/<public_id>', methods=['PUT'])
def update_user(public_id):
    return ''

# Delete a user
@app.route('/user/<public_id>', methods=['DELETE'])
def delete_user(public_id):
    return ''

# Get a user
@app.route('/user/<public_id>', methods=['GET'])
def get_user(public_id):
    return ''

# Create a story
@app.route('/story', methods=['POST'])
def create_story():
    return ''

# Update story
@app.route('/story/<id>', methods=['PUT'])
def update_story(id):
    return ''

# Delete a story
@app.route('/story/<id>', methods=['DELETE'])
def delete_story(id):
    return ''

# Get list of stories created by user
@app.route('/user/<author_id>/story', methods=['GET'])
def get_user_stories(author_id):
    return ''

# Get list of stories by genre
@app.route('/story', methods=['GET'])
def get_story_by_genre():
    genre = request.args.get('genre')
    return ''

# Create a chapter
@app.route('/story/<story_id>/chapter', methods=['POST'])
def create_chapter(story_id):
    return ''

# Get a chapter of a story
@app.route('/story/<story_id>/chapter/<id>', methods=['GET'])
def get_story_chapter(story_id, id):
    return ''

# Get all chapters of story
@app.route('/story/<id>', methods=['GET'])
def get_all_chapters(id):
    show_all = request.args.get('show_all')
    return  ''

if __name__ == '__main__':
    app.run(debug=True)
