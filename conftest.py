import pytest
import requests
import json
from util.httpUtil import HttpUtil
from common.commonData import CommonData
http=HttpUtil()
@pytest.fixture(scope="session",autouse=True)
def session_fixture():
    path='/sys/login'
    data = {'userName': CommonData.modile,
            'password': CommonData.password}
    # data={'userName':'18210034706','password':'123456'}


    resp_login=http.post(path,data)
    CommonData.token = resp_login["object"]["token"]  # 获取token


