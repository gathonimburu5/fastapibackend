from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from application.config import get_db
from application.schemas.user_schema import UserCreate, UserLogin, UserToken
from application.services.authentication_service import AuthenticationService
from fastapi.responses import JSONResponse
from application.utility.token import create_access_token

authentication_router = APIRouter()
authService = AuthenticationService()

@authentication_router.post("/register")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    authService.create_user(user, db)
    return JSONResponse(content={"message": "successfully registered users", "code": status.HTTP_201_CREATED}, status_code=status.HTTP_201_CREATED)

@authentication_router.post("/login", response_model=UserToken)
def login(user: UserLogin, db: Session = Depends(get_db)):
    user_record = authService.authenticate_user(db, user.username, user.password)
    if not user_record:
        return JSONResponse(content={"error": "invalid credentials", "code": status.HTTP_401_UNAUTHORIZED}, status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token(data={"sub": user_record.username})
    return {"access_token": access_token, "token_type": "bearer"}