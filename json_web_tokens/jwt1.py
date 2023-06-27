import jwt
from datetime import datetime, timedelta

# Set the expiration time to 1 hour from the current time
expiration_time = datetime.utcnow() + timedelta(hours=1)

# ENCODE THE TOKEN WITH HS256
secret_key = "Murume"
payload = {
    "username": "fazitech",
    "role": "admin",
    # when the token expires, "exp": datetime.date(ke=pytz.timezone("EAT")
    "exp": expiration_time,
    'sub': 'user123',
}

token = jwt.encode(payload, secret_key, algorithm='HS256')

print(token)

# Decoding a JWT
decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
print(decoded_token)
