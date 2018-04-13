from flask import Blueprint, render_template, redirect, flash, url_for, abort
from flask_login import login_user, login_required, logout_user

from app.forms import LoginForm

home=Blueprint('home',__name__,url_prefix='/')

@home.route('/')
def index():
    return render_template("home/index.html")

@home.route('login',methods=['get','post'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        # user=User.query.filter_by(email=form.email.data).first()
        # login_user(user,True)
        flash('登录成功','success')
        return redirect(url_for('.index'))
    else:
        flash('登录失败，请重试','danger')
    return render_template("home/login.html",form=form)
@home.route('register/<string:type>',methods=['post','get'])
def register(type):
    if type=='user':
        #用户注册
        pass
    elif type=='company':
        #企业注册
        pass
    else:
        abort(404)

@home.route('logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.index'))