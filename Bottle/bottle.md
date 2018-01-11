**Python的WEB框架**

###### Bottle是一个快速、简洁、轻量级的基于WSIG的微型Web框架，此框架只由一个 .py 文件，除了Python的标准库外，其不依赖任何其他模块。


    pip install bottle
    easy_install bottle
    apt-get install python-bottle
    wget http://bottlepy.org/bottle.py

###### Bottle框架大致可以分为以下部分：

- 路由系统，将不同请求交由指定函数处理
- 模板系统，将模板中的特殊语法渲染成字符串，值得一说的是Bottle的模板引擎可以任意指定：Bottle内置模板、mako、jinja2、cheetah
- 公共组件，用于提供处理请求相关的信息，如：表单数据、cookies、请求头等
- 服务，Bottle默认支持多种基于WSGI的服务，如


    server_names = {
        'cgi': CGIServer,
        'flup': FlupFCGIServer,
        'wsgiref': WSGIRefServer,
        'waitress': WaitressServer,
        'cherrypy': CherryPyServer,
        'paste': PasteServer,
        'fapws3': FapwsServer,
        'tornado': TornadoServer,
        'gae': AppEngineServer,
        'twisted': TwistedServer,
        'diesel': DieselServer,
        'meinheld': MeinheldServer,
        'gunicorn': GunicornServer,
        'eventlet': EventletServer,
        'gevent': GeventServer,
        'geventSocketIO':GeventSocketIOServer,
        'rocket': RocketServer,
        'bjoern' : BjoernServer,
        'auto': AutoServer,
    }
##### 框架的基本使用
    #!/usr/bin/env python
    # -*- coding:utf-8 -*-
    from bottle import template, Bottle
    root = Bottle()
     
    @root.route('/hello/')
    def index():
        return "Hello World"
        # return template('<b>Hello {{name}}</b>!', name="Alex")
     
    root.run(host='localhost', port=8080)
###  一、路由系统

路由系统是的url对应指定函数，当用户请求某个url时，就由指定函数处理当前请求，对于Bottle的路由系统可以分为一下几类：
- 静态路由
- 动态路由
- 请求方法路由
- 二级路由

###### 1、静态路由
    @root.route('/hello/')
    def index():
        return template('<b>Hello {{name}}</b>!', name="Alex")
###### 2、动态路由
    @root.route("/index/<pagename>")
    def hello(pagename):
        print(pagename)
        return template("index.html", msg=pagename)
    @root.route('/object/<id:int>')
    def callback(id):
        pass
     
    @root.route('/show/<name:re:[a-z]+>')
    def callback(name):
        ...
     
    @root.route('/static/<path:path>') # type path
    def callback(path):
        return static_file(path, root='static') # root: static_root_dir
###### 3、请求方法路由
    @root.route('/hello/', method='POST')
    def index():
        ...
     
    @root.get('/hello/')
    def index():
        ...
     
    @root.post('/hello/')
    def index():
        ...
     
    @root.put('/hello/')
    def index():
        ...
     
    @root.delete('/hello/')
    def index():
        ...
    
    @root.route("/index/", method=["GET", "POST"])
    def index():pass

###### 4、二级路由

    #!/usr/bin/env python
    # -*- coding:utf-8 -*-
    # filename: app01.py
    from bottle import template, Bottle
    
    app01 = Bottle()
    
    @app01.route('/hello/', method='GET')
    def index():
        return template('<b>App01</b>!')
#
    # filename: app02.py
    from bottle import Bottle
    app02 = Bottle()
    
    @app02.route("/home/", method=["post", "get"])
    def index():
        return "Hello App02--> home"
#
    #!/usr/bin/env python
    # -*- coding:utf-8 -*-
    # File: server.py
    
    from bottle import template, Bottle
    from bottle import static_file
    root = Bottle()
     
    @root.route('/hello/')
    def index():
        return template('<b>Root {{name}}</b>!', name="Gavin")
     
    from framwork_bottle import app01, app02

    root.mount('app01', app01.app01)
    root.mount('app02', app02.app02)
     
    root.run(host='localhost', port=8080)

---
### 二、模板系统

  模板系统用于将Html和自定的值两者进行渲染，从而得到字符串，然后将该字符串返回给客户端。我们知道在Bottle中可以使用 内置模板系统、mako、jinja2、cheetah等，以内置模板系统为例：

    
    <!DOCTYPE html>
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <h1>{{name}}</h1>
    </body>
    </html>
#
    #!/usr/bin/env python
    # -*- coding:utf-8 -*-
    from bottle import template, Bottle
    root = Bottle()
     
    @root.route('/hello/')
    def index():
        # 默认情况下去目录：['./', './views/']中寻找模板文件 hello_template.html
        # 配置在 bottle.TEMPLATE_PATH 中
        return template('hello_template.tpl', name='Gavin')
     
    root.run(host='localhost', port=8080)
###### 1、语法

1. 单值
1. 单行Python代码
1. Python代码快
1. Python、Html混合


>     <h1>1、单值</h1>
>     {{name}}
>      
>     <h1>2、单行Python代码</h1>
>     % s1 = "hello"
>      
>     {{s1 or "no S1"}}
>     <h1>3、Python代码块</h1>
>     <%
>         # A block of python code
>         name = name.title().strip()
>         if name == "Alex":
>             name="seven"
>     %>
>      
>      
>     <h1>4、Python、Html混合</h1>
>      
>     % if True:
>         <span>{{name}}</span>
>     % end
>     <ul>
>       % for item in name:
>         <li>{{item}}</li>
>       % end
>      </ul>


###### 2、函数 

include(sub_template, **variables)

    # 导入其他模板文件
     
    % include('header.tpl', title='Page Title') # 指定变量 title 
    Page Content
    % include('footer.tpl')
#
关闭转义

    <html>
    <head>
      <title>{{title or 'No title'}}</title>
    </head>
    <body>
        % base="<h3>abcd</h3>"
        {{base}}
        {{!base}} # 关闭转义 

rebase(name, **variables)

    # 导入母版
    % rebase('base.tpl', title='Page Title')
    <p>Page Content ...</p>
#
其他：

    defined(name)
        # 检查当前变量是否已经被定义，已定义True，未定义False
        
    get(name, default=None)
        # 获取某个变量的值，不存在时可设置默认值
        
    setdefault(name, default)
        # 如果变量不存在时，为变量设置默认值

###### 扩展：自定义函数


```
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <h1>自定义函数</h1>
    {{ custom() }}
</body>
</html>
```

```
# py
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bottle import template, Bottle,SimpleTemplate
import bottle
bottle.TEMPLATE_PATH.append('./tpl/') # add template dir
root = Bottle()

def fun1():
    return '123123'

@root.route('/hello/')
def index():
    # 默认情况下去目录：['./', './views/']中寻找模板文件 hello_template.html
    # 配置在 bottle.TEMPLATE_PATH 中
    return template('hello_template.html', name='SB', custom=func1)

root.run(host='localhost', port=8080)
```
注：变量或函数前添加 【 ! 】，则会关闭转义的功能

### 三、公共组件

由于Web框架就是用来【接收用户请求】-> 【处理用户请求】-> 【响应相关内容】，对于具体如何处理用户请求，开发人员根据用户请求来进行处理，而对于接收用户请求和相应相关的内容均交给框架本身来处理，其处理完成之后将产出交给开发人员和用户。

【接收用户请求】

> 当框架接收到用户请求之后，将请求信息封装在Bottle的request中，以供开发人员使用

【响应相关内容】

> 当开发人员的代码处理完用户请求之后，会将其执行内容相应给用户，相应的内容会封装在Bottle的response中，然后再由框架将内容返回给用户

所以，公共组件本质其实就是为开发人员提供接口，使其能够获取用户信息并配置响应内容。

###### 1、request

Bottle中的request其实是一个LocalReqeust对象，其中封装了用户请求的相关信息：

```
request.headers
    请求头信息
 
request.query
    get请求信息
 
request.forms
    post请求信息
 
request.files
    上传文件信息
 
request.params
    get和post请求信息
 
request.GET
    get请求信息
 
request.POST
    post和上传信息
 
request.cookies
    cookie信息
     
request.environ
    环境相关相关
```

###### 2、response

Bottle中的request其实是一个LocalResponse对象，其中框架即将返回给用户的相关信息：

```
response
    response.status_line
        状态行
 
    response.status_code
        状态码
 
    response.headers
        响应头
 
    response.charset
        编码
 
    response.set_cookie
        在浏览器上设置cookie
         
    response.delete_cookie
        在浏览器上删除cookie
```
实例：

```
# 基本Form请求
from bottle import route, request

@route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"
```


```
#上传文件
<form action="/upload" method="post" enctype="multipart/form-data">
  Category:      <input type="text" name="category" />
  Select a file: <input type="file" name="upload" />
  <input type="submit" value="Start upload" />
</form>


@route('/upload', method='POST')
def do_upload():
    category   = request.forms.get('category')
    upload     = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png','.jpg','.jpeg'):
        return 'File extension not allowed.'

    save_path = get_save_path_for_category(category)
    upload.save(save_path) # appends upload.filename automatically
    return 'OK'
```

### 四、服务

对于Bottle框架其本身未实现类似于Tornado自己基于socket实现Web服务，所以必须依赖WSGI，默认Bottle已经实现并且支持的WSGI有：


```
server_names = {
    'cgi': CGIServer,
    'flup': FlupFCGIServer,
    'wsgiref': WSGIRefServer,
    'waitress': WaitressServer,
    'cherrypy': CherryPyServer,
    'paste': PasteServer,
    'fapws3': FapwsServer,
    'tornado': TornadoServer,
    'gae': AppEngineServer,
    'twisted': TwistedServer,
    'diesel': DieselServer,
    'meinheld': MeinheldServer,
    'gunicorn': GunicornServer,
    'eventlet': EventletServer,
    'gevent': GeventServer,
    'geventSocketIO':GeventSocketIOServer,
    'rocket': RocketServer,
    'bjoern' : BjoernServer,
    'auto': AutoServer,
}
```
使用时，只需在主app执行run方法时指定参数即可：

```
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bottle import Bottle
root = Bottle()
 
@root.route('/hello/')
def index():
    return "Hello World"
# 默认server ＝'wsgiref'
root.run(host='localhost', port=8080, server='wsgiref')
```
默认server＝"wsgiref"，即：使用Python内置模块wsgiref，如果想要使用其他时，则需要首先安装相关类库，然后才能使用。如：

```
root.run(host='localhost', port=8080, server='tornado')
# pip install tornado
```

```
# 如果使用Tornado的服务，则需要首先安装tornado才能使用

class TornadoServer(ServerAdapter):
    """ The super hyped asynchronous server by facebook. Untested. """
    def run(self, handler): # pragma: no cover
        # 导入Tornado相关模块
        import tornado.wsgi, tornado.httpserver, tornado.ioloop
        container = tornado.wsgi.WSGIContainer(handler)
        server = tornado.httpserver.HTTPServer(container)
        server.listen(port=self.port,address=self.host)
        tornado.ioloop.IOLoop.instance().start()
# 更多参见：http://www.bottlepy.org/docs/dev/index.html
```

> PS：以上WSGI中提供了19种，如果想要使期支持其他服务，则需要扩展Bottle源码来自定义一个ServerAdapter



更多参见: [bottle-docs-dev](http://www.bottlepy.org/docs/dev/index.html)