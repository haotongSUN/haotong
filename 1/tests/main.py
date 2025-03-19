import requests
import logging
import yaml

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    try:
        # 修改文件路径为上级目录
        with open('../data/data.yaml', 'r', encoding='utf-8') as file:
            requests_config = yaml.safe_load(file)

        session = requests.session()
        from tests.request_sender import send_request
        for config in requests_config:
            method = config["method"]
            url = config["url"]
            send_request(session, method, url)
        session.close()
    except FileNotFoundError:
        logging.error("未找到 YAML 配置文件 'data.yaml'。")
    except yaml.YAMLError as yaml_error:
        logging.error(f"解析 YAML 文件时出错: {yaml_error}")


if __name__ == "__main__":
    main()
