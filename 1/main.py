import requests
import logging
import json

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


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


def main():
    # 配置请求信息
    requests_config = [
        {"method": "get", "url": "http://www.baidu.com/"},
        {"method": "get", "url": "http://www.qq.com/"}
    ]
    session = requests.session()
    for config in requests_config:
        method = config["method"]
        url = config["url"]
        send_request(session, method, url)
    session.close()


if __name__ == "__main__":
    main()
