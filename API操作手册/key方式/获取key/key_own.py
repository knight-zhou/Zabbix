#coding:utf-8
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
# create request object
request = urllib2.Request(url,data)
for key in header:
    request.add_header(key,header[key])
    result = urllib2.urlopen(request)
    response = json.loads(result.read())
    result.close()
    print "Auth Successful. The Auth ID Is:",response['result']