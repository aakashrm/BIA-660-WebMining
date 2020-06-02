import requests

r = requests.get("https://httpbin.org/")

print(r.status_code)
print(r.headers)
print(r.content)
