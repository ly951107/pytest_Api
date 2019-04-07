import pytest
from common.commonData import CommonData
from conftest import http
import allure
@allure.feature('登录模块')
class TestLogin:
    @allure.story('登录成功')
    @pytest.mark.debug
    def test_login_success(this):                        #用户登录成功
        data={'userName':CommonData.modile,
              'password':CommonData.password}
        resp=http.post("/sys/login",data)
        assert resp['code']==200
        assert resp['msg']=='操作成功'
        assert resp['object']['userId']==2

    @allure.story('登录失败——密码错误')
    @pytest.mark.debug
    def test_login_fail_pws(self):                          #用户名或密码错误
        data = {'userName': CommonData.modile,
                'password': '1234567'}
        resp = http.post("/sys/login", data)
        assert resp['code'] == 410
        assert resp['msg'] == '用户名或密码错误'
        # assert resp['object'] =='null'

    @allure.story('登录失败——用户名错误')
    @pytest.mark.debug
    def test_login_fail_name1(self):                        #用户名错误
        data = {'userName': '用户',
                'password': '1234567'}
        resp = http.post("/sys/login", data)
        assert resp['code'] ==301
        assert resp['msg'] == '用户不存在'

    @allure.story('登录失败——用户名长度超出')
    @pytest.mark.debug
    def test_login_fail_name2(self):                         #用户名长度超出
        data = {'userName': 'abcdefghijklmnopqistovwsrt',
                'password': '1234567'}
        resp = http.post("/sys/login", data)
        assert resp['code'] ==301
        assert resp['msg'] == '用户不存在'

    @allure.story('登录失败——用户名为空1')
    @pytest.mark.debug
    def test_login_fail_name3(self):                        #用户名为空1
        data = {
                'password': '1234567'}
        resp = http.post("/sys/login", data)
        assert resp['code'] ==301
        # assert resp['msg'] == '操作成功'

    @allure.story('登录失败——用户名为空2')
    @pytest.mark.debug
    def test_login_fail_name4(self):                        #用户名为空2
        data = {'userName': '',
                'password': '1234567'}
        resp = http.post("/sys/login", data)
        assert resp['code'] ==3010
        # assert resp['msg'] == '用户不存在'






