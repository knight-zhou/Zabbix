#coding:utf-8
#改写如下
import json
import urllib2
# based url and required header
url = "http://zabbix.knight.ren/api_jsonrpc.php"
header = {"Content-Type": "application/json"}
# auth user and password
data = json.dumps(
{
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
    "user": "Admin",
    "password": "zabbix"
},
"id": 0
})
# create request object,带着token请求数据
request = urllib2.Request(url,data)
for key in header:
    request.add_header(key,header[key])
    result = urllib2.urlopen(request)
    #返回json数据格式，也可以认为是字典形式，最后用程序处理即可
    for i in result:
        print i
    #response = json.loads(result.read())
    #result.close()
    #print "Auth Successful. The Auth ID Is:",response['result']