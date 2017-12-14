from bottle import template, Bottle,static_file,request,redirect,LocalResponse
from bottle import jinja2_template
import bottle
bottle.TEMPLATE_PATH.append('./templates/')

root = Bottle()

"""
@root.route('/login/',method="POST")
def login():
    return template('login.html')

@root.route('/login/',method="GET")
def login():
    return template('login.html')
"""

@root.route('/login/',method=['GET','POST'])
def login():
    if request.method == "GET":
        return template('login.html')
    else:
        # v = request.forms # GET,POST
        # v = request.query # GET发来的请求数据
        # v = request.body  # POST发来的请求
        # print(v)
        # from bottle import FormsDict
        u = request.forms.get('user')
        p = request.forms.get('pwd')
        return redirect('/index/')

def jinxin():
    return '<h1>金鑫大</h1>'


@root.route('/index/',method='GET')
def index():
    user_list = [
        {'id':1,'name': 'root','age': 18},
        {'id':1,'name': 'root','age': 18},
        {'id':1,'name': 'root','age': 18},
        {'id':1,'name': 'root','age': 18},
    ]
    # return template('index.html',age='root',user_list=user_list,jj=jinxin)
    # return jinja2_template('index.html',age='root',user_list=user_list,jj=jinxin)


@root.route('/sta/<path:path>')
def callback(path):
    return static_file(path, root='static')

root.run(host='localhost', port=8080)