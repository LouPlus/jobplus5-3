from flask import Blueprint, render_template, redirect, flash, url_for, abort
from flask_login import login_user, login_required, logout_user

from app.forms import LoginForm, RegisterForm

home=Blueprint('home',__name__,url_prefix='/')

@home.route('/')
def index():
    return render_template("home/index.html")

@home.route('login',methods=['get','post'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        #做角色判断，登录的 用户是 企业用户还是个人用户
        # user=User.query.filter_by(email=form.email.data).first()
        # login_user(user,True)
        flash('登录成功','success')
        return redirect(url_for('.index'))
    return render_template("home/login.html",form=form)

@home.route('register/<string:type>',methods=['post','get'])
def register(type):
    form=RegisterForm()
    if form.validate_on_submit():
        flash('注册成功','success')
        return redirect(url_for('.index'))
    if type=='user':
        #用户注册
        form_title='用户注册'
        form.username.label.text='用户名'
    elif type=='company':
        #企业注册
        form_title='企业注册'
        form.username.label.text='企业名称'
    return render_template('home/register.html',form=form,type=type,form_title=form_title)

@home.route('logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.index'))

@home.route('job')
def job_list():
    pass

@home.route('company')
def company_list():
    pass

