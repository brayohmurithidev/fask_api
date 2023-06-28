import jwt
from datetime import datetime, timedelta
import sys

# Set the expiration time to 1 hour from the current time
expiration_time = datetime.utcnow() + timedelta(hours=1)

# ENCODE THE TOKEN WITH HS256
secret_key = "Murume"
payload = {
    "username": "fazitech",
    "role": ["admin", "donor", "foodbank", "recipient"],
    # when the token expires, "exp": datetime.date(ke=pytz.timezone("EAT")
    "exp": expiration_time,
    'sub': 'user123',
}

token = jwt.encode(payload, secret_key, algorithm='HS256')
