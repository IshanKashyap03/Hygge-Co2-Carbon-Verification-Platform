import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from backend.common.config import JWT_ALGORITHM, JWT_SECRET_KEY
from backend.common.logger import logger

security = HTTPBearer()


# TODO: Handle in middleware
def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        logger.error("Error in decoding token. Error: {exception}", exception=e)
        raise HTTPException(
            status_code=500,
            detail="Internal server error in decoding token. Try again later.",
        )


def get_current_user(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    return decode_access_token(token)
