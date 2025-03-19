import requests
import logging
import json


def send_request(session, method, url):
    """
    封装发送请求的逻辑
    :param session: requests 会话对象
    :param method: 请求方法
    :param url: 请求的 URL
    :return: 响应对象或 None
    """
    try:
        resp = session.request(method, url)
        assert resp.status_code == 200, f"{url} 请求状态码异常，实际为: {resp.status_code}"
        headers_json = json.dumps(dict(resp.headers), ensure_ascii=False, indent=2)
        logging.info(f"\n{url} 请求状态码: {resp.status_code} \n响应头信息: {headers_json}")
        return resp
    except AssertionError as assert_error:
        logging.error(assert_error)
    except requests.RequestException as error:
        logging.error(f"请求 {url} 发生错误: {error}")
    return None
