# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
# 导入表单字段类型
from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField, IntegerField
# 导入验证函数
from wtforms.validators import DataRequired, Length, ValidationError


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