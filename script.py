from flask import request
import requests
import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
req = requests.get('https://www.commonwebsite.com');
req.status_code

rHeaders = r.headers['Content-type'];

if req.status_code == 200 && rHeaders == 'text/html; charset=UTF=8'
    request_status = 1
else 
    request_status = 0
    

def block_method()
    ip = request.environ.get(IPAddr)
    if ip in ip_ban_list:
        abort(403)

if request_status = 0
    block_method;
    