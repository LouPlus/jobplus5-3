from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError


class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(message='登录失败'), Email()])
    password = PasswordField('密码', validators=[DataRequired(message='登录失败'), Length(min=6)])
    submit = SubmitField('登录')

    # def validate_email(self,field):
    #     if field.data and not User.query.filter_by(email=field.data):
    #         raise ValidationError('登录失败')
    #
    # def validate_password(self,field):
    #     user=User.query.filter_by(email=self.email.data)
    #     if user and not user.check_password:
    #         raise ValidationError('登录失败')
