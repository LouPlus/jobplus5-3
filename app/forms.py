from os import abort

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,IntegerField,FileField,TextAreaField
from wtforms.validators import DataRequired, Email, Length, ValidationError,EqualTo,InputRequired

from app.models import User, db, Jobseeker, Company


class LoginForm(FlaskForm):
    userEmail = StringField('邮箱', validators=[DataRequired(message='登录失败'), Email()])
    userPassword = PasswordField('密码', validators=[DataRequired(message='登录失败'), Length(min=6)])
    submit = SubmitField('登录')

    def validate_userEmail(self,field):
        if field.data and not User.query.filter_by(userEmail=field.data).first_or_404():
            raise ValidationError('登录失败')

    def validate_userPassword(self,field):
        user=User.query.filter_by(userEmail=self.userEmail.data).first_or_404()
        if user and not user.check_password(field.data):
            raise ValidationError('登录失败')

class RegisterForm(FlaskForm):
    userName=StringField('用户名',validators=[DataRequired('注册失败'),Length(min=6)])
    userEmail=StringField('邮箱',validators=[DataRequired('注册失败'),Email()])
    userPassword=PasswordField('密码',validators=[DataRequired('注册失败'),Length(min=6,max=36)])
    re_userPassword=PasswordField('重复密码',validators=[DataRequired('注册失败'),Length(min=6,max=36),EqualTo('userPassword')])
    submit=SubmitField('提交')

    def create_user(self,type):
        user=User()
        self.populate_obj(user)
        if type=='jobseeker':
            user.userRole=User.ROLE_JOBSEEKER
        elif type=='company':
            user.userRole=User.ROLE_COMPANY
        else:
            abort(404)
        db.session.add(user)
        db.session.commit()
        return user



class CompanyProfile(FlaskForm):
    userName = StringField('企业名称', validators=[DataRequired('更新失败'), Length(min=6)])
    userEmail = StringField('邮箱', validators=[DataRequired('注册失败'), Email()])
    password = PasswordField('密码(不填表示保持不变)')
    userPhone = StringField('手机号',)
    companySlug= StringField('Slug')
    companyCity = StringField('地址')
    companyHomepage = StringField('公司网站')
    companyIntroduction= StringField('一句话描述')
    companyDescription= TextAreaField('公司详情')
    submit=SubmitField('提交')

    def update_profile(self,user_id):
        user=User.query.filter_by(id=user_id).first_or_404()
        if self.password.data != '':
            user.userPassword=self.password.data
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return user





class JobseekerProfile(FlaskForm):
    userName=StringField('姓名',validators=[DataRequired('更新失败'),Length(min=6)])
    userEmail=StringField('邮箱',validators=[DataRequired('注册失败'),Email()])
    password=PasswordField('密码(不填表示保持不变)')
    userPhone=StringField('手机号')
    jobseekerExperience=IntegerField('工作年限')
    jobseekerResume=FileField('上传简历')
    submit=SubmitField('提交')

    def update_profile(self,user_id):
        user = User.query.filter_by(id=user_id).first_or_404()
        if self.password.data != '':
            user.userPassword = self.password.data
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return user




