import requests

t = requests.get("https://api.ip.sb/ip")
print(t.text)