import requests

# 在问url and api
url = "https://www.13042332817.top"

# url = "https://www.gaosijiaoyu.cn"
resource = "/message"
input_message = {"message": [{"role": "user", "content": "你好"}], "mode": "v3.5", "key": None}
response = requests.post(url + resource, json=input_message)
text = response.text
print(text)
