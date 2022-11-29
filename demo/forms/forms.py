# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
# 导入表单字段类型
from wtforms import StringField, PasswordField, BooleanField, \
    SubmitField, IntegerField,MultipleFileField, TextAreaField
# 导入验证函数
from wtforms.validators import DataRequired, Length, ValidationError, Email
import email_validator
from flask_ckeditor import CKEditorField


# 定义WTForms 表单类
class LoginForm(FlaskForm):
    # DataRequired()验证数据有效性，内容不为空
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')

# 自定义验证器
class FortyTwoForm(FlaskForm):
    answer = IntegerField('The Number')
    submit = SubmitField()

    def validate_answer(self, form, field):
        if field.data != 42:
            raise ValidationError('Must be 42.')

# 创建上传表单
class UploadForm(FlaskForm):
    photo = FileField('Upload Image', validators=[FileRequired(), FileAllowed(['jpg','jpeg','png','gif'])])
    submit = SubmitField()

# 创建多文件上传
class MultiUploadForm(FlaskForm):
    photo = MultipleFileField('Upload Image', validators=[FileRequired()])
    submit = SubmitField()

# 创建富文本编辑器
class RichTextForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 50)])
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField('Publish')

# 包含两个按钮
class NewPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 50)])
    body = TextAreaField('Body', validators=[DataRequired()])
    publish = SubmitField('Publish')    #发布按钮
    save = SubmitField('Save')  # 保存按钮

class SigninForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    submit1 = SubmitField('Sign in')

class SigninForm2(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    submit1 = SubmitField('Sign in')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 254)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    submit2 = SubmitField('Register')

class RegisterForm2(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 254)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    submit2 = SubmitField('Register')