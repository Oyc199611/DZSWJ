# NOTE: Generated By HttpRunner v4.3.5
# FROM: tq_login.yml
from httprunner import HttpRunner, Config, Step, RunRequest


class TestCaseTqLogin(HttpRunner):

    config = Config("testcase description")

    teststeps = [
        Step(
            RunRequest("/user/login")
            .post("https://www.tianqiapi.com/user/login")
            .with_headers(
                **{
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
                    "X-Requested-With": "XMLHttpRequest",
                    "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                }
            )
            .with_data(
                {
                    "password": "ouyangchao199611",
                    "registerSubmit": "",
                    "username": "13767594293@163.com",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.errcode", 0)
            .assert_equal("body.errmsg", "success")
        ),
    ]


if __name__ == "__main__":
    TestCaseTqLogin().test_start()
