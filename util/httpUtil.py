import requests
import json
from common.commonData import CommonData
common=CommonData()
class HttpUtil:
    def __init__(self):
        self.http=requests.session()
        self. headers = {'Content-Type':'application/json;charset=UTF-8'}
    def post(self,path,data):
        proxies=CommonData.proxies   #获取全局变量
        host=CommonData.host         #获取全局变量
        data_json=json.dumps(data)     #将字典形式的data转换成json格式
        if CommonData.token is not None:   #判断token是否为空，不为空则赋值，为空则不加
            self.headers['token']=CommonData.token

        resp_login= self.http.post(url=host+path,
                             proxies=proxies,
                             headers=self.headers,
                             data=data_json)
        assert resp_login.status_code==200    #检验返回码是否为200
        print(resp_login.status_code)          #获取response响应的body值
        resp_json_login=resp_login.text        #将body值转换
        resp_dict_login=json.loads(resp_json_login)
        return resp_dict_login












