from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    create_time = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)


class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, unique=True)
    company_homepage = db.Column(db.String(20),nullable=True)
    company_field = db.Column(db.String(20), nullable=True)
    company_financing = db.Column(db.String(20), nullable=True)
    company_city = db.Column(db.String(20), nullable=True)
    company_logo = db.Column(db.String(255), nullable=True)
    company_introduction = db.Column(db.String(1024), nullable=True)
    company_description = db.Column(db.String(4096), nullable=True)
    company_slug=db.Column(db.String(20),nullable=True)
    job=db.relationship('Job',backref='Company')
    user_id=db.Column(db.Integer,db.ForeignKey('user.id',ondelete='SET NULL'))
    user=db.relationship('User',uselist=False,backref=db.backref('Company',uselist=False))


class User(Base, UserMixin):
    __tablename__ = 'user'
    ROLE_JOBSEEKER = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30
    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, unique=True)
    user_name = db.Column(db.String(255), nullable=False)
    user_email = db.Column(db.String(255), nullable=False, unique=True)
    _user_password = db.Column('userPassword', db.String(256), nullable=False)
    user_role = db.Column(db.Integer, nullable=False, default=ROLE_JOBSEEKER)
    user_phone = db.Column(db.String(15), nullable=True)

    user_experience = db.Column(db.Integer, nullable=True)
    user_resume = db.Column(db.String(1024), nullable=True)
    company=db.relationship('Company',uselist=False)

    @property
    def user_password(self):
        return self._user_password

    @user_password.setter
    def user_password(self, orig_password):
        self._user_password = generate_password_hash(orig_password)

    def check_password(self, password):
        return check_password_hash(self._user_password, password)
    @property
    def is_admin(self):
        return self.user_role==self.ROLE_ADMIN

    @property
    def is_jobseeker(self):
        return self.user_role==self.ROLE_JOBSEEKER

    @property
    def is_company(self):
        return self.user_role==self.ROLE_COMPANY


class Job(Base):
    __tablename__ = 'job'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    job_name = db.Column(db.String(255), nullable=False)
    job_tag = db.Column(db.String(255), nullable=False)
    job_description = db.Column(db.String(4096), nullable=False)
    job_address = db.Column(db.String(1024), nullable=False)
    job_salary_l = db.Column(db.Integer, nullable=False)
    job_salary_h = db.Column(db.Integer, nullable=False)
    job_experience = db.Column(db.String(255), nullable=False)
    job_education = db.Column(db.String(255), nullable=False)
    job_company = db.Column(db.Integer, db.ForeignKey('company.id') ,nullable=False)



class Delivery(Base):
    __tablename__ = 'delivery'

    STATUS_WAITING = 1
    STATUS_REJECT = 2
    STATUS_ACCEPT = 3

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    deliveryJob = db.Column(db.Integer, nullable=False)
    deliveryCompany = db.Column(db.Integer, nullable=False)
    deliveryJobseeker = db.Column(db.Integer, nullable=False)
    deliveryStatus = db.Column(db.Integer, nullable=False)
