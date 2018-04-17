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


class Jobseeker(db.Model):
    __tablename__ = 'jobseeker'
    __abstract__=True
    jobseekerExperience = db.Column(db.Integer, nullable=True)
    jobseekerResume = db.Column(db.String(1024), nullable=True)


class Company(db.Model):
    __tablename__ = 'company'
    __abstract__=True
    companyHomepage = db.Column(db.String(1024),nullable=True)
    companyField = db.Column(db.String(20), nullable=True)
    companyFinancing = db.Column(db.String(20), nullable=True)
    companyCity = db.Column(db.String(20), nullable=True)
    companyLogo = db.Column(db.String(255), nullable=True)
    companyIntroduction = db.Column(db.String(1024), nullable=True)
    companyDescription = db.Column(db.String(4096), nullable=True)
    companySlug=db.Column(db.String(1024),nullable=True)


class User(Base, UserMixin, Jobseeker, Company):
    __tablename__ = 'user'
    ROLE_JOBSEEKER = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, unique=True)
    userName = db.Column(db.String(255), nullable=False)
    userEmail = db.Column(db.String(255), nullable=False, unique=True)
    _userPassword = db.Column('userPassword', db.String(256), nullable=False)
    userRole = db.Column(db.Integer, nullable=False, default=ROLE_JOBSEEKER)
    userPhone = db.Column(db.String(15), nullable=True)

    @property
    def userPassword(self):
        return self._userPassword

    @userPassword.setter
    def userPassword(self, orig_password):
        self._userPassword = generate_password_hash(orig_password)

    def check_password(self, password):
        return check_password_hash(self._userPassword, password)


class Job(Base):
    __tablename__ = 'job'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    jobName = db.Column(db.String(255), nullable=False)
    jobTag = db.Column(db.String(255), nullable=False)
    jobDescription = db.Column(db.String(4096), nullable=False)
    jobAddress = db.Column(db.String(1024), nullable=False)
    jobSalaryL = db.Column(db.Integer, nullable=False)
    jobSalaryH = db.Column(db.Integer, nullable=False)
    jobExperience = db.Column(db.String(255), nullable=False)
    jobEducation = db.Column(db.String(255), nullable=False)
    jobCompany = db.Column(db.Integer, nullable=False)


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
