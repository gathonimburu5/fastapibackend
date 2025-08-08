from sqlalchemy.orm import Session
from application.models.trail_model import AuditTrail
from application.models.user_model import Signup

class AuditTrailService:
    def getAllAuditTrail(self, db: Session):
        return db.query(
            AuditTrail.id,
            AuditTrail.module_id,
            AuditTrail.module_name,
            AuditTrail.action_taken,
            AuditTrail.user_id,
            Signup.full_name.label("created_by"),
            AuditTrail.created_on
        ).join(Signup, Signup.id == AuditTrail.user_id).all()