#coding:utf-8
import json
import urllib2

url = "http://zabbix.knight.ren/api_jsonrpc.php"
header = {"Content-Type": "application/json"}
# request json
data = json.dumps(
{
    "jsonrpc":"2.0",
    "method":"host.get",
    "params":{
        "output":["hostid","name"],
        "filter":{"host":""}
    },
    "auth":"8c67fd696eb3a6a877569b9bc34d6c22",
    "id":1,
})
# create request object
request = urllib2.Request(url,data)
#带着token请求,result变量返回结果
for key in header:
    request.add_header(key,header[key])
    result = urllib2.urlopen(request)
    #print result
    #json解码
    a = json.loads(result.read())
    print a
    print a['result']
    for host in a['result']:
        #print host
        print host['name']
    
    
