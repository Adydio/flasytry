from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
from flask_sqlalchemy import SQLAlchemy
from gevent import pywsgi

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

class NameForm(FlaskForm):
    name = StringField('你叫什么名字?', validators=[DataRequired()])
    submit = SubmitField('提交')

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/', methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('你好像换了个名字!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=session.get('name'))

@app.route('/user/<name>',methods=['GET','POST'])
def user(name):
    return render_template("user.html",name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    server.serve_forever()


