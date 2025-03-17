import requests
import logging
import json

logging.basicConfig(level=logging.INFO)

baidu = "http://www.baidu.com/"
qq = "http://www.qq.com/"

session = requests.session()
method = 'get'
try:
    resp_baidu = session.request(method, url=baidu)
    assert resp_baidu.status_code == 200, f"百度请求状态码异常，实际为: {resp_baidu.status_code}"
    baidu_headers_json = json.dumps(dict(resp_baidu.headers), ensure_ascii=False, indent=2)
    logging.info(f"\n百度请求状态码: {resp_baidu.status_code} \n响应头信息: {baidu_headers_json}")

    resp_qq = session.request(method, url=qq)
    assert resp_qq.status_code == 200, f"腾讯请求状态码异常，实际为: {resp_qq.status_code}"
    qq_header_json = json.dumps(dict(resp_qq.headers), ensure_ascii=False, indent=2)
    logging.info(f"\n腾讯请求状态码: {resp_qq.status_code} \n响应头信息: {qq_header_json}")

except AssertionError as assert_error:
    logging.error(assert_error)
except requests.RequestException as error:
    logging.error(f"请求发生错误: {error}")
finally:
    session.close()
