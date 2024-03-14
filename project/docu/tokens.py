from datetime import datetime, timedelta
import jwt

def getToken(payload: dict, key: str, acc:bool=False):
    now = datetime.utcnow()
    payload['iss'] = "webdomain"
    payload['iat'] = now.timestamp()
    payload['sub'] = "subject"
    if acc:
        payload['tokentype'] = "access"
        payload['exp'] = (now + timedelta(minutes=5)).timestamp()
    else:
        payload['tokentype'] = "refresh"
        payload['exp'] = (now + timedelta(days=30)).timestamp()
    payload['scope'] = "openid"
    print(payload)
    token = jwt.encode(payload=payload, key=key)
    return token

def verifyToken(token, key):
    try:
        decoded_data = jwt.decode(jwt=token, key=key, algorithms=["HS256"])
        return decoded_data
    except jwt.exceptions.InvalidSignatureError:
        return {"errormsg": 'at VerifyToken InvalidSignatureError'}
    except jwt.exceptions.ExpiredSignatureError:
        return {"errormsg": 'at VerifyToken InvalidSignatureError'}
    except jwt.exceptions.DecodeError:
        return {"errormsg": 'at VerifyToken DecodeError'}
    except ValueError:
        return {"errormsg": 'at VerifyToken ValueError'}
