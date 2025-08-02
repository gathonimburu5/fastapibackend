from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import JWTError, jwt
from application.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, oauth2_scheme
from application.models.user_model import Signup
from application.utility.security import hash_password, verify_password
from application.schemas.user_schema import UserCreate, UserLogin
from fastapi import HTTPException, status, Depends

class AuthenticationService:
    def create_user(self, user: UserCreate, db: Session):
        existing_user = db.query(Signup).filter(Signup.username == user.username).first()
        if existing_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
        hashed_password = hash_password(user.password)
        new_user = Signup(
            full_name=user.full_name,
            email_address=user.email_address,
            phone_number=user.phone_number,
            username=user.username,
            password=hashed_password,
            date_of_birth=user.date_of_birth,
            profile_picture=user.profile_picture,
            status=user.status or "active"
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def authenticate_user(self, db: Session, username: str, password: str):
        user = db.query(Signup).filter(Signup.username == username).first()
        if not user or not verify_password(password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return user

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def get_current_user(self, db: Session, token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        user = db.query(Signup).filter(Signup.username == username).first()
        if user is None:
            raise credentials_exception
        return user

    def login_user(self, db: Session, user_login: UserLogin):
        user = self.authenticate_user(db, user_login.username, user_login.password)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self.create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer", "user": user}