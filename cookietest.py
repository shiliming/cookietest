# -*- coding: cp936 -*-
from bottle import run,template,request,response,route,redirect
from tool import islogin,checkuser

@route('/login')
def login(user='shiliming'):
        return template('views\login')

@route('/login_post',method='post')
def login_post():
        username=request.forms.get('username')
        password=request.forms.get('password')
        if checkuser(username,password):
                response.set_cookie('user',username,secret='hello')
                redirect('/')
        else:
                return template('views\login_error')

@route('/')
def default ():
        islogin()
        return template('views\default')

run(port=80,reloader=True,debug=True)
