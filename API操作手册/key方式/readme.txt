(1)����zabbix API
post json���ݵ�api�ӿڵ�ַ���������zabbix��ַ��http://company.com/zabbix��
��ô��ýӿڵ�ַ�ǣ�http://company.com/zabbix/api_jsonrpc.php��
�������content-typeͷ��ֵΪapplication/json-rpc, application/json or application/jsonrequest֮һ��

(2)
zabbix api��������
ͨ����֤֮�����Ǵ���tokenʹ��host.get��ȡ�����б������json���£�
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

��ȡ����������

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

ʹ����ĳ�����һ�¼��ɡ�