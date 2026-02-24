from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])

def hashed_pass(password:str):
    return pwd_context.hash(password)
    

def passwor_verify(password:str,hashed:str):
    
    is_correct = pwd_context.verify(password,hashed)
    
    return is_correct
    

