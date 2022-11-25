from flask import Flask, redirect, session, url_for,request
from urllib.parse import urlparse, urljoin
from jinja2.utils import generate_lorem_ipsum

app = Flask(__name__)

@app.route('/post')
def show_post():
    post_body = generate_lorem_ipsum(n=2) # 生成两段随机文本
    return '''
    <h1>A very long post</h1>
    <div class="body">%s</div>
    <button id="load">Load More</button>
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script type="text/javascript">
    $(function() {
        $('#load').click(function() {
            $.ajax({
                url: '/more', // 目标URL
                type: 'get', // 请求方法
                success: function(data){ // 返回2XX响应后触发的回调函数
                    $('.body').append(data); // 将返回的响应插入到页面中
                }
            })
        })
    })
    </script>''' % post_body

@app.route('/more')
def load_post():
    return generate_lorem_ipsum(n=1)

# -----------------------------------------------------
# def is_safe_url(target):
#     ref_url = urlparse(request.host_url)
#     test_url = urlparse(urljoin(request.host_url, target))
#     return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc
#
# @app.route('/foo')
# def foo():
#     resp = '<h1>Foo page</h1><a href=%s>Do something</a>' % url_for('do_something',next=request.full_path)
#     return resp
#
# @app.route('/bar')
# def bar():
#     resp = '<h1>Bar page</h1><a href=%s>Do something</a>' % url_for('do_something',next=request.full_path)
#     return resp
#
# @app.route('/do_something')
# def do_something():
#     return redirect_back()
#     # return redirect(request.args.get('next'))
#     # return redirect(request.referrer)
#     # return redirect(url_for('hello'))
#
# @app.route('/hello')
# def hello():
#     return '<h1>hello,这是默认视图!</h1>'
#
# def redirect_back(default='hello', **kwargs):
#     for target in request.args.get('next'), request.referrer:
#         if not target:
#             continue
#         if is_safe_url(target):
#             return redirect(target)
#     return redirect(url_for(default, **kwargs))

# ---------------------------------------------------
# app.secret_key = 'secret string'
#
# @app.route('/login')
# def login():
#     session['logged_in'] = True
#     return redirect(url_for('hello'))
#
# @app.route('/')
# @app.route('/hello')
# def hello():
#     name = request.args.get('name')
#     if name is None:
#         name = request.cookies.get('name', 'Human')
#         resp = '<h1>hello,%s!</h1>' % name
#         if 'logged_in' in session:
#             resp += '[Authenticated]'
#         else:
#             resp += '[Not Authenticated]'
#     return resp
#
# @app.route('/logout')
# def logout():
#     if 'logged_in' in session:
#         session.pop('logged_in')
#     return redirect(url_for('hello'))