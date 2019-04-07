# from common.commonData import CommonData
# from conftest import http
# import pytest
# import allure
# @allure.feature('修改密码模块')
# class TestChangeName:
#     @allure.story('修改密码成功')
#     # @pytest.mark.usefixtures("recoverpwd")
#     def test_changeName_success(this):                        #修改密码成功
#         data={"token":CommonData.token,
#             "userId":CommonData.userId,
#               "userName":CommonData.userName,
#               "oldPwd":CommonData.oldPwd,
#               "password":CommonData.newPwd}
#         resp=http.post("/sys/changePwd",data)
#         assert resp['code']==200
#         assert resp['msg']=='操作成功'
#
#
#
# # @pytest.fixture(autouse=True)
# #
# # def recoverpwd():
# #     pass
#
