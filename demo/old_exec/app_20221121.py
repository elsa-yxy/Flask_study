from flask import Flask, make_response,request,abort,redirect,url_for,jsonify

app = Flask(__name__)

@app.route('/set/<name>')
def set_cookie(name):
    resp = make_response(redirect(url_for('hello')))
    resp.set_cookie('name', name)
    return resp

@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name is None:
        # 从cookie 中获取 name 值
        name = request.cookies.get('name', 'Human')
    return '<h1>hello,%s!</h1>' % name

# -----------------------------------------
# @app.route('/foo')
# def foo():
#     return jsonify(name='Gery Li', gender='male')
# -----------------------------------------
# @app.route('/404')
# def not_found():
#     abort(404)
# -----------------------------------------
# @app.route('/hi')
# def hi():
#     return redirect(url_for('hello'))
#
# @app.route('/hello')
# def hello():
#     return '<h1>hello,Flask!这里是重定向</h1>'

# -----------------------------------------
# @app.route('/hello')
# def hello():
#     # return '',302,{'Location': 'https://www.baidu.com/'}
#     return redirect('https://www.baidu.com/')
# -----------------------------------------
# colors = ['blue','white','red']
# @app.route('/color/<any(%s):color>' % str(colors)[1:-1])
# def three_colors(color):
#     return '<p>Love is patient and kind.Love is not jealous or boastful or proud or rude!</p>'
#
# @app.before_request
# def do_something():
#     pass

# -----------------------------------------
# @app.route('/goback/<int:year>')
# def go_back(year):
#     return '<p>Welcome to %d !</p>' % (2022 - year)
# -----------------------------------------
# @app.route('/hello', methods=['GET','POSt'])
# def hello():
#     return '<h1>hello,Flask!</h1>'
    # --------------------------------------------
    # # 获取查询参数 name 的值
    # name = request.args.get('name', 'Flask')
    # # 插入到返回值中
    # return '<h1>hello, %s!</h1>' % name