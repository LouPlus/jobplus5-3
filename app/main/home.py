from flask import Blueprint, render_template, redirect, flash, url_for, abort
from flask_login import login_user, login_required, logout_user, current_user

from app.forms import LoginForm, RegisterForm, JobseekerProfile, CompanyProfile
from app.models import User, Jobseeker

home = Blueprint('home', __name__, url_prefix='/')


@home.route('/')
def index():
    return render_template("home/index.html")


@home.route('login', methods=['get', 'post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(userEmail=form.userEmail.data).first()
        if user!=None:
            login_user(user, True)
            flash('登录成功', 'success')
            if user.userRole==User.ROLE_JOBSEEKER:
                return redirect(url_for('.profile',type='jobseeker'))
            elif user.userRole==User.ROLE_COMPANY:
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
        form.userName.label.text = '用户名'
    elif type == 'company':
        # 企业注册
        form_title = '企业注册'
        form.userName.label.text = '企业名称'
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
        form.jobseekerExperience.data=user.jobseekerExperience
    elif type=='company':
        form=CompanyProfile()
        if form.validate_on_submit():
            form.update_profile(user.id)
            return redirect(url_for('.profile',type=type))
        form.companyHomepage.data=user.companyHomepage
        form.companyCity.data=user.companyCity
        form.companySlug.data=user.companySlug
        form.companyDescription.data=user.companyDescription
        form.companyIntroduction.data=user.companyIntroduction
    else:
        abort(404)
    form.userName.data= user.userName
    form.userEmail.data = user.userEmail
    form.userPhone.data=user.userPhone
    return render_template('home/profile.html',form=form,type=type)

@home.route('job')
def job_list():
    pass


@home.route('company')
def company_list():
    pass
