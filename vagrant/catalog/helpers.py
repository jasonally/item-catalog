# Flask basics
from flask import Flask, Blueprint, flash, jsonify, redirect, render_template, request, url_for
from flask import session as login_session

# SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database
from database_setup import Base, User, ReadingList, Book

# Miscellaneous
from functools import wraps
import random, string

# Authentication
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

# Database connection
engine = create_engine('sqlite:///readinglistwithusers.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in login_session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function

def create_user(login_session):
    new_user = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(new_user)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id

def get_user_id(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

def get_user_info(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user