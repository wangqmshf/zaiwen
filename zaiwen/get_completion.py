import requests


def get_completion(prompt, model="v3.5", url="https://www.13042332817.top"):
    """
    prompt: 对应的提示
    model: 调用的模型，默认为 "v3.5"
    """

    # url = "https://www.gaosijiaoyu.cn"
    resource = "/message"
    messages = {"message": [{"role": "user", "content": prompt}], "mode": model, "key": None}
    response = requests.post(url + resource, json=messages)
    # 调用 在问 的 message 接口
    return response.text
