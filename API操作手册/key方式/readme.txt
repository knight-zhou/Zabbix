(1)请求zabbix API
post json数据到api接口地址，例如你得zabbix地址是http://company.com/zabbix，
那么你得接口地址是：http://company.com/zabbix/api_jsonrpc.php，
必须包含content-type头，值为application/json-rpc, application/json or application/jsonrequest之一。

(2)
zabbix api检索主机
通过验证之后，我们带着token使用host.get获取主机列表，请求的json如下：
{
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": [
            "hostid",
            "host"
        ],
        "selectInterfaces": [
            "interfaceid",
            "ip"
        ]
    },
    "id": 2,
    "auth": "0424bd59b807674191e7d77572075f33"
}

获取到如下数据

{
    "jsonrpc": "2.0",
    "result": [
        {
            "hostid": "10084",
            "host": "Zabbix server",
            "interfaces": [
                {
                    "interfaceid": "1",
                    "ip": "127.0.0.1"
                }
            ]
        }
    ],
    "id": 2
}

使用你的程序处理一下即可。