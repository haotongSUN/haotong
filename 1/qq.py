import requests
import logging
import json

logging.basicConfig(level=logging.INFO)

qq = "http://www.qq.com/"
qq_login = "https://ui.ptlogin2.qq.com/cgi-bin/login?daid=164&target=self&style=5&mibao_css=m_webqq&appid=501004106&enable_qlogin=0&no_verifyimg=1&s_url=http%3A%2F%2Fw.qq.com%2Fproxy.html&f_url=loginerroralert&strong_login=1&login_state=10&t=20231023001"
# 假设的登录接口，实际可能需要根据抓包分析得到正确的接口地址
login_api = "https://example.com/login"

session = requests.session()

try:
    resp_qq = session.get(qq)
    qq_header_json = json.dumps(dict(resp_qq.headers), ensure_ascii=False, indent=2)
    logging.info(f"腾讯请求状态码: {resp_qq.status_code}\n")

    # 获取 QQ 官网响应中的 cookie
    cookies = resp_qq.cookies

    # 在请求 QQ 登录页面时带上从 QQ 官网获取的 cookie
    resp_qq_login = session.get(qq_login, cookies=cookies)
    qq_login_header_json = json.dumps(dict(resp_qq_login.headers), ensure_ascii=False, indent=2)
    logging.info(f"QQ 登录页面请求状态码: {resp_qq_login.status_code}\n")

    # 预留 QQ 账号和密码的位置
    qq_number = "2636433628"
    qq_password = "1"

    # 假设登录请求需要的表单数据，实际参数需要根据抓包分析得到
    login_data = {
        "qq_number": qq_number,
        "qq_password": qq_password
    }

    # 发起登录请求
    resp_login = session.post(login_api, data=login_data, cookies=cookies)
    login_header_json = json.dumps(dict(resp_login.headers), ensure_ascii=False, indent=2)
    logging.info(f"QQ 登录请求状态码: {resp_login.status_code}\n")
    logging.info(f"QQ 登录响应内容: {resp_login.text}")

    try:
        response_data = resp_login.json()
        # 假设响应中包含 success 字段表示登录结果
        assert response_data.get('success', False), "登录失败，响应数据中 success 字段为 false"
        logging.info("登录成功！")
    except (json.JSONDecodeError, AssertionError) as e:
        logging.error(f"登录验证失败: {e}")

except requests.RequestException as error:
    logging.error(f"请求发生错误: {error}")
finally:
    session.close()
