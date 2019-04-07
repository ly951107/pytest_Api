from conftest import http
from common.commonData import CommonData
import pytest
import random
import allure
@allure.feature('新增用户')
class TestSaveOrUpdateUser:

    #TestSaveOrUpdateUser
    @allure.story('注册用户成功')
    @pytest.mark.debug
    def test_saveOrUpdateUser(self):                          #注册用户成功
        nickName=str(random.randint(10000000,11111111))
        mobile="155"+nickName
        data={"nickName":nickName,
              "userName":mobile,
              "telNo": "",
              "email": "",
              "address": "",
              "roleIds": "1",
              "regionId": 1,
              "regionLevel": 1

              }
        resp=http.post("/user/saveOrUpdateUser",data)
        # assert resp['code']==200
        # assert resp['msg']=='操作成功'




    #TestLogin_admin
    # #用户登录成功
        login_data={"userName":mobile,
	            "password": CommonData.password}
        resp=http.post("/sys/login",login_data)
        assert resp['code'] == 200
        assert resp['msg'] == '操作成功'
        useridadmin=resp['object']['userId']
        print("用户id：",useridadmin)

    # TestLoadUserList
    # 请求获取用户列表成功
        select_data = {"token": CommonData.token,
                        "pageCurrent": 1,
	                    "pageSize": 10,
	                    "nickName": "",
	                    "userName": "",
	                    "regionId": 1}
        resp = http.post("/user/loadUserList", select_data)
        useridGuanLiYuan = resp['object']['list'][0]["id"]
        print("管理员查看id:",useridGuanLiYuan)
        assert resp['code'] == 200
        assert resp['msg'] == '操作成功'
        assert useridGuanLiYuan==useridadmin


