from conftest import http
from common.commonData import CommonData
import allure
@allure.feature('退出模块')
class TestLogout:
    @allure.story('退出成功')
    def test_logout(self):
        data={ "token":CommonData.token}
        resp=http.post("/sys/logout",data)
        assert resp["code"]

