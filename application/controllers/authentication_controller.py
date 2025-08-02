from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from application.config import get_db
from application.schemas.user_schema import UserCreate, UserLogin, UserOut
from application.services.authentication_service import AuthenticationService
from fastapi.responses import JSONResponse

authentication_router = APIRouter()
authService = AuthenticationService()

@authentication_router.post("/signup", response_model=UserOut)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    authService.create_user(user, db)
    return JSONResponse(content={"message": "successfully registered users", "code": status.HTTP_201_CREATED}, status_code=status.HTTP_201_CREATED)

@authentication_router.post("/login", response_model=UserOut)
def login(user: UserLogin, db: Session = Depends(get_db)):
    user_record = authService.login_user(db, user)
    if not user_record:
        return JSONResponse(content={"error": "invalid credentials", "code": status.HTTP_401_UNAUTHORIZED}, status_code=status.HTTP_401_UNAUTHORIZED)
    return user_record

@authentication_router.get("/CurrentUser", response_model=UserOut)
def get_current_user(current_user: UserOut = Depends(authService.get_current_user), db: Session = Depends(get_db)):
    if not current_user:
        return JSONResponse(content={"error": "user not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return current_user