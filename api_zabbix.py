from pyzabbix import ZabbixAPI


def login_no_zabbix():
    zapi = ZabbixAPI("http://179.190.52.148:4444/zabbix")
    zapi.login("Admin", "zabbix")
    return( zapi)

def pesquisa_item_por_key_texto(zapi):

    items = zapi.item.get(output="extend", search={'key_':"a3tech.get"}, groupids="26")

    lista_de_hostid=[]
    if  (len(items) > 0 ):
        for i in items :
            lista_de_hostid.append(i["hostid"])
            print(i["hostid"])

    # x = zapi.hostgroup.get(output="extend")
    x = zapi.host.get(output="extend", hostids=lista_de_hostid)

    #y=[d['host'] for d in x]
    y=[]
    for i in x :
        hostid=i["hostid"]
        host=i["host"]

        #y.append(dic)
        z= [p["lastvalue"] for p in items if p['hostid'] == hostid]

        z=z[0].strip().split("\n")
        for j in z :
            dic={"hosp":host.split("-")[1],"vm":j}
            print(dic)
            y.append(dic)



    #historico_da_key= zapi.history.get(output="extend" , history= 4 , sortfield =  "clock",sortorder = "DESC",  limit = 6 , groupids= ["26"])

    return(y)