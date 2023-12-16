import base64

url = 'example'
encoded_url = base64.b64encode(url.encode()).decode()

print(encoded_url)