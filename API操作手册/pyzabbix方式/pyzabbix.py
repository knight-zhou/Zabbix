#coding:utf-8
from pyzabbix import ZabbixAPI
a = ZabbixAPI("http://zabbix.knight.ren")
#print a
a.login("admin", "zabbix")
#print a.api_version()
#print a.host.get(output="extend")
#以字典形式列出
for h in a.host.Get(output="extend"):
    #print h['hostid']
    print h['host']




