from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from application.config import get_db
from application.utility.token import get_current_user
from application.schemas.user_schema import UserToken
from fastapi.responses import JSONResponse
from application.services.trail_service import AuditTrailService
from application.schemas.trail_schema import AuditTrailOut

trail_router = APIRouter()
auditService = AuditTrailService()

@trail_router.get("/trail", response_model=list[AuditTrailOut])
def get_audit_trail(db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    return auditService.getAllAuditTrail(db)
