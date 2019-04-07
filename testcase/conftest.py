import pytest
@pytest.fixture(scope="module",autouse=False)
def module_fixture():
    print("module执行")
    yield
    print("module完成")

import pytest
@pytest.fixture(scope="class",autouse=False)
def class_fixture():
    print("class执行")
    yield
    print("class完成")


import pytest
@pytest.fixture(scope="function",autouse=False)
def function_fixture():
    print("function执行")
    yield
    print("function完成")