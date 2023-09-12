import requests

response = requests.get("https://raw.githubusercontent.com/TianxiangR/cmput-404-lab0/master/scratch.py")

print(response.text)