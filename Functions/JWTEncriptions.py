from django.http import JsonResponse
import jwt

def decode_jwt(token):
    try:
        # Replace 'your-secret-key' with the actual secret key used to encode the JWT
        decoded_data = jwt.decode(token, 'automate0323', algorithms=['HS256'])
        return decoded_data
    except jwt.ExpiredSignatureError as error:
        return error  # Token has expired
    except jwt.InvalidTokenError as error:
        return error  # Invalid token
    
def encode_jwt(payload):
    try:
        # Replace 'your-secret-key' with the actual secret key used to encode the JWT
        decoded_data = jwt.encode(payload, 'automate0323', algorithm='HS256')
        return decoded_data
    except jwt.ExpiredSignatureError as error:
        raise error  # Token has expired
    except jwt.InvalidTokenError as error:
        raise error  # Invalid token
    