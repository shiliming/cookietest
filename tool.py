from bottle import request,redirect
import sqlite3
con=sqlite3.connect('liuxiang.db')
cur=con.cursor()


def islogin():
    username=request.get_cookie('user',secret='hello')
    if username==None:
            redirect('/login')

def checkuser(username=None,password=None):
    res=cur.execute('select username from user where username=? and password=?',(username,password))
    if res.fetchone()==None:
        return False
    else:
        return True
