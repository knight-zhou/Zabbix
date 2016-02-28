#coding:utf-8
#Check if a screen named “abc” already exists
#result 
import json
import urllib2
from _mysql import result
url = "http://zabbix.knight.ren/api_jsonrpc.php"
header = {"Content-Type": "application/json"}
# request json
data = json.dumps(
{
    "jsonrpc":"2.0",
    "method":"screen.exists",
    "params":{
              "name":"abc"
              },
    "auth":"8c67fd696eb3a6a877569b9bc34d6c22",
    "id":1,
})
# create request object
request = urllib2.Request(url,data)

#print request
for key in header:
    request.add_header(key,header[key])
    result = urllib2.urlopen(request)
    for h in result:
        print h





