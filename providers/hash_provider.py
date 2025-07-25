from passlib.context import CryptContext # pyright: ignore[reportMissingModuleSource]

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def gen_hash(texto):
    return pwd_context.hash(texto)

def verify_hash(password: str, hash: str) -> bool:
    return pwd_context.verify(password, hash)