from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hasher:
    @staticmethod
    def password_verify(password, hassed_password):
        return pwd_context.verify(password, hassed_password)

    @staticmethod
    def get_hashed_password(password):
        return pwd_context.hash(password)