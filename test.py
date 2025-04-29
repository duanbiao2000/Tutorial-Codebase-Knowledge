from google import genai

import os

# 设置代理
# os.environ["http_proxy"] = "http://127.0.0.1:7890"
# os.environ["https_proxy"] = "http://127.0.0.1:7890"


client = genai.Client(api_key="AIzaSyDLhkdHMsD-eLSeYACX7pxVOmN91AKofCc")
model = "gemini-2.0-flash-exp-image-generation"
print("before API call")
response = client.models.generate_content(model=model, contents=["Test prompt"])
print("after API call")
print(response.text)
