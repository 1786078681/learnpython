#__author:  Administrator
#date:  2017/3/10

from flask import Flask,render_template,request,make_response,redirect,url_for,session
app = Flask(__name__,template_folder="templates")