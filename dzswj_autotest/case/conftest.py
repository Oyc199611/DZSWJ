# -*- coding:utf-8 -*-
import os
import time

import pytest

from dzswj_autotest.api.get_token import Get_Token
from dzswj_autotest.common.yml_util import YamlUtil


@pytest.fixture(scope="function", autouse=False)  # autouse=False需要手动调用，作用于函数，fixture下面的函数可以作为一个参数被调用
# 作用于类就是scope="class"
def conn_database():
    print("数据库连接")
    # 类似于唤醒teardown功能，唤醒后置
    yield
    print("关闭数据库")


# # 暂时未用到，用的场景很少，一般用数据驱动
# # autouse=False需要手动调用，作用于函数，fixture下面的函数可以作为一个参数被调用，作用于类就是scope="class";ids="参数别名";name="固件别名"
# # name="固件别名"，如果定义了固件别名，引用fixture下面的函数时需要用别名
# @pytest.fixture(scope="function", autouse=False,
#                 params=[["1", "1"], ["2", "2"]], ids=["参数1：", "参数2："], name="connection_database")
# def connection_database(request):  # request名称是固定的，不能动；作用：将params的第一组参数传给request
#     print("数据库连接")
#     # yield类似于唤醒teardown功能，唤醒后置
#     yield request.param  # 这个写法也是固定的，此时是param，注意不是上面的params：作用：将request的参数传给param，通过yield返回
#     # 函数中要看到这些参数就需要打印出来，比如print(connection_database)
#     print("关闭数据库")


@pytest.fixture(scope="function", autouse=False)  # 自动作用于会话不需要被调用；此处作用：每次运行时，防止yaml中键值被重复写入，始终写入一个
def clear_yaml():
    YamlUtil().clear_extract_yaml_cookie()


# 这种夹具的引用，在需要引用的类(类中的每一个方法都会引用该夹具方法)或者函数前面用：@pytest.mark.usefixtures('test_clear_yaml')
@pytest.fixture()
def test_clear_yaml():
    YamlUtil().clear_extract_yaml_cookie()


# @pytest.fixture(scope="session", autouse=True)  # 自动作用于会话不需要被调用；此处作用：每次运行时，防止yaml中键值被重复写入，始终写入一个
# def clear_yaml():
#     YamlUtil().clear_extract_yaml_cookie()

#
@pytest.fixture(scope="session", autouse=True)
def get_token():
    """前置操作获取token并传入headers"""
    Get_Token().get_token()
    # if not RequestUtil().param.get("cookie", ""):  # 没有get到Set-Cookie，跳出用例
    #     pytest.skip("未获取cookie跳过用例")
    # yield RequestUtil().session
    # RequestUtil().session.close()


# 设置环境地址
def pytest_addoption(parser):
    parser.addoption(
        "--cmdhost", action="store", default="http://10.199.20.221:8081",
        help="my option: type1 or type2"
    )


@pytest.fixture(scope="session", autouse=True)
def host(request):
    """获取命令行参数"""
    # 获取命令行参数给到环境变量
    # pytest --cmdhost 运行指定环境
    os.environ["host"] = request.config.getoption("--cmdhost")


# 测试执行完成后被调用,可以用于汇总测试结果并输出到终端，属于报告钩子
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """
    收集测试结果
    """
    # print(terminalreporter.stats)
    print("total:", terminalreporter._numcollected)
    print('passed:', len(terminalreporter.stats.get('passed', [])))
    print('failed:', len(terminalreporter.stats.get('failed', [])))
    print('error:', len(terminalreporter.stats.get('error', [])))
    print('skipped:', len(terminalreporter.stats.get('skipped', [])))
    print('成功率：%.2f' % (len(terminalreporter.stats.get('passed', [])) / terminalreporter._numcollected * 100) + '%')
    # terminalreporter._sessionstarttime 会话开始时间
    duration = time.time() - terminalreporter._sessionstarttime
    print('total times：', duration, 'seconds')

# 用例执行钩子
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     print("------------------------Start---------------------------")
#     out = yield
#     res = out.get_result()
#     print("执行结果：{}".format(res))
#     print("测试用例：{}".format(item))
#     print("测试步骤：{}".format(call))
#     print("------------------------End---------------------------")
