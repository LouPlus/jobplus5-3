from flask import Blueprint, render_template, redirect, flash, url_for, abort
from flask_login import login_user, login_required, logout_user, current_user

from app.forms import LoginForm, RegisterForm, JobseekerProfile, CompanyProfile
from app.models import User, Company, Job

home = Blueprint('home', __name__, url_prefix='/')


@home.route('/')
def index():
    company_list=Company.query.order_by(Company.create_time.desc()).limit(12).all()
    job_list=Job.query.filter_by(is_open=True).order_by(Job.create_time.desc()).limit(9).all()
    return render_template("home/index.html",company_list=company_list,job_list=job_list)


@home.route('login', methods=['get', 'post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.user_email.data).first()
        if user!=None:
            login_user(user, True)
            flash('登录成功', 'success')
            if user.is_jobseeker:
                return redirect(url_for('.profile',type='jobseeker'))
            elif user.is_company:
                return redirect(url_for('.profile',type='company'))
            else:
                abort(404)
        else:
            flash('登录失败,请检查后重试', 'error')
            return render_template("home/login.html", form=form)
    return render_template("home/login.html", form=form)


@home.route('register/<string:type>', methods=['post', 'get'])
def register(type):
    form = RegisterForm()
    if form.validate_on_submit():
        user = form.create_user(type)
        if user != None:
            flash('注册成功', 'success')
            return redirect(url_for('.index'))
        else:
            flash('注册失败,请检查后重试', 'error')
            return redirect(url_for('.register'))
    if type == 'jobseeker':
        # 用户注册
        form_title = '用户注册'
        form.user_name.label.text = '用户名'
    elif type == 'company':
        # 企业注册
        form_title = '企业注册'
        form.user_name.label.text = '企业名称'
    return render_template('home/register.html', form=form, type=type, form_title=form_title)


@home.route('logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.index'))



@home.route('<string:type>/profile',methods=['get','post'])
@login_required
def profile(type):
    user = current_user
    if type=='jobseeker':
        form = JobseekerProfile()
        if form.validate_on_submit():
            form.update_profile(user.id)
            return redirect(url_for('.profile',type=type))
        form.user_experience.data=user.user_experience
    elif type=='company':
        form=CompanyProfile()
        if form.validate_on_submit():
            form.update_profile(user.id)
            return redirect(url_for('.profile',type=type))
        form.company_homepage.data = user.company.company_homepage
        form.company_city.data = user.company.company_city
        form.company_slug.data = user.company.company_slug
        form.company_description.data = user.company.company_description
        form.company_introduction.data = user.company.company_introduction
        form.company_logo.data=user.company.company_logo
    else:
        abort(404)
    form.user_name.data= user.user_name
    form.user_email.data = user.user_email
    form.user_phone.data=user.user_phone
    return render_template('home/profile.html',form=form,type=type)

