#!/usr/bin/env python3

from templates import login_page, secret_page, after_login_incorrect
import cgi
import cgitb
cgitb.enable()

import secret
import os
from http.cookies import SimpleCookie

print(login_page())

s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")
print()

form_ok = username == secret.username and password == secret.password

print("Content-Type: text/html")
if form_ok:
    print(f"Set-Cookie:username={username}")
    print(f"Set-Cookie:username={password}")

print()

cookie = SimpleCookie(os.environ['HTTP_COOKIE'])
cookie_username = None
cookie_password = None
if cookie.get("username"):
    cookie_username = cookie.get('username').value
if cookie.get('password'):
    cookie_password = cookie.get('password').value


right_cookie = cookie_username == secret.username and cookie_password == secret.password
right_fields = username == secret.username and password == secret.password

if username == None and password == None:
    # print(login_page())
    pass
elif right_fields:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())

