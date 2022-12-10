import config
import requests # pip install requests
import jwt	# pip install pyjwt
from datetime import datetime as date

# Admin API key goes here
key = config.GHOST_ADMIN_API_KEY

# Split the key into ID and SECRET
id, secret = key.split(':')

# Prepare header and payload
iat = int(date.now().timestamp())

header = {'alg': 'HS256', 'typ': 'JWT', 'kid': id}
payload = {
    'iat': iat,
    'exp': iat + 5 * 60,
    'aud': '/admin/'
}

# Create the token (including decoding secret)
token = jwt.encode(payload, bytes.fromhex(secret), algorithm='HS256', headers=header)

# Make an authenticated request to create a post
url = f'{config.GHOST_DOMAIN}/ghost/api/admin/posts/?source=html'
headers = {'Authorization': 'Ghost {}'.format(token)}
body = {'posts': [{'title': 'Test HTML Source', "html": "<h1>level 1</h1> <p>My post content. Work in progress...</p>"}]}
r = requests.post(url, json=body, headers=headers)

print(r)