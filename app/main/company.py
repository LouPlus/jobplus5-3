from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from app import User
from app.forms import publish_job
from app.models import Job

company = Blueprint('company', __name__, url_prefix='/company')


@company.route('/')
def index():
    company_list=User.query.filter_by(user_role=User.ROLE_COMPANY).all()
    return render_template("company/index.html",company_list=company_list)

@company.route('/<int:company_id>')
def detail(company_id):
    company=User.query.filter_by(id=company_id).first()
    return render_template('company/detail.html',company=company)

@company.route('/admin')
@login_required
def admin():
    user = current_user
    jobs=Job.query.filter_by(job_company=user.company.id).all()
    return render_template('company/admin.html',jobs=jobs)

@company.route('/publish',methods=['get','post'])
@login_required
def publish():
    form=publish_job()
    if form.validate_on_submit():
        form.publish(current_user.company)
        return redirect(url_for('.index'))
    return render_template('company/publish.html',form=form)

@company.route('apply')
@login_required
def apply():
    return render_template('company/apply.html')