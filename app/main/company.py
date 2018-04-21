from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from app import User
from app.forms import publish_job
from app.models import Job, db, Delivery, Company

company = Blueprint('company', __name__, url_prefix='/company')


@company.route('/')
def index():
    company_list = User.query.filter_by(user_role=User.ROLE_COMPANY).all()
    return render_template("company/index.html", company_list=company_list)


@company.route('/<int:company_id>')
def detail(company_id):
    company = User.query.filter_by(id=company_id).first()
    return render_template('company/detail.html', company=company)


@company.route('/admin')
@login_required
def admin():
    user = current_user
    jobs = Job.query.filter_by(job_company=user.company.id).all()
    return render_template('company/admin.html', jobs=jobs)


@company.route('/publish', methods=['get', 'post'])
@login_required
def publish():
    form = publish_job()
    if form.validate_on_submit():
        form.publish(current_user.company)
        return redirect(url_for('.index'))
    return render_template('company/publish.html', form=form,type='create')


@company.route('/apply')
@login_required
def apply():
    deliveries=Delivery.query.filter_by(delivery_company=current_user.company.id).all()
    return render_template('company/apply.html',deliveries=deliveries)

@company.route('/apply/<int:delivery_id>/accept')
@login_required
def accept(delivery_id):
    delivery=Delivery.query.get_or_404(delivery_id)
    delivery.delivery_status=Delivery.STATUS_ACCEPT
    db.session.add(delivery)
    db.session.commit()
    return redirect(url_for('.apply'))

@company.route('/apply/<int:delivery_id>/reject')
@login_required
def reject(delivery_id):
    delivery=Delivery.query.get_or_404(delivery_id)
    delivery.delivery_status=Delivery.STATUS_REJECT
    db.session.add(delivery)
    db.session.commit()
    return redirect(url_for('.apply'))

@company.route('/del/<int:job_id>')
@login_required
def del_job(job_id):
    job = Job.query.filter_by(id=job_id).first_or_404()
    db.session.delete(job)
    db.session.commit()
    return redirect(url_for('.admin'))


@company.route('/edit/<int:job_id>',methods=['get','post'])
@login_required
def edit_job(job_id):
    job = Job.query.filter_by(id=job_id).first_or_404()
    form = publish_job(obj=job)
    tags=[]
    for tag in job.job_tag:
        tags.append(tag.tag_name)
    form.tags.data=",".join(tags)
    if form.validate_on_submit():
        form.update(job)
        return redirect(url_for('.admin'))
    return render_template('company/publish.html', form=form,type='edit',job_id=job_id)

@company.route('/<int:company_id>/jobs')
def open_jobs(company_id):
    company=Company.query.get_or_404(company_id)
    return render_template('company/jobs.html',company=company)
