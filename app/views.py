from flask import render_template, session, jsonify
from app import app, db
from models import User, Presenter, Message
import datetime


@app.route('/')
@app.route('/index')
@app.route('/index/<int:page>', methods = ['GET', 'POST'])
#@login_required
def index(page=1):
    session['newest_post'] = Message.query.order_by(-Message.id).first().id
    session['oldest_post'] = Message.query.order_by(-Message.id).first().id+1
    return render_template('index.html', title='Home')

@app.route('/admin/adduser', methods=['GET', 'POST'])
def adduser():
    form = newUserForm()
    # if open

@app.route('/get_newer_posts/')
@app.route('/get_newer_posts/<int:count>')
def get_newer_posts():
    messages = Message.query.filter(Message.id > session.get('newest_post')).all()
    if len(messages) > 0:
        session['newest_post'] = messages[-1].id
    return jsonify(messages=[i.serialize for i in messages])

@app.route('/get_older_posts/')
@app.route('/get_older_posts/<int:count>')
def get_older_posts(count=20):
    messages = Message.query.filter(Message.id < session.get('oldest_post')).order_by(Message.id.desc()).limit(count).all()
    if (len(messages) > 0):
        session['oldest_post'] = messages[count-1].id
    return jsonify(messages=[i.serialize for i in messages])
