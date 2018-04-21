from flask import Blueprint, render_template, request, current_app, redirect, url_for
from flask_login import login_required, current_user

from app.models import Job, Delivery, Company, db

job = Blueprint('job', __name__, url_prefix='/job')


@job.route('/')
def index():
    page=request.args.get('page',default=1,type=int)
    pagination=Job.query.filter_by(is_open=True).order_by(Job.create_time.desc()).paginate(page=page,per_page=current_app.config['PER_PAGE'],error_out=False)
    return render_template("job/index.html",pagination=pagination)

@job.route('/<int:job_id>')
def detail(job_id):
    job=Job.query.get_or_404(job_id)
    return render_template('job/detail.html',job=job)

@job.route('/apply/<int:job_id>')
@login_required
def apply(job_id):
    job=Job.query.filter_by(id=job_id).first_or_404()
    delivery=Delivery()
    delivery.delivery_company=job.job_company
    delivery.delivery_job=job.id
    delivery.delivery_user=current_user.id
    db.session.add(delivery)
    db.session.commit()
    return redirect(url_for('.detail',job_id=job_id))