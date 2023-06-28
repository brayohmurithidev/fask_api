from jwt1 import token
import jwt

# CHECK TOKEN VALIDITY


def validate_token(func):
    def wrapper(*args, **kwargs):
        try:
            # Decoding a JWT
            jwt.decode(token, 'Murume', algorithms=['HS256'])
            print("You are verified")
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(str(e))
    return wrapper


@validate_token
def test():
    print("Your endpoint")


test()
