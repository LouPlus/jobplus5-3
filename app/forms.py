from os import abort

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,IntegerField,FileField,TextAreaField,SelectField
from wtforms.validators import DataRequired, Email, Length, ValidationError,EqualTo,InputRequired

from app.models import User, db, Company, Job


class LoginForm(FlaskForm):
    user_email = StringField('邮箱', validators=[DataRequired(message='登录失败'), Email()])
    user_password = PasswordField('密码', validators=[DataRequired(message='登录失败'), Length(min=6)])
    submit = SubmitField('登录')

    def validate_user_email(self,field):
        if field.data and not User.query.filter_by(user_email=field.data).first_or_404():
            raise ValidationError('登录失败')

    def validate_user_password(self,field):
        user=User.query.filter_by(user_email=self.user_email.data).first_or_404()
        if user and not user.check_password(field.data):
            raise ValidationError('登录失败')

class RegisterForm(FlaskForm):
    user_name=StringField('用户名',validators=[DataRequired('注册失败'),Length(min=6)])
    user_email=StringField('邮箱',validators=[DataRequired('注册失败'),Email()])
    user_password=PasswordField('密码',validators=[DataRequired('注册失败'),Length(min=6,max=36)])
    re_user_password=PasswordField('重复密码',validators=[DataRequired('注册失败'),Length(min=6,max=36),EqualTo('user_password')])
    submit=SubmitField('提交')

    def create_user(self,type):
        user=User()
        self.populate_obj(user)
        if type=='jobseeker':
            user.user_role=User.ROLE_JOBSEEKER
        elif type=='company':
            user.user_role=User.ROLE_COMPANY
            user.company_detail=Company()
        else:
            abort(404)
        db.session.add(user)
        db.session.commit()
        return user



class CompanyProfile(FlaskForm):
    user_name = StringField('企业名称', validators=[DataRequired('更新失败'), Length(min=6)])
    user_email = StringField('邮箱', validators=[DataRequired('注册失败'), Email()])
    password = PasswordField('密码(不填表示保持不变)')
    user_phone = StringField('手机号',)
    company_slug= StringField('Slug')
    company_city = StringField('地址')
    company_logo=StringField('Logo')
    company_homepage = StringField('公司网站')
    company_introduction= StringField('一句话描述')
    company_description= TextAreaField('公司详情')
    submit=SubmitField('提交')

    def update_profile(self,user_id):
        user=User.query.filter_by(id=user_id).first_or_404()
        if self.password.data != '':
            user.user_password=self.password.data
        self.populate_obj(user)
        self.populate_obj(user.company)
        db.session.add(user)
        db.session.commit()
        return user





class JobseekerProfile(FlaskForm):
    user_name=StringField('姓名',validators=[DataRequired('更新失败'),Length(min=6)])
    user_email=StringField('邮箱',validators=[DataRequired('注册失败'),Email()])
    password=PasswordField('密码(不填表示保持不变)')
    user_phone=StringField('手机号')
    jobseeker_experience=IntegerField('工作年限')
    jobseeker_resume=FileField('上传简历')
    submit=SubmitField('提交')

    def update_profile(self,user_id):
        user = User.query.filter_by(id=user_id).first_or_404()
        if self.password.data != '':
            user.user_password = self.password.data
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return user
class publish_job(FlaskForm):
    job_name = StringField('职位名称', validators=[DataRequired('发布失败'), Length(min=1)])
    job_salary_l = StringField('最低薪酬', validators=[DataRequired('发布失败'), Length(min=1)])
    job_salary_h = StringField('最高薪酬', validators=[DataRequired('发布失败'), Length(min=1)])
    job_address = StringField('工作地点', validators=[DataRequired('发布失败'), Length(min=1)])
    job_tag = StringField('职位标签（多个用,隔开）', validators=[DataRequired('发布失败'), Length(min=1)])
    job_experience = SelectField('经验要求(年)',choices=[('1','不限'),('1',"1"),('2',"2"),('3',"3"),('4',"1-3"),('5',"3-5"),('6',"5+")])
    job_education = SelectField('学历要求',choices=[('0',"不限"),('1',"专科"),('2',"本科"),('3',"硕士"),('4',"博士")])
    job_description = TextAreaField('职位描述', validators=[DataRequired('发布失败'), Length(min=1)])
    submit = SubmitField('提交')

    def publish(self,company):
        job=Job()
        self.populate_obj(job)
        job.job_company=company.id
        db.session.add(job)
        db.session.commit()
        return job




