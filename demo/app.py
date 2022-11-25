from flask import Flask, render_template, flash, redirect, url_for, Markup
from forms.forms import LoginForm, UploadForm

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = "secret string"
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024  # 3MB

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/html')
def pure_html():
    return render_template('pure_html.html')


@app.route('/basic', methods=['GET', 'POST'])
def basic_login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        flash("Welcome home, %s!" % username)
        return redirect(url_for('index'))
    return render_template('basic.html', form=form)


@app.route('/bootstrap', methods=['GET', 'POST'])
def bootstrap():
    form = LoginForm()
    return render_template('bootstrap.html', form=form)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    return render_template('upload.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('errors/500.html'),500

@app.template_global()
def bar():
    return 'I am bar.'

@app.template_filter()
def musical(s):
    return s + Markup(' &#9835;')

@app.template_test()
def baz(n):
    if n == 'baz':
        return True
    return False

