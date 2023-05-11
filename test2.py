import requests

url = "https://api.chatgptai.com/data"
headers = {"Authorization": "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"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("API key is correct!")
else:
    print("API key is incorrect.")
