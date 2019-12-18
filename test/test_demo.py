#!/usr/bin/env python
# coding=utf-8
import conftest
import pytest
import allure
@allure.feature('购物车功能')  # feature定义功能
class TestShoppingTrolley(object):
    @allure.story('加入购物车')  # story定义用户场景
    def test_add_shopping_trolley(self):
        login('刘春明', '密码')  # 调用“步骤函数”
        with allure.step("浏览商品"):  # 将一个测试用例分成几个步骤，将步骤打印到测试报告中，步骤2
            allure.attach('商品1', '刘春明')  # attach可以打印一些附加信息
            allure.attach('商品2', 'liuchunming')
        with allure.step("点击商品"):  # 将一个测试用例分成几个步骤，将步骤打印到测试报告中，步骤3
            allure.attach('点击商品')
        with allure.step("校验结果"):
            allure.attach('期望结果', '添加购物车成功')
            allure.attach('实际结果', '添加购物车失败')
            # assert 'success' == 'failed'

    @allure.story('修改购物车0')
    def test_edit_shopping_trolley(self):
        allure.attach('修改购物车1')

    @pytest.mark.skipif(reason='本次不执行')
    @allure.story('删除购物车2')
    def test_delete_shopping_trolley(self):
        allure.attach('删除购物车3')

    def test_skip(self):
       """this test is skipped"""
       pytest.skip('for a reason!')

    def test_broken(self):
      raise Exception('oops')

    @pytest.mark.xfail(condition=lambda: False, reason='this test is expecting failure')
    def test_xfail_expected_failure(self):
        """this test is an xfail that will be marked as expected failure"""
        assert False

    @pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
    def test_xfail_unexpected_pass(self):
        """this test is an xfail that will be marked as unexpected success"""
        assert True

    @pytest.mark.abc(condition=lambda: True, reason='this test is expecting failure')
    def test_mark(self):
        """给测试用例进行mark分组，运行"""
        print('test_mark')

    @pytest.mark.finished1
    def test_func1(self):
        assert 1 == 1

    @pytest.mark.skip(reason='out-of-date api')
    def test_connect(self):
        '''加一个跳过的装饰器'''
        pass

    @pytest.mark.skipif(reason='not supported until v0.2.0')
    def test_api(self):
        '''如果满足跳过条件则跳过'''
        pass

    @pytest.mark.parametrize('passwd',
                             ['123456',
                              'abcdefdfs',
                              'as52345fasdf4'])
    def test_passwd_length(self,passwd):
        assert len(passwd) >= 8

    @pytest.mark.parametrize('user, passwd',
                             [('jack', 'abcdefgh'),
                              ('tom', 'a123456a')])
    def test_passwd_md5(self,user, passwd):
        db = {
            'jack': 'e8dc4081b13434b45189a720b77b6818',
            'tom': '1702a132e769a623c1adb78353fc9503'
        }
        import hashlib
        assert hashlib.md5(passwd.encode()).hexdigest() == db[user]

    @pytest.fixture()
    def postcode(self):
        return '010'

    def test_postcode(self,postcode):
        assert postcode == '010'

@allure.step('用户登录')  # 还可以将一个函数作为一个步骤，调用此函数时，报告中输出一个步骤，步骤名字通常是函数名，我把这样的函数叫“步骤函数”
def login(user, pwd):
    print(user, pwd)

@pytest.fixture()
def db():
    print('Connection successful')
    yield
    print('Connection closed')


def search_user(user_id):
    print(user_id)
    d = {
        '001': 'xiaoming'
    }
    print(d[user_id])
    return d[user_id]

#固件重命名
@pytest.fixture(name='age')
def calculate_average_age():
    return 28

def test_age(age):
    assert age == 28



def test_search(db):
    assert search_user('001') == 'xiaoming'