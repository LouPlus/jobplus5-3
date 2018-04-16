from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    create_time = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)


class User(Base):
    __tablename__ = 'user'

    ROLE_JOBSEEKER = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    userId = db.Column(db.Integer, primary_key=True,
                       nullable=False, unique=True)
    userEmail = db.Column(db.String(255), nullable=False, unique=True)
    _userPassword = db.Column('userPassword', db.String(256), nullable=False)
    userRole = db.Column(db.Integer, nullable=False, default=ROLE_JOBSEEKER)

    @property
    def userPassword(self):
        return self._userPassword

    @password.setter
    def userPassword(self, orig_password):
        self._userPassword = generate_password_hash(orig_password)

    def check_password(self, password):
        return check_password_hash(self._userPassword, password)


class Jobseeker(Base):
    __tablename__ = 'jobseeker'

    jobseekerId = db.Column(db.Integer, nullable=False)
    jobseekerName = db.Column(db.String(20), nullable=False)
    jobseekerPhone = db.Column(db.String(15), nullable=False)
    jobseekerResume = db.Column(db.String(1024), nullable=False)


class Company(Base):
    __tablename__ = 'company'

    companyId = db.Column(db.Integer, nullable=False)
    companyName = db.Column(db.String(255), nullable=False)
    compangHomepage = db.Column(db.String(1024))
    companyField = db.Column(db.String(20), nullable=False)
    companyFinancing = db.Column(db.String(20))
    companyCity = db.Column(db.String(20), nullable=False)
    companyLogo = db.Column(db.String(255), nullable=False)
    companyIntroduction = db.Column(db.String(1024), nullable=False)
    companyDescription = db.Column(db.String(4096), nullable=False)


class Job(Base):
    __tablename__ = 'job'

    jobId = db.Column(db.Integer, nullable=False)
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

    deliveryId = db.Column(db.Integer, nullable=False)
    deliveryJob = db.Column(db.Integer, nullable=False)
    deliveryCompany = db.Column(db.Integer, nullable=False)
    deliveryJobseeker = db.Column(db.Integer, nullable=False)
    deliveryStatus = db.Column(db.Integer, nullable=False)
