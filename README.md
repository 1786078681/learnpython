# learnpython
python example


#Web框架
    - bottle
    - flask
    - tornado
    
    # 三大组件
        - 路由系统
        - 控制器（含模版渲染）
        - 数据库操作
    # 微型框架
        - 依赖第三方写的socket，WSGI
        - 本身功能少
        
    # 安装
        pip3 install bottle
        pip3 install flask
        pip3 install tornado
    
    # 博客示例
    http://www.cnblogs.com/wupeiqi/articles/5341480.html 
    
    1. bottle
        a. 路由系统
            - 静态
            - 动态
            - 方法
            - 二级
        b. 视图
            - 获取用户内容 request
            - 数据库操作
            - 文件操作
            - ...
            - 返回给用户内容return ""
            - 模版引擎渲染
        c. WSGI进行配置
        
    2. flask
        - 13点
        
    3. Tornado
        - 异步非阻塞的框架 Node.js
        
        
        
    模版语言：
        Django: ORM，模板引擎
        bottle: 模板引擎
        SqlAchmey： ORM
        JinJa2: 模板引擎
        

    
二、Web组件的定制
    1. Session
        a. 请求到来
            - 用户浏览器设置cookie   {'session_id':随机字符串}
            - 
               session = {
                    随机字符串: {login:true}
                    随机字符串: {login:true}
               }
    
    
    2. Form组件
        a. 表单验证
            - 写Form类
            - 定义Form类中的字段
            - 用户发送
            - obj = Form(请求数据)
               obj.is_valid()
               obj.cleaned_data
    
    
# ****ELSE****
router is three:

pattern=((r"^$", xxx),)

@root.route("/")

url=[('/?P<controller>\w+/?P<action>\w+'),]

from bottle import request

request.forms # GET and POST request data# form
request.query # GET method request data  ?page=3&..
request.body  # POST ..data
request.params # GET or POST data, forms or ?page=xx..
#
root.mount("games", server1.games) # server1.games = Bottle()
root.mount("users", server1.users)
root.mount("app02", app02.root)
bottle.TEMPLATE_PATH.append("./tpl/"), add template dir
    
    