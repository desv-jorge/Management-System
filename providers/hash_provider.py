from passlib.context import CryptContext # pyright: ignore[reportMissingModuleSource]

pwd_context = CryptContext(schemes="bcrypt")

def gen_hash(texto):
    return pwd_context.hash(texto)

def verify_hash(texto, hash):
    return pwd_context.verify(texto, hash)