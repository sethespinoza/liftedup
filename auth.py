from passlib.context import CryptContext
from jose import JWTError, jwt 
from datetime import datetime, timedelta

# tells passlib to use bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# secret key to sign tokens
SECRET_KEY = "secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    # copy of data to prevent modification of original
    to_encode = data.copy()
    # token expires after 30 mins
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    # encode everything into token string
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
