from functools import wraps
import string

from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from flask import make_response
from flask import session
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker

from forumdb import Base, Forum

import flask
from flask.templating import render_template
from datetime import datetime

app = flask.Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///forum.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
POSTS_PER_PAGE= 5

# Request handler for main page
@app.route('/', methods=['GET', 'POST'])
def getAllPosts():
    '''View is the 'main page' of the forum.
    It displays the submission form and the previously posted messages.
    '''
    if request.method == 'POST':
        if request.form['content']:
            newPost = Forum(content=request.form['content'], time=datetime.utcnow())
            session.add(newPost)
            session.commit()
            return redirect(url_for('getAllPosts'))
    posts = session.query(Forum).order_by(desc(Forum.time))
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
