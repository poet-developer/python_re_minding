import requests
import re

response = requests.get("https://bkksg.com")
page = response.text
print(page)

# urls = re.findall('"card-title"', page)

# print(urls)