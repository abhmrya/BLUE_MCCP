print("Hello from Docker!")

import requests

response = requests.get("https://google.com")
print(f'response .....',dir(response))
print(f'response .....',repr(response))
print("Status:", response.status_code)