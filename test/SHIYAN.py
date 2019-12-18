import pytest

@pytest.fixture(scope='function')
def func_scope():
    print("函数级别的fixtue")
@pytest.fixture(scope='module')
def module_scope():
    print("模块级别的fixtue")
@pytest.fixture(scope='session')
def session_scope():
    print("会话级别的fixtue")
@pytest.fixture(scope='class')
def class_scope():
    print("类级别的fixtue")

def test_func_01(func_scope,module_scope,session_scope):
    print("执行函数一")
def test_func_02(func_scope,module_scope,session_scope):
    print("执行函数2")

@pytest.mark.usefixtures('class_scope')
class Test_class():
    def test_func_03(self):
        print("执行类函数3")

    def test_func_04(self):
        print("执行类函数4")