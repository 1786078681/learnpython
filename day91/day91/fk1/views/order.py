#__author:  Administrator
#date:  2017/3/10
from . import app

@app.route("/index/",methods=['GET','POST'])
def hello():
    print('...')
    return 'OK'
